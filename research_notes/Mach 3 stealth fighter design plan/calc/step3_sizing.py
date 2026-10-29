"""Step 3: (f) takeoff-gross-weight sizing for the notional mission profiles, design-point
selection by minimum TOGW along the constraint envelope, (g) fuel fractions, wing area,
installed thrust, engine class, and sensitivities.
Writes out/step3_sizing.md, out/sizing_*.png, out/sizing_summary.json."""
import json
import math
import os

import numpy as np

import assumptions as A
import models as m
import step2_constraints as s2

OUT = s2.OUT
G0 = A.G0

PATH_M3 = [(0.3, 0.0), (0.9, 1e3), (0.9, 10e3), (1.5, 11e3), (2.2, 15e3), (3.0, 20e3), (3.0, 22e3)]
PATH_15_25 = [(1.5, 12e3), (2.0, 15e3), (2.5, 19e3)]
PATH_09_30 = [(0.9, 11e3), (1.5, 11e3), (2.2, 15e3), (3.0, 20e3), (3.0, 22e3)]
PATH_09_16 = [(0.9, 11e3), (1.6, 13e3)]
PATH_09_16b = [(0.9, 9e3), (1.6, 13e3)]


def profile_A(radius=500e3, combat=(1.5, 12e3), m3_ceiling=25e3):
    M_c, h_c = combat
    return [
        dict(type='fixed', f=A.F_TAKEOFF, label='1 Warm-up, taxi, takeoff'),
        dict(type='accel', M1=None, M2=3.0, path=PATH_M3, label='2 Climb & accelerate to M3.0'),
        dict(type='cruise', R=radius, M=3.0, h=(20e3, m3_ceiling), throttle='auto', label=f'3 Mach 3.0 cruise-out {radius / 1e3:.0f} km'),
        dict(type='combat', t=120.0, M=M_c, h=h_c, label=f'4 Combat 2 min max AB (M{M_c:g}, {h_c / 1e3:.0f} km)'),
        dict(type='drop', label='5 Payload released'),
        dict(type='accel', M1=M_c, M2=2.5, path=[(M_c, h_c)] + PATH_15_25[1:], label='6 Re-accelerate to M2.5'),
        dict(type='cruise', R=radius, M=2.5, h=(17e3, m3_ceiling), throttle='auto', label=f'7 Return at M2.5, {radius / 1e3:.0f} km'),
        dict(type='fixed', f=A.F_DESCENT, label='8 Descent'),
        dict(type='loiter', t=A.RESERVE_LOITER_MIN * 60, reserve=True, label='9 Reserve 20 min loiter, SL'),
        dict(type='fixed', f=A.F_LANDING, label='10 Landing'),
    ]


def profile_A_dash(radius=500e3, dash=100e3):
    return [
        dict(type='fixed', f=A.F_TAKEOFF, label='1 Warm-up, taxi, takeoff'),
        dict(type='fixed', f=A.F_CLIMB, label='2 Climb to subsonic cruise'),
        dict(type='cruise', R=radius - dash, M=0.9, h=(9e3, 15e3), throttle='auto', label=f'3 M0.9 cruise-out {(radius - dash) / 1e3:.0f} km'),
        dict(type='accel', M1=0.9, M2=3.0, path=PATH_09_30, label='4 Accelerate to M3.0'),
        dict(type='cruise', R=dash, M=3.0, h=(20e3, 25e3), throttle='auto', label=f'5 Mach 3.0 dash {dash / 1e3:.0f} km'),
        dict(type='combat', t=120.0, M=1.5, h=12e3, label='6 Combat 2 min max AB (M1.5, 12 km)'),
        dict(type='drop', label='7 Payload released'),
        dict(type='cruise', R=radius, M=0.9, h=(9e3, 15e3), throttle='auto', label=f'8 M0.9 return {radius / 1e3:.0f} km'),
        dict(type='fixed', f=A.F_DESCENT, label='9 Descent'),
        dict(type='loiter', t=A.RESERVE_LOITER_MIN * 60, reserve=True, label='10 Reserve 20 min loiter, SL'),
        dict(type='fixed', f=A.F_LANDING, label='11 Landing'),
    ]


