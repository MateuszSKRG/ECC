"""Step 4: (h) sanity check against MiG-25P, MiG-31, SR-71A, F-22A.
Ratios from public data, Raymer-fit residuals (-> K_we calibration), comparison with the sized
concepts, and a Breguet consistency check for the SR-71. Writes out/step4_sanity.md."""
import json
import math
import os

import assumptions as A
import models as m
from atmosphere import isa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')


def md_table(header, rows):
    s = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    s += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return '\n'.join(s)


def main():
    out = ['# Step 4 output: sanity check against real aircraft\n']
    rows, fit_rows = [], []
    for nm, d in A.REF_AIRCRAFT.items():
        W0, We, Wf, S = d['W0'], d['We'], d['Wf'], d['S']
        ar = d['span'] ** 2 / S
        tw = d['T_ab'] / (W0 * A.G0)
        ws = W0 * A.G0 / S
        rows.append([nm, f'{W0:,.0f}', f'{We:,.0f}', f'{Wf:,.0f}', f'{We / W0:.3f}', f'{Wf / W0:.3f}', f'{tw:.2f}',
                     f"{d['T_dry'] / (W0 * A.G0):.2f}", f'{ws:,.0f} ({W0 / S:.0f})', f'{ar:.2f}', d['Mmax']])
        fs = m.we_frac_simple(W0)
        fd = m.we_frac_detailed(W0, tw, ws, ar, d['Mmax'])
        fit_rows.append([nm, f'{We / W0:.3f}', f'{fs:.3f}', f'{We / W0 / fs:.2f}', f'{fd:.3f}', f'{We / W0 / fd:.2f}'])
    out.append('## Reference aircraft: published inputs and derived ratios\n\n'
               'W0 conventions: MiG-25P loaded 36,720 kg; MiG-31 normal 41,000 kg; SR-71A = empty + 80,000 lb fuel + 2 crew; '
               'F-22A = empty + ~18,000 lb internal fuel + ~1,100 kg pilot/internal AAMs.\n\n'
               + md_table(['Aircraft', 'W0 (kg)', 'We (kg)', 'Wf internal (kg)', 'We/W0', 'Wf/W0', 'T_AB/W0', 'T_dry/W0',
                           'W0/S N/m2 (kg/m2)', 'AR', 'Mmax'], rows) + '\n')
    for nm, d in A.REF_AIRCRAFT.items():
        out.append(f"- {nm}: {d['note']}")
    out.append('')
    out.append('## Raymer empty-weight fits vs actual (ratio > 1 = heavier than the historical fit)\n\n'
               + md_table(['Aircraft', 'We/W0 actual', 'Raymer T3.1 simple', 'actual/simple', 'Raymer T6.1 detailed',
                           'actual/detailed'], fit_rows) + '\n')

    # our concepts
    try:
        with open(os.path.join(OUT, 'sizing_summary.json')) as f:
            js = json.load(f)
        rows = []
        for k, v in js['baseline'].items():
            if 'K=1.0' not in k:
                continue
            rows.append([k.split(' | ')[0], f"{v['W0']:,.0f}", f"{v['We_frac']:.3f}", f"{v['Wf_frac']:.3f}",
                         f"{v['T_sl'] / (v['W0'] * A.G0):.2f}", f"{v['W0'] * A.G0 / v['S']:,.0f}", f"{v['S']:.0f}"])
        out.append('## Sized concepts (K_we = 1.0) on the same ratios\n\n'
                   + md_table(['Concept', 'W0 (kg)', 'We/W0', 'Wf/W0', 'T/W', 'W/S (N/m2)', 'S (m2)'], rows) + '\n')
    except FileNotFoundError:
        out.append('(run step3_sizing.py first for the concept comparison)\n')

    # SR-71 Breguet consistency
    s = isa(24e3)
    V = 3.2 * s['a']
    d = A.REF_AIRCRAFT['SR-71A']
    W_start = d['W0'] * 0.97 * m.raymer_accel_fraction(3.2)
    W_end = d['We'] + 200 + 0.08 * d['Wf']
    rows = []
    for LD in (5.5, 6.0, 6.6):
        for c in (1.7, 1.9):
            R = V / (c / 3600) * LD * math.log(W_start / W_end) / 1e3
            rows.append([LD, c, f'{W_start:,.0f}', f'{W_end:,.0f}', f'{R:,.0f}', f'{R / 1.852:,.0f}'])
    out.append('## Breguet consistency check, SR-71A at M3.2 / 24 km (cruise from end of Raymer climb to empty + crew + 8% fuel reserve)\n\n'
               + md_table(['L/D', 'c (1/h)', 'W start (kg)', 'W end (kg)', 'Cruise range (km)', '(nmi)'], rows)
               + '\n\n(L/D)max 6.6 for the A-12 family is a sourced value; c = 1.7-1.9/h and the published unrefuelled range '
               '(~2,900-3,200 nmi) are NOT verified this session.\n')

    # Inverse check: fly the reference aircraft's own weights through the mission model and solve for
    # the radius that its internal fuel supports (tests aero/propulsion/mission models, not We fits).
    import step3_sizing as s3

    def radius_for_fuel(prof_fn, W0, des, cfg, wf_avail):
        lo, hi = 0.0, 4000e3
        for _ in range(50):
            mid = 0.5 * (lo + hi)
            r = m.fly(prof_fn(mid), W0, des, cfg)
            if r['Wf'] > wf_avail:
                hi = mid
            else:
                lo = mid
        return 0.5 * (lo + hi), r

    def prof_m31(R):
        return [dict(type='fixed', f=A.F_TAKEOFF, label='TO'),
                dict(type='accel', M1=None, M2=2.35, label='climb/accel M2.35'),
                dict(type='cruise', R=R, M=2.35, h=(15e3, 21e3), throttle='max', label='M2.35 out'),
                dict(type='combat', t=120.0, M=1.5, h=12e3, label='combat'),
                dict(type='drop', label='drop'),
                dict(type='accel', M1=1.5, M2=2.35, label='re-accel'),
                dict(type='cruise', R=R, M=2.35, h=(15e3, 21e3), throttle='max', label='M2.35 back'),
                dict(type='fixed', f=A.F_DESCENT, label='descent'),
                dict(type='loiter', t=1200.0, reserve=True, label='reserve'),
                dict(type='fixed', f=A.F_LANDING, label='landing')]

    rows = []
    f22 = A.REF_AIRCRAFT['F-22A']
    des = dict(ws=f22['W0'] * A.G0 / f22['S'], tw=f22['T_ab'] / (f22['W0'] * A.G0), eng=A.ENGINES['P1'], eng_key='P1')
    for sup in (0.0, 185e3):
        R, r = radius_for_fuel(lambda x: s3.profile_B(sub=x, sup=sup), f22['W0'], des, dict(payload=1000.0), f22['Wf'])
        sc = [s['info'] for s in r['log'] if 'Supercruise' in s['label']]
        rows.append(['F-22A on Profile B (P1 engine model, TR 1.07)', f'{sup / 1e3:.0f} km supercruise each way',
                     f'{(R + sup) / 1e3:.0f} km total radius ({R / 1e3:.0f} subsonic)', (sc[0] if sc else '-')])
    m31 = A.REF_AIRCRAFT['MiG-31']
    eng31 = dict(kind='LBPTF', TR=round((216.65 / 288.15) * (1 + 0.2 * 2.83 ** 2), 3), knockdown_supersonic=1.0)
    des = dict(ws=m31['W0'] * A.G0 / m31['S'], tw=m31['T_ab'] / (m31['W0'] * A.G0), eng=eng31, eng_key='P1')
    pay31 = m31['W0'] - m31['We'] - m31['Wf'] - 200.0
    R, r = radius_for_fuel(prof_m31, m31['W0'], des, dict(payload=pay31), m31['Wf'])
    cr = [s['info'] for s in r['log'] if s['label'] == 'M2.35 out'][0]
    rows.append([f'MiG-31 on M2.35 out-and-back (LBPTF, TR {eng31["TR"]})', f'payload {pay31:,.0f} kg released',
                 f'{R / 1e3:.0f} km radius', cr])
    out.append('## Inverse check: radius supported by the reference aircraft\'s own internal fuel in this mission model\n\n'
               + md_table(['Aircraft / model', 'Mission variant', 'Model radius', 'Cruise detail'], rows)
               + '\n\nPublished radius claims to compare against were NOT verified this session (commonly quoted: F-22 ~760 km '
               'class on internal fuel; MiG-31 ~720 km at M2.35, listed as unverified in the sibling Russian-programs note).\n')

    with open(os.path.join(OUT, 'step4_sanity.md'), 'w') as f:
        f.write('\n'.join(out))
    print('\n'.join(out))


if __name__ == '__main__':
    main()
