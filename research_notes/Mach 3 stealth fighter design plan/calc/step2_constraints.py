"""Step 2: (e) constraint analysis T_SL/W_TO vs W_TO/S, drag polar / lapse / TSFC tables,
design-point selection and its sensitivity. Writes out/step2_constraints.md,
out/constraint_diagram_P2.png, out/constraint_diagram_P1.png, out/design_points.json."""
import json
import math
import os

import numpy as np

import assumptions as A
import models as m
from atmosphere import isa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
os.makedirs(OUT, exist_ok=True)
WS = np.arange(2000.0, 8000.1, 25.0)      # W_TO/S grid, N/m^2

# name, M, h [m], n, beta, Ps [m/s], throttle, applies to Mach-3 engine only?
FLIGHT_CONSTRAINTS = [
    ('M3.0 cruise 20 km (max AB)', 3.0, 20e3, 1.0, 0.80, 0.0, 'max', True),
    ('M3.0 cruise 22 km (max AB)', 3.0, 22e3, 1.0, 0.80, 0.0, 'max', True),
    ('M3.0 cruise 24 km (max AB)', 3.0, 24e3, 1.0, 0.80, 0.0, 'max', True),
    ('Ps 50 m/s M2.5 18 km (accel margin)', 2.5, 18e3, 1.0, 0.80, 50.0, 'max', True),
    ('Supercruise M1.7 13 km (dry)', 1.7, 13e3, 1.0, 0.85, 0.0, 'mil', False),
    ('Supercruise M1.8 15 km (dry)', 1.8, 15e3, 1.0, 0.85, 0.0, 'mil', False),
    ('5 g sustained M0.9 9 km (max AB)', 0.9, 9e3, 5.0, 0.80, 0.0, 'max', False),
    ('Ps 120 m/s M0.9 9 km (max AB)', 0.9, 9e3, 1.0, 0.80, 120.0, 'max', False),
]
TAKEOFF_REQ = 800.0
TAKEOFF_SHOW = [600.0, 800.0, 900.0]
LANDING_REQ = 900.0


def md_table(header, rows):
    s = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    s += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return '\n'.join(s)


def curves(eng, include_m3, cfg=None, turn_g=5.0, s_to=TAKEOFF_REQ):
    cs = {}
    for name, M, h, n, beta, Ps, thr, m3 in FLIGHT_CONSTRAINTS:
        if m3 and not include_m3:
            continue
        if name.startswith('5 g'):
            n = turn_g
            name = f'{turn_g:g} g sustained M0.9 9 km (max AB)'
        cs[name] = np.array([m.tw_required(w, M, h, n, beta, Ps, thr, eng, cfg) for w in WS])
    cs[f'Takeoff ground roll {s_to:.0f} m'] = np.array([m.tw_takeoff(w, s_to, eng, cfg=cfg) for w in WS])
    return cs


def design_point(cs, ws_max):
    env = np.max(np.vstack(list(cs.values())), axis=0)
    feas = WS <= ws_max
    i = int(np.argmin(np.where(feas, env, np.inf)))
    active = max(cs, key=lambda k: cs[k][i])
    return WS[i], env[i], active, env


def plot(cs_show, ws_max, dp, title, fname, refs):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        return None
    fig, ax = plt.subplots(figsize=(9, 6.2))
    for k, v in cs_show.items():
        vv = np.where(np.isfinite(v), v, np.nan)
        ax.plot(WS, vv, label=k, lw=1.6, ls='--' if ('600' in k or '900' in k) else '-')
    ax.axvline(ws_max, color='k', lw=1.4, ls=':', label=f'Landing {LANDING_REQ:.0f} m (max W/S)')
    ax.plot(dp[0], dp[1], 'k*', ms=15, label=f'Design point W/S={dp[0]:.0f} N/m2, T/W={dp[1]:.2f}')
    for nm, (ws, tw) in refs.items():
        ax.plot(ws, tw, 'o', ms=6, mfc='none', mec='0.3')
        ax.annotate(nm, (ws, tw), textcoords='offset points', xytext=(4, 4), fontsize=8, color='0.3')
    ax.set_ylim(0, 2.2)
    ax.set_xlim(WS[0], WS[-1])
    ax.set_xlabel('Takeoff wing loading W_TO/S (N/m^2)')
    ax.set_ylabel('Installed SL static max thrust / W_TO')
    ax.set_title(title, fontsize=10)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=7, loc='upper right')
    fig.tight_layout()
    path = os.path.join(OUT, fname)
    fig.savefig(path, dpi=130)
    plt.close(fig)
    return path