def profile_B(sub=600e3, sup=200e3):
    return [
        dict(type='fixed', f=A.F_TAKEOFF, label='1 Warm-up, taxi, takeoff'),
        dict(type='fixed', f=A.F_CLIMB, label='2 Climb to subsonic cruise'),
        dict(type='cruise', R=sub, M=0.9, h=(9e3, 15e3), throttle='auto', label=f'3 M0.9 cruise-out {sub / 1e3:.0f} km'),
        dict(type='accel', M1=0.9, M2=1.6, path=PATH_09_16, label='4 Accelerate to M1.6'),
        dict(type='cruise', R=sup, M=1.6, h=(11e3, 18e3), throttle='auto', label=f'5 Supercruise M1.6 {sup / 1e3:.0f} km'),
        dict(type='combat', t=180.0, M=0.9, h=9e3, label='6 Combat 3 min max AB (M0.9, 9 km)'),
        dict(type='drop', label='7 Payload released'),
        dict(type='accel', M1=0.9, M2=1.6, path=PATH_09_16b, label='8 Re-accelerate to M1.6'),
        dict(type='cruise', R=sup, M=1.6, h=(11e3, 18e3), throttle='auto', label=f'9 Supercruise M1.6 {sup / 1e3:.0f} km'),
        dict(type='cruise', R=sub, M=0.9, h=(9e3, 15e3), throttle='auto', label=f'10 M0.9 return {sub / 1e3:.0f} km'),
        dict(type='fixed', f=A.F_DESCENT, label='11 Descent'),
        dict(type='loiter', t=A.RESERVE_LOITER_MIN * 60, reserve=True, label='12 Reserve 20 min loiter, SL'),
        dict(type='fixed', f=A.F_LANDING, label='13 Landing'),
    ]


def md_table(header, rows):
    return s2.md_table(header, rows)


def envelope(eng, include_m3, turn_g=5.0, cfg=None):
    cs = s2.curves(eng, include_m3, cfg, turn_g=turn_g)
    return np.max(np.vstack(list(cs.values())), axis=0)


def fmt_res(r):
    if not r.get('closed'):
        return 'NC'
    return f"{r['W0'] / 1e3:.1f}" + ('' if r['practical'] else '*')


def select_design(eng, eng_key, include_m3, profiles, cfg, ws_max, turn_g=5.0):
    env = envelope(eng, include_m3, turn_g, cfg)
    rows, best = [], None
    for ws in np.arange(2000.0, ws_max + 1, 100.0):
        tw = float(np.interp(ws, s2.WS, env))
        des = dict(ws=ws, tw=tw, eng=eng, eng_key=eng_key)
        res = [m.size(p, des, cfg) for p in profiles]
        w = [r['W0'] if r.get('closed') else float('inf') for r in res]
        rows.append([f'{ws:.0f}', f'{tw:.3f}'] + [fmt_res(r) for r in res])
        if best is None or max(w) < best[2]:
            best = (ws, tw, max(w))
    return best, rows


def summary_row(name, r, des):
    if not r.get('closed'):
        return [name, r.get('reason', 'NC')] + ['-'] * 10
    T = r['T_sl']
    return [name, f"{r['W0']:.0f}", f"{r['We']:.0f}", f"{r['Wf']:.0f}", f"{r['We_frac']:.3f}", f"{r['Wf_frac']:.3f}",
            f"{r['S']:.1f}", f"{des['ws']:.0f}", f"{des['tw']:.3f}", f"{T / 1e3:.0f}", f"{T / 2e3:.0f}",
            f"{(r['burned_mission'] + r['burned_reserve']) / r['W0']:.3f}"]


SUMMARY_HDR = ['Case', 'W0 (kg)', 'We (kg)', 'Wf (kg)', 'We/W0', 'Wf/W0', 'S (m2)', 'W/S (N/m2)', 'T/W', 'T_SL total (kN)',
               'per engine, twin (kN)', 'fuel burned/W0']


def seg_table(r):
    rows = []
    for s in r['log']:
        rows.append([s['label'], f"{s['W_start']:.0f}", f"{s['W_end']:.0f}", f"{s['W_end'] / s['W_start']:.4f}",
                     f"{s['fuel']:.0f}", s['info']])
    return md_table(['Segment', 'W start (kg)', 'W end (kg)', 'Wi/Wi-1', 'fuel (kg)', 'details'], rows)


