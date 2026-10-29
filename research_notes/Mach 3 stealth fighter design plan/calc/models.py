"""Physics and sizing models for the Mach 3 LO fighter entry analysis.

Sections
  1. Aerodynamics: CD0(M) table, K1(M) (subsonic constant, Raymer supersonic no-suction formula)
  2. Propulsion: Mattingly (Aircraft Engine Design, 2nd ed.) installed thrust lapse and TSFC fits
  3. Aero-thermal: stagnation / adiabatic-wall temperature, Eckert reference-temperature turbulent
     flat-plate heat transfer, radiative-equilibrium skin temperature, Planck band exitance
  4. Constraint analysis: Mattingly master equation, takeoff, landing
  5. Weights: Raymer empty-weight regressions, Raymer segment fractions
  6. Mission simulation (Breguet range/endurance, combat, energy-method climb) and
     fixed-point / bisection takeoff-weight sizing
All units SI unless stated; TSFC in 1/h (lbm/(lbf h) == kg/(kgf h)).
"""
import math
import numpy as np

import assumptions as A
from atmosphere import isa, G0, R_AIR, GAMMA, A_SL

SIGMA = 5.670374419e-8
H_PL, C_LIGHT, K_B = 6.62607015e-34, 2.99792458e8, 1.380649e-23

# =============================================================== 1. aerodynamics
_CD0_M = np.array([m for m, _ in A.CD0_TABLE])
_CD0_V = np.array([c for _, c in A.CD0_TABLE])


def cd0(M, scale_super=1.0):
    """CD0(M); scale_super multiplies the value progressively from M1.0 (x1) to M2.0+ (x scale)."""
    c = float(np.interp(M, _CD0_M, _CD0_V))
    if scale_super != 1.0 and M > 1.0:
        w = min(1.0, M - 1.0)
        c *= 1.0 + (scale_super - 1.0) * w
    return c


def k_super_raymer(M, ar=A.AR, sweep_deg=A.SWEEP_LE_DEG):
    """Raymer supersonic drag-due-to-lift, zero LE suction: K = A(M^2-1)cosL/(4A sqrt(M^2-1) - 2)."""
    b2 = M * M - 1.0
    return ar * b2 * math.cos(math.radians(sweep_deg)) / (4.0 * ar * math.sqrt(b2) - 2.0)


def k1(M, cfg=None):
    ks = (cfg or {}).get('k1_sub', A.K1_SUB)
    if M <= 0.9:
        return ks
    k12 = max(ks, k_super_raymer(1.2))
    if M < 1.2:
        return ks + (k12 - ks) * (M - 0.9) / 0.3
    return max(ks, k_super_raymer(M))


def polar(M, CL, cfg=None):
    cfg = cfg or {}
    return cd0(M, cfg.get('cd0_scale', 1.0)) + A.CDR + k1(M, cfg) * CL * CL + A.K2 * CL


def ld_max(M, cfg=None):
    cfg = cfg or {}
    c, k = cd0(M, cfg.get('cd0_scale', 1.0)), k1(M, cfg)
    return 1.0 / (2.0 * math.sqrt(c * k)), math.sqrt(c / k)


# =============================================================== 2. propulsion
def theta_delta(M, T, p):
    f = 1.0 + 0.5 * (GAMMA - 1.0) * M * M
    return T / 288.15 * f, p / 101325.0 * f ** (GAMMA / (GAMMA - 1.0))


