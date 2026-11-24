"""Step 1: tables (a) ISA, (b) stagnation & adiabatic-wall temperature, (c) dynamic pressure,
(d) radiative-equilibrium skin temperature, heat-soak time constants and IR exitance.
Writes out/step1_atmos_thermal.md and out/step1_*.csv."""
import csv
import math
import os

import assumptions as A
import models as m
from atmosphere import isa, self_test

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
os.makedirs(OUT, exist_ok=True)

ALTS_KM = [0, 11, 15, 18, 20, 22, 24, 25]
MACHS = [2.0, 2.5, 2.83, 3.0, 3.2]


def md_table(header, rows):
    s = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    s += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return '\n'.join(s)


def main():
    out = ['# Step 1 output: atmosphere, aero-heating, dynamic pressure, skin temperature, IR\n']
    self_test()
    out.append('USSA-1976 self-test against tabulated values at 0/11/20/25 km geometric: PASSED (<0.1%).\n')

    # (a) ISA
    rows = []
    for z in ALTS_KM:
        s = isa(z * 1e3)
        rows.append([z, f"{s['H'] / 1e3:.3f}", f"{s['T']:.2f}", f"{s['T'] - 273.15:.2f}", f"{s['p']:.1f}",
                     f"{s['p'] / 101325:.5f}", f"{s['rho']:.5f}", f"{s['a']:.2f}", f"{s['mu'] * 1e5:.4f}"])
    hdr = ['z geom (km)', 'H geopot (km)', 'T (K)', 'T (degC)', 'p (Pa)', 'p/p0', 'rho (kg/m3)', 'a (m/s)', 'mu (1e-5 Pa s)']
    out.append('## (a) 1976 US Standard Atmosphere\n\n' + md_table(hdr, rows) + '\n')
    with open(os.path.join(OUT, 'step1_isa.csv'), 'w', newline='') as f:
        csv.writer(f).writerows([hdr] + rows)

    # (b) T0 and Taw, (c) q
    t0_rows, taw_rows, q_rows, v_rows = [], [], [], []
    for z in ALTS_KM:
        s = isa(z * 1e3)
        t0_rows.append([z] + [f"{m.t_stag(s['T'], M):.0f} K / {m.t_stag(s['T'], M) - 273.15:.0f} C" for M in MACHS])
        taw_rows.append([z] + [f"{m.t_aw(s['T'], M):.0f} K / {m.t_aw(s['T'], M) - 273.15:.0f} C" for M in MACHS])
        q_rows.append([z] + [f"{0.5 * 1.4 * s['p'] * M * M / 1e3:.1f}" for M in MACHS])
        v_rows.append([z] + [f"{M * s['a']:.0f}" for M in MACHS])
    mh = ['z (km)'] + [f'M{M:g}' for M in MACHS]
    out.append('## (b1) Stagnation temperature T0 = T(1 + 0.2 M^2)\n\n' + md_table(mh, t0_rows) + '\n')
    out.append(f'## (b2) Adiabatic-wall (recovery) temperature, turbulent r = {A.R_TURB}\n\n' + md_table(mh, taw_rows) + '\n')
    lam = [[z] + [f"{m.t_aw(isa(z * 1e3)['T'], M, A.R_LAM) - 273.15:.0f} C" for M in MACHS] for z in ALTS_KM]
    out.append(f'Laminar (r = {A.R_LAM}) recovery temperature for comparison:\n\n' + md_table(mh, lam) + '\n')
    out.append('## (c) Dynamic pressure q = 0.7 p M^2 (kPa)\n\n' + md_table(mh, q_rows) + '\n')
    out.append('True airspeed V = M a (m/s):\n\n' + md_table(mh, v_rows) + '\n')

    # (d) skin temperature and IR
    cases = [('M0.9 cruise, 11 km', 0.9, 11e3), ('M1.6 supercruise, 13 km', 1.6, 13e3),
             ('M2.83, 20 km (MiG-25 limit)', 2.83, 20e3), ('M3.0, 20 km', 3.0, 20e3),
             ('M3.0, 24 km', 3.0, 24e3), ('M3.2, 24 km', 3.2, 24e3)]
    rows, ir_rows = [], []
    base = None
    for name, M, h in cases:
        s = isa(h)
        Taw = m.t_aw(s['T'], M)
        for x in A.X_STATIONS:
            temps = []
            hc_ref = None
            for e in A.EMISSIVITIES:
                Tw, hc, Re, _ = m.wall_temp_radiative_eq(M, h, x, e)
                temps.append(Tw)
                if hc_ref is None:
                    hc_ref = (hc, Re)
            rows.append([name, f'{x:g}', f'{Taw - 273.15:.0f}', f'{hc_ref[1]:.2e}', f'{hc_ref[0]:.0f}']
                        + [f'{T - 273.15:.0f}' for T in temps] + [f'{Taw - temps[0]:.0f}'])
        # IR at x = 5 m (typical large-area skin), eps = 0.9 and 0.3
        for e in (0.9, 0.3):
            Tw, _, _, _ = m.wall_temp_radiative_eq(M, h, 5.0, e)
            tot = e * m.SIGMA * Tw ** 4
            mw = m.band_exitance(Tw, 3.0, 5.0, e)
            lw = m.band_exitance(Tw, 8.0, 12.0, e)
            if base is None:
                base = (tot, mw, lw)
            ir_rows.append([name, e, f'{Tw:.0f} K / {Tw - 273.15:.0f} C', f'{tot:.0f}', f'{mw:.1f}', f'{lw:.1f}',
                            f'{tot / base[0]:.3g}', f'{mw / base[1]:.3g}', f'{lw / base[2]:.3g}'])
    hdr = ['Case', 'x (m)', 'Taw (C)', 'Re_x*', 'h (W/m2K)'] + [f'Tw eps={e} (C)' for e in A.EMISSIVITIES] + ['Taw - Tw(eps 0.9) (K)']
    out.append('## (d1) Radiative-equilibrium skin temperature (turbulent flat plate, Eckert T*, radiation to ambient, '
               'adiabatic inner face)\n\n' + md_table(hdr, rows) + '\n')
    hdr = ['Case', 'eps', 'Skin T (x=5 m)', 'Total exitance eps*sigma*T^4 (W/m2)', 'MWIR 3-5 um (W/m2)',
           'LWIR 8-12 um (W/m2)', 'Total vs M0.9 eps0.9', 'MWIR ratio', 'LWIR ratio']
    out.append('## (d2) Skin IR exitance (grey body; ratios relative to M0.9/11 km, eps=0.9)\n\n' + md_table(hdr, ir_rows) + '\n')

    # heat soak: lumped time constant tau = rho c t / (h + 4 eps sigma Tw^3) at M3.0 / 20 km, x=5 m
    Tw, hc, _, Taw = m.wall_temp_radiative_eq(3.0, 20e3, 5.0, 0.9)
    skins = [('Aluminium alloy skin 2.0 mm', 2780, 875, 2.0e-3), ('Ti-6Al-4V skin 1.5 mm', 4430, 526, 1.5e-3),
             ('CFRP/polyimide skin 3.0 mm', 1600, 1000, 3.0e-3), ('Steel skin 1.2 mm', 7850, 460, 1.2e-3)]
    rows = []
    for nm, rho, c, t in skins:
        hr = 4 * 0.9 * m.SIGMA * Tw ** 3
        tau = rho * c * t / (hc + hr)
        T63 = 216.65 + 0.632 * (Tw - 216.65)
        rows.append([nm, f'{rho * c * t / 1e3:.2f}', f'{hc:.0f}+{hr:.0f}', f'{tau:.0f}', f'{3 * tau:.0f}'])
    out.append('## (d3) Thin-skin heat-soak time constant at M3.0 / 20 km, x = 5 m, eps = 0.9 '
               '(lumped; handbook-typical rho, c; skin only, no structure/fuel heat sink)\n\n'
               + md_table(['Skin', 'rho c t (kJ/m2K)', 'h_conv + h_rad (W/m2K)', 'tau (s)', '95% soak ~3 tau (s)'], rows) + '\n')
    out.append(f'Equilibrium skin at this point: {Tw - 273.15:.0f} C (Taw {Taw - 273.15:.0f} C).\n')

    path = os.path.join(OUT, 'step1_atmos_thermal.md')
    with open(path, 'w') as f:
        f.write('\n'.join(out))
    print('\n'.join(out))


if __name__ == '__main__':
    main()