def main():
    out = ['# Step 3 output: mission sizing, design-point selection, sensitivities\n']
    P1, P2 = A.ENGINES['P1'], A.ENGINES['P2']
    ws_max = m.ws_landing_max(s2.LANDING_REQ)
    base_cfg = dict(K_we=1.0, we_method='detailed', climb_method='raymer')

    # ---- design point selection (P2, K=1.0): minimise max(W0_A, W0_B) along the envelope
    profs = [profile_A(), profile_B()]
    best, rows = select_design(P2, 'P2', True, profs, base_cfg, ws_max)
    out.append('## Design-point selection along the P2 constraint envelope (K_we = 1.0, detailed Raymer We)\n\n'
               'T/W = constraint envelope at each W/S; W0 in tonnes for Profile A (interceptor) and B (strike/air superiority). '
               '`*` = above 60 t practical limit; NC = no closure.\n\n'
               + md_table(['W_TO/S (N/m2)', 'T_SL/W_TO', 'W0 A (t)', 'W0 B (t)'], rows) + '\n')
    ws_d, tw_d, _ = best
    desP2 = dict(ws=ws_d, tw=tw_d, eng=P2, eng_key='P2')
    out.append(f'**Selected P2 design point:** W_TO/S = {ws_d:.0f} N/m2 ({ws_d / G0:.0f} kg/m2), T_SL/W_TO = {tw_d:.3f} '
               f'(minimum of max(W0_A, W0_B)).\n')

    bestP1, rowsP1 = select_design(P1, 'P1', False, [profile_B()], dict(base_cfg, Mmax=2.0), ws_max)
    desP1 = dict(ws=bestP1[0], tw=bestP1[1], eng=P1, eng_key='P1')
    out.append(f'**P1 (no Mach 3) design point for Profile B:** W_TO/S = {desP1["ws"]:.0f} N/m2, T_SL/W_TO = {desP1["tw"]:.3f}.\n')

    # ---- baseline sizing
    summary = []
    results = {}
    cases = [('A interceptor, P2', profile_A(), desP2, {}),
             ('A-dash (M3 dash 100 km only), P2', profile_A_dash(), desP2, {}),
             ('B strike/air-sup, P2 (Mach 3 capable)', profile_B(), desP2, {}),
             ('B strike/air-sup, P1 (Mach 2 class, no M3)', profile_B(), desP1, {'Mmax': 2.0})]
    for kname, K in A.K_WE_CASES.items():
        for name, prof, des, extra in cases:
            cfg = dict(base_cfg, K_we=K, **extra)
            r = m.size(prof, des, cfg)
            results[(name, K)] = r
            summary.append(summary_row(f'{name}; {kname}', r, des))
    out.append('## (f)/(g) Sizing results\n\n' + md_table(SUMMARY_HDR, summary) + '\n')

    for name, prof, des, extra in cases:
        r = results[(name, 1.0)]
        if r.get('closed'):
            out.append(f'### Segment log: {name}, K_we = 1.0 (W0 = {r["W0"]:.0f} kg)\n\n' + seg_table(r) + '\n')
            out.append(f'Mission fuel burned {r["burned_mission"]:.0f} kg, reserve loiter {r["burned_reserve"]:.0f} kg, '
                       f'+5% mission fuel reserve, +1% trapped -> Wf = {r["Wf"]:.0f} kg.\n')

    # ---- climb cross-check
    rows = []
    for nm, cfgc in [('Raymer fit 0.991-0.007M-0.01M^2', dict(base_cfg)), ('Energy method (max AB, this airframe)', dict(base_cfg, climb_method='energy'))]:
        r = m.size(profile_A(), desP2, cfgc)
        climb = [s for s in r['log'] if s['label'].startswith('2 ')][0]
        rows.append([nm, f"{climb['W_end'] / climb['W_start']:.4f}", climb['info'], fmt_res(r)])
    out.append('## Climb/acceleration to Mach 3: Raymer fit vs energy-state integration (Profile A, K=1.0)\n\n'
               + md_table(['Method', 'Wi/Wi-1', 'details', 'W0 A (t)'], rows) + '\n')

    rows = []
    for name, prof, des, extra in cases:
        ra = m.size(prof, des, dict(base_cfg, **extra))
        re_ = m.size(prof, des, dict(base_cfg, climb_method='energy', **extra))
        rows.append([name, fmt_res(ra), fmt_res(re_), f"{ra['Wf_frac']:.3f}" if ra.get('closed') else '-',
                     f"{re_['Wf_frac']:.3f}" if re_.get('closed') else '-'])
    out.append('W0 (t) for all cases, K_we = 1.0, Raymer-fit vs energy-method climb/acceleration segments:\n\n'
               + md_table(['Case', 'W0 Raymer', 'W0 energy', 'Wf/W0 Raymer', 'Wf/W0 energy'], rows) + '\n')

    # ---- engine class
    rows = []
    for name, prof, des, extra in cases:
        for K in A.K_WE_CASES.values():
            r = results[(name, K)]
            if r.get('closed'):
                T = r['T_sl'] / 1e3
                rows.append([name, K, f'{T:.0f}', f'{T / 2:.0f}', f'{T:.0f}'])
    out.append('## Required installed SL static max (AB) thrust and engine class\n\n'
               + md_table(['Case', 'K_we', 'Total (kN)', 'Twin: per engine (kN)', 'Single: one engine (kN)'], rows)
               + '\n\nReference AB classes (public): R-15B-300 ~100 kN; J58 145-151 kN; D-30F6 ~152 kN; F119 ~156 kN (35,000 lbf class). '
               'Single-engine values far above every listed fighter engine imply a twin-engine layout.\n')

    # ---- sensitivity 1: Mach 3 radius x K_we (Profile A)
    radii = [100e3, 200e3, 300e3, 400e3, 500e3, 600e3, 700e3, 800e3, 1000e3]
    Ks = [1.0, 1.1, 1.2, 1.3]
    grid = {}
    rows = []
    for R in radii:
        row = [f'{R / 1e3:.0f}']
        for K in Ks:
            r = m.size(profile_A(R), desP2, dict(base_cfg, K_we=K))
            grid[(R, K)] = r['W0'] if r.get('closed') else float('nan')
            row.append(fmt_res(r))
        rows.append(row)
    out.append('## Sensitivity S1: Profile A W0 (t) vs Mach 3 radius (M3 out, M2.5 back) and empty-weight factor K_we\n\n'
               + md_table(['Radius (km)'] + [f'K={K}' for K in Ks], rows) + '\n')

    # ---- sensitivity 2: K sweep for all profiles
    Kgrid = [0.9, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35]
    rows = []
    kcurves = {}
    for name, prof, des, extra in cases:
        row = [name]
        vals = []
        for K in Kgrid:
            r = m.size(prof, des, dict(base_cfg, K_we=K, **extra))
            row.append(fmt_res(r))
            vals.append(r['W0'] / 1e3 if r.get('closed') else float('nan'))
        kcurves[name] = vals
        rows.append(row)
    out.append('## Sensitivity S2: W0 (t) vs empty-weight factor K_we (LO / hot-structure penalty)\n\n'
               + md_table(['Case'] + [f'K={K}' for K in Kgrid], rows) + '\n')

    # ---- sensitivity 3: one-at-a-time, Profile A baseline (K=1.0)
    rA = m.size(profile_A(), desP2, base_cfg)
    W0b = rA['W0']
    oat = [('K_we 1.0 -> 1.2 (F-22-like LO penalty)', profile_A(), desP2, dict(base_cfg, K_we=1.2)),
           ('Mach 3 radius 500 -> 300 km', profile_A(300e3), desP2, base_cfg),
           ('Mach 3 radius 500 -> 700 km', profile_A(700e3), desP2, base_cfg),
           ('Payload 900 -> 700 kg', profile_A(), desP2, dict(base_cfg, payload=700.0)),
           ('Payload 900 -> 1,000 kg', profile_A(), desP2, dict(base_cfg, payload=1000.0)),
           ('TSFC x0.9 (better cycle)', profile_A(), desP2, dict(base_cfg, tsfc_scale=0.9)),
           ('TSFC x1.1', profile_A(), desP2, dict(base_cfg, tsfc_scale=1.1)),
           ('Supersonic CD0 x0.85 (L/D_M3 ~5.3)', profile_A(), desP2, dict(base_cfg, cd0_scale=0.85)),
           ('Supersonic CD0 x1.2 (L/D_M3 ~4.5)', profile_A(), desP2, dict(base_cfg, cd0_scale=1.2)),
           ('Supersonic thrust knockdown 0.7', profile_A(), desP2, dict(base_cfg, knockdown=0.7)),
           ('Energy-method climb instead of Raymer fit', profile_A(), desP2, dict(base_cfg, climb_method='energy')),
           ('Simple Raymer We (Table 3.1) instead of detailed', profile_A(), desP2, dict(base_cfg, we_method='simple')),
           ('No explicit engine-mass correction', profile_A(), desP2, dict(base_cfg, engine_correction=False)),
           ('Engine T/W 6 -> 8 (lighter Mach 3 engine)', profile_A(), desP2, dict(base_cfg, twr_eng=8.0)),
           ('Engine T/W 6 -> 5 (heavier)', profile_A(), desP2, dict(base_cfg, twr_eng=5.0)),
           ('Combat at M0.9/9 km instead of M1.5/12 km', profile_A(combat=(0.9, 9e3)), desP2, base_cfg),
           ('Mach 3 dash 100 km only (A-dash)', profile_A_dash(), desP2, base_cfg)]
    # re-selected design points (constraint changes move the envelope)
    def reselect(turn_g=5.0, cfg=None, prof_kw=None):
        cfg = cfg or {}
        envr = envelope(P2, True, turn_g=turn_g, cfg=cfg)
        bestr = None
        for ws in np.arange(2000.0, ws_max + 1, 100.0):
            tw = float(np.interp(ws, s2.WS, envr))
            d = dict(ws=ws, tw=tw, eng=P2, eng_key='P2')
            ra = m.size(profile_A(**(prof_kw or {})), d, dict(base_cfg, **cfg))
            rb = m.size(profile_B(), d, dict(base_cfg, **cfg))
            w = max(ra['W0'] if ra.get('closed') else 1e9, rb['W0'] if rb.get('closed') else 1e9)
            if bestr is None or w < bestr[2]:
                bestr = (ws, tw, w)
        return dict(ws=bestr[0], tw=bestr[1], eng=P2, eng_key='P2')
    des4 = reselect(4.0)
    oat.append((f'Sustained turn 5 g -> 4 g (re-selected W/S {des4["ws"]:.0f}, T/W {des4["tw"]:.2f})', profile_A(), des4, base_cfg))
    desk = reselect(5.0, dict(k1_sub=0.14))
    oat.append((f'Subsonic K1 0.18 -> 0.14 (re-selected W/S {desk["ws"]:.0f}, T/W {desk["tw"]:.2f})', profile_A(), desk,
                dict(base_cfg, k1_sub=0.14)))
    desc = reselect(5.0, {}, dict(m3_ceiling=28e3))
    oat.append((f'Mach 3/2.5 cruise ceiling 25 -> 28 km (re-selected W/S {desc["ws"]:.0f}, T/W {desc["tw"]:.2f})',
                profile_A(m3_ceiling=28e3), desc, base_cfg))
    des4c = reselect(4.0, {}, dict(m3_ceiling=28e3))
    oat.append((f'4 g turn AND 28 km ceiling (re-selected W/S {des4c["ws"]:.0f}, T/W {des4c["tw"]:.2f})',
                profile_A(m3_ceiling=28e3), des4c, base_cfg))
    alt_designs = dict(turn4g=des4, k1_014=desk, ceiling28=desc, turn4g_ceiling28=des4c)
    rows = []
    tornado = []
    for nm, prof, des, cfg in oat:
        r = m.size(prof, des, cfg)
        if r.get('closed'):
            d = (r['W0'] - W0b) / W0b * 100
            rows.append([nm, f"{r['W0']:.0f}", f'{d:+.1f}%', f"{r['Wf_frac']:.3f}", f"{r['We_frac']:.3f}"])
            tornado.append((nm, d))
        else:
            rows.append([nm, r.get('reason'), '-', '-', '-'])
    out.append(f'## Sensitivity S3: one-at-a-time, Profile A baseline W0 = {W0b:.0f} kg (K_we = 1.0)\n\n'
               + md_table(['Change', 'W0 (kg)', 'dW0', 'Wf/W0', 'We/W0'], rows) + '\n')

    # ---- S4: relaxed-requirement design points x K_we for all P2 missions
    rows = []
    for dname, dd, pkw in [('Baseline 5 g, 25 km ceiling', desP2, {}), ('4 g turn', des4, {}),
                           ('4 g turn + 28 km ceiling', des4c, dict(m3_ceiling=28e3))]:
        for K in (1.0, 1.1, 1.2):
            cfgk = dict(base_cfg, K_we=K)
            ra = m.size(profile_A(**pkw), dd, cfgk)
            rd = m.size(profile_A_dash(), dd, cfgk)
            rb = m.size(profile_B(), dd, cfgk)
            rows.append([dname, f"{dd['ws']:.0f} / {dd['tw']:.2f}", K, fmt_res(ra), fmt_res(rd), fmt_res(rb),
                         f"{ra['S']:.0f}" if ra.get('closed') else '-',
                         f"{ra['T_sl'] / 2e3:.0f}" if ra.get('closed') else '-'])
    out.append('## Sensitivity S4: W0 (t) for relaxed-requirement design points and K_we (engine P2)\n\n'
               + md_table(['Design point', 'W/S / T/W', 'K_we', 'A', 'A-dash', 'B', 'S for A (m2)', 'A per-engine twin (kN)'], rows)
               + '\n')

    # ---- payload effect (growth factor)
    r7 = m.size(profile_A(), desP2, dict(base_cfg, payload=700.0))
    r10 = m.size(profile_A(), desP2, dict(base_cfg, payload=1000.0))
    gf = (r10['W0'] - r7['W0']) / 300.0
    out.append(f'Weight growth factor dW0/dW_payload (Profile A, K=1.0) = {gf:.1f} kg per kg of payload.\n')

    # ---- plots
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 5))
        for K in Ks:
            ax.plot([R / 1e3 for R in radii], [grid[(R, K)] / 1e3 for R in radii], marker='o', label=f'K_we = {K}')
        for nm, d in A.REF_AIRCRAFT.items():
            ax.axhline(d['W0'] / 1e3, color='0.75', lw=0.8, ls='--')
            ax.text(1005, d['W0'] / 1e3, nm, fontsize=7, color='0.4', va='center')
        ax.set_ylim(0, 100)
        ax.set_xlabel('Mach 3 out / Mach 2.5 back radius (km)')
        ax.set_ylabel('Takeoff gross weight W0 (t)')
        ax.set_title(f'Profile A sizing, P2 engine, W/S={ws_d:.0f} N/m2, T/W={tw_d:.2f}', fontsize=10)
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(os.path.join(OUT, 'sizing_radius_vs_W0.png'), dpi=130)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(8, 5))
        for name, vals in kcurves.items():
            ax.plot(Kgrid, vals, marker='o', label=name)
        ax.set_ylim(0, 100)
        ax.set_xlabel('Empty-weight factor K_we (x Raymer detailed fit)')
        ax.set_ylabel('W0 (t)')
        ax.grid(alpha=0.3)
        ax.legend(fontsize=7)
        ax.set_title('Takeoff weight vs empty-weight penalty (LO + hot structure)', fontsize=10)
        fig.tight_layout()
        fig.savefig(os.path.join(OUT, 'sizing_Kwe_vs_W0.png'), dpi=130)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(8, 5))
        tornado.sort(key=lambda t: abs(t[1]))
        ax.barh([t[0] for t in tornado], [t[1] for t in tornado], color=['#c0504d' if t[1] > 0 else '#4f81bd' for t in tornado])
        ax.axvline(0, color='k', lw=0.8)
        ax.set_xlabel('Change in Profile A W0 (%)')
        ax.tick_params(axis='y', labelsize=7)
        ax.set_title(f'One-at-a-time sensitivity, baseline W0 = {W0b / 1e3:.1f} t', fontsize=10)
        fig.tight_layout()
        fig.savefig(os.path.join(OUT, 'sizing_tornado_A.png'), dpi=130)
        plt.close(fig)

        # final constraint diagram with selected point
        cs = s2.curves(P2, True)
        for s_to in (600.0, 900.0):
            cs[f'Takeoff ground roll {s_to:.0f} m'] = np.array([m.tw_takeoff(w, s_to, P2) for w in s2.WS])
        s2.plot(cs, ws_max, (ws_d, tw_d), 'Mach 3 LO fighter, engine P2: selected design point (min TOGW on envelope)',
                'constraint_diagram_P2_selected.png', s2.ref_points())
        out.append('Plots: `out/sizing_radius_vs_W0.png`, `out/sizing_Kwe_vs_W0.png`, `out/sizing_tornado_A.png`, '
                   '`out/constraint_diagram_P2_selected.png`\n')
    except ImportError:
        out.append('(matplotlib not available: plots skipped; tables above are complete)\n')

    js = dict(design_P2=desP2 | {'eng': 'P2'}, design_P1=desP1 | {'eng': 'P1'},
              alt_designs={k: v | {'eng': 'P2'} for k, v in alt_designs.items()},
              baseline={f'{k[0]} | K={k[1]}': {kk: v[kk] for kk in ('W0', 'We', 'Wf', 'S', 'T_sl', 'We_frac', 'Wf_frac')}
                        for k, v in results.items() if v.get('closed')})
    with open(os.path.join(OUT, 'sizing_summary.json'), 'w') as f:
        json.dump(js, f, indent=2)
    with open(os.path.join(OUT, 'step3_sizing.md'), 'w') as f:
        f.write('\n'.join(out))
    print('\n'.join(out))


if __name__ == '__main__':
    main()