def lapse(eng, throttle, M, h, cfg=None):
    """Installed thrust lapse alpha = T / T_SL(max, static), Mattingly 2nd ed. eq. family 2.54.

    eng: dict with kind ('LBPTF' or 'TJ'), TR, knockdown_supersonic.
    throttle: 'max' (afterburner) or 'mil' (dry)."""
    cfg = cfg or {}
    s = isa(h)
    th0, d0 = theta_delta(M, s['T'], s['p'])
    TR = eng['TR']
    if eng['kind'] == 'LBPTF':
        if throttle == 'max':
            a = d0 if th0 <= TR else d0 * (1.0 - 3.5 * (th0 - TR) / th0)
        else:
            a = 0.6 * d0 if th0 <= TR else 0.6 * d0 * (1.0 - 3.8 * (th0 - TR) / th0)
    elif eng['kind'] == 'TJ':
        if throttle == 'max':
            a = d0 * (1.0 - 0.3 * (th0 - 1.0) - 0.1 * math.sqrt(M))
            if th0 > TR:
                a -= d0 * 1.5 * (th0 - TR) / th0
        else:
            a = 0.8 * d0 * (1.0 - 0.16 * math.sqrt(M))
            if th0 > TR:
                a -= 0.8 * d0 * 24.0 * (th0 - TR) / ((9.0 + M) * th0)
    else:
        raise ValueError(eng['kind'])
    kd = cfg.get('knockdown', eng.get('knockdown_supersonic', 1.0))
    if kd != 1.0 and M > 1.5:
        a *= 1.0 + (kd - 1.0) * min(1.0, (M - 1.5) / 1.0)   # ramps in from M1.5 to M2.5
    return max(a, 0.0)


def tsfc(eng, throttle, M, h, cfg=None):
    """Installed TSFC [1/h], Mattingly 2nd ed. fits, times sqrt(T/T_SL)."""
    cfg = cfg or {}
    th = isa(h)['T'] / 288.15
    coef = {('LBPTF', 'mil'): (0.9, 0.30), ('LBPTF', 'max'): (1.6, 0.27),
            ('TJ', 'mil'): (1.1, 0.30), ('TJ', 'max'): (1.5, 0.23)}[(eng['kind'], throttle)]
    return (coef[0] + coef[1] * M) * math.sqrt(th) * cfg.get('tsfc_scale', A.TSFC_SCALE)


def mil_e_5007d_recovery(M):
    """MIL-E-5007D inlet total-pressure recovery (reference only; not applied to lapse)."""
    return 1.0 if M <= 1.0 else 1.0 - 0.075 * (M - 1.0) ** 1.35


# =============================================================== 3. aero-thermal
def t_stag(T, M):
    return T * (1.0 + 0.5 * (GAMMA - 1.0) * M * M)


def t_aw(T, M, r=A.R_TURB):
    return T * (1.0 + r * 0.5 * (GAMMA - 1.0) * M * M)


def _mu(T):
    return 1.458e-6 * T ** 1.5 / (T + 110.4)


def h_conv(M, h, Tw, x):
    """Turbulent flat-plate heat-transfer coefficient (W/m2K) at distance x [m].

    Eckert reference temperature T*/Te = 1 + 0.032 M^2 + 0.58 (Tw/Te - 1);
    Schultz-Grunow local skin friction cf = 0.370 (log10 Re*)^-2.584;
    Colburn-Reynolds analogy St = (cf/2) Pr^(-2/3)."""
    s = isa(h)
    Te, pe = s['T'], s['p']
    u = M * s['a']
    Ts = Te * (1.0 + 0.032 * M * M + 0.58 * (Tw / Te - 1.0))
    rho_s = pe / (R_AIR * Ts)
    Re = rho_s * u * x / _mu(Ts)
    cf = 0.370 / math.log10(Re) ** 2.584
    St = 0.5 * cf * A.PR ** (-2.0 / 3.0)
    return St * rho_s * u * A.CP_AIR, Re


def wall_temp_radiative_eq(M, h, x, eps, r=A.R_TURB, T_env=None):
    """Steady skin temperature with convective heating balanced by radiation to T_env (default
    = ambient static temperature); inner surface adiabatic (no heat into structure or fuel)."""
    s = isa(h)
    Te = s['T']
    Tenv = Te if T_env is None else T_env
    Taw = t_aw(Te, M, r)
    lo, hi = Tenv, Taw
    for _ in range(80):
        Tw = 0.5 * (lo + hi)
        hc, _ = h_conv(M, h, Tw, x)
        f = hc * (Taw - Tw) - eps * SIGMA * (Tw ** 4 - Tenv ** 4)
        if f > 0:
            lo = Tw
        else:
            hi = Tw
    hc, Re = h_conv(M, h, Tw, x)
    return Tw, hc, Re, Taw