def ref_points():
    r = {}
    for nm, d in A.REF_AIRCRAFT.items():
        r[nm] = (d['W0'] * A.G0 / d['S'], d['T_ab'] / (d['W0'] * A.G0))
    return r


def main():
    out = ['# Step 2 output: drag polar, propulsion models, constraint analysis\n']
    P1, P2 = A.ENGINES['P1'], A.ENGINES['P2']

    # drag polar table
    rows = []
    for M in [0.3, 0.6, 0.9, 1.0, 1.2, 1.5, 1.6, 1.8, 2.0, 2.5, 2.83, 3.0, 3.2]:
        ldm, clo = m.ld_max(M)
        rows.append([M, f'{m.cd0(M):.4f}', f'{m.k1(M):.3f}', f'{ldm:.2f}', f'{clo:.3f}', f'{4 * (M + 3) / M:.1f}' if M >= 1.2 else '-'])
    out.append('## Drag polar CD = CD0(M) + K1(M) CL^2 (wing-referenced)\n\n'
               f'K1: {A.K1_SUB} for M<=0.9, Raymer no-suction supersonic formula (AR={A.AR}, LE sweep {A.SWEEP_LE_DEG} deg) for M>=1.2, '
               'linear blend between.\n\n'
               + md_table(['M', 'CD0', 'K1', '(L/D)max', 'CL*', 'Kuchemann 4(M+3)/M bound'], rows) + '\n')

    # lapse & TSFC tables
    conds = [(0.0, 0.0), (0.9, 9e3), (0.9, 11e3), (1.5, 11e3), (1.7, 13e3), (2.0, 15e3), (2.5, 18e3),
             (2.5, 20e3), (2.83, 20e3), (3.0, 20e3), (3.0, 22e3), (3.0, 24e3), (3.2, 24e3)]
    rows = []
    for M, h in conds:
        s = isa(h)
        th0, d0 = m.theta_delta(M, s['T'], s['p'])
        rows.append([M, h / 1e3, f'{th0:.3f}', f'{d0:.3f}',
                     f"{m.lapse(P1, 'mil', M, h):.3f}", f"{m.lapse(P1, 'max', M, h):.3f}",
                     f"{m.lapse(P2, 'mil', M, h):.3f}", f"{m.lapse(P2, 'max', M, h):.3f}",
                     f'{m.mil_e_5007d_recovery(M):.3f}'])
    out.append(f"## Installed thrust lapse alpha = T/T_SL,max (Mattingly fits)\n\nP1 = {P1['label']}, TR={P1['TR']}; "
               f"P2 = {P2['label']}, TR={P2['TR']}. alpha=0 means the fit predicts no net thrust (beyond validity).\n\n"
               + md_table(['M', 'h (km)', 'theta0', 'delta0', 'P1 dry', 'P1 max', 'P2 dry', 'P2 max', 'MIL-E-5007D recovery (ref.)'], rows) + '\n')
    rows = []
    for M, h in [(0.0, 0.0), (0.9, 11e3), (1.5, 13e3), (2.5, 20e3), (3.0, 21e3), (3.2, 24e3)]:
        rows.append([M, h / 1e3] + [f"{m.tsfc(e, t, M, h):.2f}" for e in (P1, P2) for t in ('mil', 'max')])
    out.append('## Installed TSFC (1/h) from Mattingly fits: LBPTF mil (0.9+0.30M)sqrt(theta), max (1.6+0.27M)sqrt(theta); '
               'TJ mil (1.1+0.30M)sqrt(theta), max (1.5+0.23M)sqrt(theta)\n\n'
               + md_table(['M', 'h (km)', 'P1 LBPTF dry', 'P1 LBPTF max', 'P2 TJ dry', 'P2 TJ max'], rows) + '\n'
               + '\nRaymer Table 3.3-type cruise/loiter TSFC (for comparison): turbojet 0.9/0.8, low-bypass turbofan 0.8/0.7 (1/h).\n')

    ws_max = m.ws_landing_max(LANDING_REQ)
    out.append(f'Landing: s_L = {LANDING_REQ:.0f} m, beta_L = {A.BETA_LAND}, CLmax_L = {A.CLMAX_L}, mu = {A.MU_BRAKE} '
               f'-> W_TO/S <= {ws_max:.0f} N/m2 ({ws_max / A.G0:.0f} kg/m2).\n')

    results = {}
    refs = ref_points()
    for key, eng, inc_m3, title in [('P2', P2, True, 'Mach 3 LO fighter, engine P2 (high-TR AB turbojet), all requirements'),
                                    ('P1', P1, False, 'Same airframe with engine P1 (LBP AB turbofan), Mach 3 requirement removed')]:
        cs = curves(eng, inc_m3)
        ws_d, tw_d, active, env = design_point(cs, ws_max)
        results[key] = dict(ws=float(ws_d), tw=float(tw_d), active=active, ws_max_landing=ws_max)
        # table of curve values at selected W/S
        sel = [2500, 3000, 3500, 4000, 4500, 5000, 6000]
        rows = [[k] + [f'{cs[k][np.argmin(abs(WS - w))]:.3f}' for w in sel] for k in cs]
        rows.append(['ENVELOPE (max)'] + [f'{env[np.argmin(abs(WS - w))]:.3f}' for w in sel])
        out.append(f'## Constraint table, {title}\n\nT_SL/W_TO required at W_TO/S (N/m2):\n\n'
                   + md_table(['Constraint'] + [str(w) for w in sel], rows) + '\n')
        out.append(f'**Design point {key}:** W_TO/S = {ws_d:.0f} N/m2 ({ws_d / A.G0:.0f} kg/m2, {ws_d * A.PSF_PER_PA:.1f} lbf/ft2), '
                   f'T_SL/W_TO = {tw_d:.3f}; active constraint(s) at the minimum: {active}.\n')
        show = dict(cs)
        if key == 'P2':
            for s_to in (600.0, 900.0):
                show[f'Takeoff ground roll {s_to:.0f} m'] = np.array([m.tw_takeoff(w, s_to, eng) for w in WS])
        png = plot(show, ws_max, (ws_d, tw_d), title, f'constraint_diagram_{key}.png', refs)
        if png:
            out.append(f'Plot: `out/{os.path.basename(png)}`\n')

    # P1 at Mach 3: show infeasibility
    out.append('## Mach 3 with the conventional fighter turbofan (P1)\n')
    rows = []
    for h in (20e3, 22e3, 24e3):
        rows.append([h / 1e3, f"{m.lapse(P1, 'max', 3.0, h):.3f}",
                     f"{m.tw_required(4000, 3.0, h, 1, 0.8, 0, 'max', P1):.3g}"])
    out.append(md_table(['h (km)', 'P1 alpha_max at M3', 'T_SL/W_TO required (W/S=4000)'], rows) + '\n')
    for TR in (1.07, 1.3, 1.5, 1.8, 2.1):
        e = dict(P1, TR=TR)
        out.append(f"- LBPTF with TR={TR}: alpha_max at M3/20 km = {m.lapse(e, 'max', 3.0, 20e3):.3f}; "
                   f"at M2.5/18 km = {m.lapse(e, 'max', 2.5, 18e3):.3f}")
    out.append('')

    # sensitivity of P2 design point
    rows = []
    variants = [('Baseline', {}, 5.0, TAKEOFF_REQ, A.CLMAX_TO),
                ('Turn 4 g instead of 5 g', {}, 4.0, TAKEOFF_REQ, A.CLMAX_TO),
                ('Turn 6 g', {}, 6.0, TAKEOFF_REQ, A.CLMAX_TO),
                ('Takeoff roll 600 m', {}, 5.0, 600.0, A.CLMAX_TO),
                ('Takeoff roll 900 m', {}, 5.0, 900.0, A.CLMAX_TO),
                ('CLmax_TO 1.0', {}, 5.0, TAKEOFF_REQ, 1.0),
                ('Supersonic thrust knockdown 0.7 (M>=2.5)', {'knockdown': 0.7}, 5.0, TAKEOFF_REQ, A.CLMAX_TO),
                ('Supersonic CD0 x1.2', {'cd0_scale': 1.2}, 5.0, TAKEOFF_REQ, A.CLMAX_TO),
                ('Subsonic K1 0.14 (more LE suction / vortex lift)', {'k1_sub': 0.14}, 5.0, TAKEOFF_REQ, A.CLMAX_TO)]
    for nm, cfg, g, sto, clmax in variants:
        cs = curves(P2, True, cfg, turn_g=g, s_to=sto)
        if clmax != A.CLMAX_TO:
            cs[f'Takeoff ground roll {sto:.0f} m'] = np.array([m.tw_takeoff(w, sto, P2, clmax=clmax, cfg=cfg) for w in WS])
        ws_d, tw_d, active, _ = design_point(cs, ws_max)
        m3 = max(cs[k][np.argmin(abs(WS - ws_d))] for k in cs if k.startswith('M3.0'))
        rows.append([nm, f'{ws_d:.0f}', f'{tw_d:.3f}', active, f'{m3:.3f}'])
    out.append('## Design-point sensitivity (engine P2)\n\n'
               + md_table(['Variant', 'W/S (N/m2)', 'T/W', 'Active constraint', 'Worst M3 cruise T/W at that W/S'], rows) + '\n')

    # Mach-3 cruise: best altitude for L/D at given wing loading
    rows = []
    for ws_to in (3000, 3500, 4000, 5000, 6000):
        ws = 0.8 * ws_to
        ldm, clo = m.ld_max(3.0)
        q_opt = ws / clo
        p_opt = q_opt / (0.7 * 9.0)
        # invert pressure for altitude
        lo, hi = 10e3, 40e3
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if isa(mid)['p'] > p_opt:
                lo = mid
            else:
                hi = mid
        rows.append([ws_to, f'{q_opt / 1e3:.1f}', f'{mid / 1e3:.1f}', f'{ldm:.2f}'])
    out.append('## Altitude for (L/D)max at Mach 3 (beta = 0.8)\n\n'
               + md_table(['W_TO/S (N/m2)', 'q* (kPa)', 'altitude for CL* (km)', '(L/D)max'], rows) + '\n')

    out.append('## Reference aircraft on the same axes (W_TO/S, T_SL,max/W_TO)\n\n'
               + md_table(['Aircraft', 'W/S (N/m2)', 'T/W'], [[k, f'{v[0]:.0f}', f'{v[1]:.2f}'] for k, v in refs.items()]) + '\n')

    with open(os.path.join(OUT, 'design_points.json'), 'w') as f:
        json.dump(results, f, indent=2)
    with open(os.path.join(OUT, 'step2_constraints.md'), 'w') as f:
        f.write('\n'.join(out))
    print('\n'.join(out))


if __name__ == '__main__':
    main()