def band_exitance(T, lam1_um, lam2_um, eps=1.0, n=4000):
    lam = np.linspace(lam1_um, lam2_um, n) * 1e-6
    c1 = 2.0 * math.pi * H_PL * C_LIGHT ** 2
    c2 = H_PL * C_LIGHT / K_B
    with np.errstate(over='ignore'):
        Ml = c1 / (lam ** 5 * (np.exp(c2 / (lam * T)) - 1.0))
    return eps * float(np.trapezoid(Ml, lam))


# =============================================================== 4. constraint analysis
def tw_required(ws_to, M, h, n, beta, Ps, throttle, eng, cfg=None):
    """Mattingly master equation, T_SL/W_TO for a flight condition (K2=0, CDR from assumptions)."""
    s = isa(h)
    V = M * s['a']
    q = 0.5 * s['rho'] * V * V
    al = lapse(eng, throttle, M, h, cfg)
    if al <= 0.0:
        return float('inf')
    ws = beta * ws_to
    CL = n * ws / q
    DW = q * polar(M, CL, cfg) / ws
    return beta / al * (DW + Ps / V)


def tw_takeoff(ws_to, s_g, eng, clmax=A.CLMAX_TO, cfg=None):
    """Ground roll s_g [m] = acceleration distance + rotation (t_R * V_TO). Aero drag neglected,
    rolling friction included; thrust taken at 0.7 V_TO (average)."""
    s0 = isa(0.0)
    Vto = A.K_TO * math.sqrt(2.0 * ws_to / (s0['rho'] * clmax))
    s_acc = s_g - A.T_ROT * Vto
    if s_acc <= 0:
        return float('inf')
    al = lapse(eng, 'max', 0.7 * Vto / s0['a'], 0.0, cfg)
    return (Vto ** 2 / (2.0 * G0 * s_acc) + A.MU_ROLL) / al


def ws_landing_max(s_l, clmax=A.CLMAX_L, beta=A.BETA_LAND, mu=A.MU_BRAKE):
    """Largest W_TO/S meeting landing ground roll s_l: s = t_fr V_TD + V_TD^2/(2 g mu)."""
    rho = isa(0.0)['rho']
    a = 1.0 / (2.0 * G0 * mu)
    V = (-A.T_FREE_ROLL + math.sqrt(A.T_FREE_ROLL ** 2 + 4.0 * a * s_l)) / (2.0 * a)
    Vs = V / A.K_TD
    return Vs ** 2 * rho * clmax / (2.0 * beta)


# =============================================================== 5. weights
def we_frac_simple(W0_kg, K=1.0):
    c = A.RAYMER_SIMPLE
    return K * c['A_lb'] * (W0_kg * A.LB_PER_KG) ** c['C'] * c['Kvs']


def we_frac_detailed(W0_kg, tw, ws_pa, ar=A.AR, mmax=A.MMAX, K=1.0):
    c = A.RAYMER_DETAILED
    return K * (c['a'] + c['b'] * (W0_kg * A.LB_PER_KG) ** c['C1'] * ar ** c['C2'] * tw ** c['C3']
                * (ws_pa * A.PSF_PER_PA) ** c['C4'] * mmax ** c['C5'])


def raymer_accel_fraction(M):
    """Raymer climb/accelerate fraction from M~0.1 to M (refined-sizing fits)."""
    return 1.0065 - 0.0325 * M if M < 1.0 else 0.991 - 0.007 * M - 0.01 * M * M


# =============================================================== 6. mission & sizing
def _cruise_point(M, h, Wkg, S, T_sl, eng, throttle, cfg):
    s = isa(h)
    V = M * s['a']
    q = 0.5 * s['rho'] * V * V
    CL = Wkg * G0 / (q * S)
    CD = polar(M, CL, cfg)
    D = q * S * CD
    Tav = lapse(eng, throttle, M, h, cfg) * T_sl
    return dict(h=h, V=V, CL=CL, LD=CL / CD, D=D, Tav=Tav, ok=Tav >= D)


def best_cruise(M, Wkg, S, T_sl, eng, h_rng, throttle, cfg):
    """Pick altitude in h_rng maximising L/D with thrust available >= drag.
    throttle 'auto': dry if dry thrust suffices at the chosen point, else max AB.
    For Mach >= 2.5 the 'auto' mode always uses max AB (dry-lapse fits not trusted there)."""
    hs = np.arange(h_rng[0], h_rng[1] + 1.0, 250.0)
    modes = ['mil', 'max'] if (throttle == 'auto' and M < 2.5) else (['max'] if throttle == 'auto' else [throttle])
    for mode in modes:
        pts = [_cruise_point(M, h, Wkg, S, T_sl, eng, mode, cfg) for h in hs]
        ok = [pt for pt in pts if pt['ok']]
        if ok:
            best = max(ok, key=lambda d: d['LD'])
            best['throttle'] = mode
            best['thrust_short'] = False
            return best
    best = max(pts, key=lambda d: d['LD'])
    best['throttle'] = modes[-1]
    best['thrust_short'] = True
    return best


def energy_climb(Wkg, S, T_sl, eng, path, cfg, n=600):
    """Energy-state climb/acceleration fuel: d ln W = -c T dhe / (V (T - D)), max AB."""
    pts = []
    for (M1, h1), (M2, h2) in zip(path[:-1], path[1:]):
        for i in range(n // (len(path) - 1)):
            f = i / (n // (len(path) - 1))
            pts.append((M1 + f * (M2 - M1), h1 + f * (h2 - h1)))
    pts.append(path[-1])
    lnW, t = math.log(Wkg), 0.0
    for (M1, h1), (M2, h2) in zip(pts[:-1], pts[1:]):
        he1 = h1 + (M1 * isa(h1)['a']) ** 2 / (2 * G0)
        he2 = h2 + (M2 * isa(h2)['a']) ** 2 / (2 * G0)
        Mm, hm = 0.5 * (M1 + M2), 0.5 * (h1 + h2)
        cp = _cruise_point(Mm, hm, math.exp(lnW), S, T_sl, eng, 'max', cfg)
        if cp['Tav'] <= cp['D']:
            return None, None
        c = tsfc(eng, 'max', Mm, hm, cfg) / 3600.0
        dhe = he2 - he1
        lnW -= c * cp['Tav'] * dhe / (cp['V'] * (cp['Tav'] - cp['D']))
        t += dhe * math.exp(lnW) * G0 / (cp['V'] * (cp['Tav'] - cp['D']))
    return math.exp(lnW) / Wkg, t


def fly(profile, W0, des, cfg=None):
    """Simulate a mission. des: dict(ws=W_TO/S [N/m2], tw=T_SL/W_TO, eng=engine dict).
    Returns per-segment log and fuel totals [kg]."""
    cfg = cfg or {}
    S = W0 * G0 / des['ws']
    T_sl = des['tw'] * W0 * G0
    eng = des['eng']
    payload = cfg.get('payload', A.W_PAYLOAD)
    W = W0
    burned_mission = burned_reserve = 0.0
    log = []
    for seg in profile:
        typ = seg['type']
        Wb = W
        info = ''
        if typ == 'fixed':
            W *= seg['f']
            info = f"f={seg['f']:.3f}"
        elif typ == 'accel':
            M1, M2 = seg.get('M1'), seg['M2']
            if cfg.get('climb_method', 'raymer') == 'energy' and 'path' in seg:
                fr, tclimb = energy_climb(W, S, T_sl, eng, seg['path'], cfg)
                if fr is None:
                    return dict(feasible=False, reason='thrust < drag on climb path', log=log)
                info = f"energy method, {tclimb / 60:.1f} min"
            else:
                fr = raymer_accel_fraction(M2) / (raymer_accel_fraction(M1) if M1 else 1.0)
                info = 'Raymer fit'
            W *= fr
            info += f", f={fr:.4f}"
        elif typ == 'cruise':
            M = seg['M']
            Wmid = W * 0.97
            for _ in range(4):
                pt = best_cruise(M, Wmid, S, T_sl, eng, seg['h'], seg.get('throttle', 'auto'), cfg)
                c = tsfc(eng, pt['throttle'], M, pt['h'], cfg)
                fr = math.exp(-seg['R'] * (c / 3600.0) / (pt['V'] * pt['LD']))
                Wmid = W * 0.5 * (1.0 + fr)
            W *= fr
            info = (f"h={pt['h'] / 1e3:.2f} km, L/D={pt['LD']:.2f}, CL={pt['CL']:.3f}, {pt['throttle']}, "
                    f"c={c:.2f}/h, f={fr:.4f}" + (' THRUST SHORT' if pt['thrust_short'] else ''))
            seg_pt = pt
        elif typ == 'combat':
            al = lapse(eng, 'max', seg['M'], seg['h'], cfg)
            c = tsfc(eng, 'max', seg['M'], seg['h'], cfg)
            fuel = c / 3600.0 * al * T_sl * seg['t'] / G0
            W -= fuel
            info = f"{seg['t'] / 60:.0f} min max AB, alpha={al:.3f}, c={c:.2f}/h"
        elif typ == 'drop':
            W -= payload * A.PAYLOAD_DROP_FRACTION
            info = f"-{payload * A.PAYLOAD_DROP_FRACTION:.0f} kg payload"
        elif typ == 'loiter':
            M_lo = 0.4
            ldm, clopt = ld_max(M_lo, cfg)
            V = math.sqrt(2 * W * G0 / (isa(0.0)['rho'] * S * clopt))
            M_lo = V / A_SL
            ldm, _ = ld_max(M_lo, cfg)
            c = tsfc(eng, 'mil', M_lo, 0.0, cfg)
            fr = math.exp(-seg['t'] * (c / 3600.0) / ldm)
            W *= fr
            info = f"SL, M={M_lo:.2f}, L/D={ldm:.2f}, c={c:.2f}/h, f={fr:.4f}"
        else:
            raise ValueError(typ)
        dW = Wb - W
        if typ != 'drop':
            if seg.get('reserve'):
                burned_reserve += dW
            else:
                burned_mission += dW
        log.append(dict(label=seg['label'], W_start=Wb, W_end=W, fuel=dW if typ != 'drop' else 0.0, info=info))
    usable = burned_mission * (1.0 + A.RESERVE_FRAC_MISSION) + burned_reserve
    Wf = usable / (1.0 - A.TRAPPED_FRAC)
    return dict(feasible=True, log=log, burned_mission=burned_mission, burned_reserve=burned_reserve,
                Wf=Wf, W_end=W, S=S, T_sl=T_sl)


def empty_weight(W0, des, cfg):
    """K_we x Raymer regression + explicit engine-mass delta for T/W away from TW_REF."""
    K = cfg.get('K_we', 1.0)
    if cfg.get('we_method', 'detailed') == 'simple':
        we = we_frac_simple(W0, K) * W0
    else:
        we = we_frac_detailed(W0, des['tw'], des['ws'], A.AR, cfg.get('Mmax', A.MMAX), K) * W0
    if cfg.get('engine_correction', True):
        twr = cfg.get('twr_eng', A.TWR_ENG[des['eng_key']])
        we += (des['tw'] - A.TW_REF) * W0 / twr
    return we


def size(profile, des, cfg=None, lo=4000.0, hi=400000.0, practical_limit=60000.0):
    """Solve W0 = We(W0) + Wf(W0) + W_crew + W_payload by bisection (robust form of Raymer's
    fixed-point iteration). Returns None-closure if no root below hi."""
    cfg = cfg or {}
    payload = cfg.get('payload', A.W_PAYLOAD)

    def resid(W0):
        r = fly(profile, W0, des, cfg)
        if not r['feasible']:
            return None, r, None
        We = empty_weight(W0, des, cfg)
        return W0 - (We + r['Wf'] + A.W_CREW + payload), r, We

    f_lo, _, _ = resid(lo)
    f_hi, _, _ = resid(hi)
    if f_lo is None or f_hi is None:
        return dict(closed=False, reason='mission infeasible (thrust)')
    if f_hi < 0:
        return dict(closed=False, reason=f'no closure below {hi / 1000:.0f} t')
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        fm, r, We = resid(mid)
        if fm is None:
            return dict(closed=False, reason='mission infeasible (thrust)')
        if fm > 0:
            hi = mid
        else:
            lo = mid
        if hi - lo < 0.5:
            break
    W0 = 0.5 * (lo + hi)
    _, r, We = resid(W0)
    return dict(closed=True, practical=W0 <= practical_limit, W0=W0, We=We, Wf=r['Wf'], S=r['S'],
                T_sl=r['T_sl'], We_frac=We / W0, Wf_frac=r['Wf'] / W0, log=r['log'],
                burned_mission=r['burned_mission'], burned_reserve=r['burned_reserve'])
