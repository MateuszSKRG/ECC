"""Single registry of every input used by the entry analysis.

Every entry carries: value, unit, source/rationale, confidence.
Confidence codes:
  V  = verified this session from an open source (URL in the notes)
  T  = published textbook method/coefficient, recalled; NOT re-verified online this
       session (web search budget exhausted, fetch hosts blocked). Check against the book.
  A  = engineering assumption chosen by the analyst (rationale given)
  L  = low confidence; a sensitivity is run on it
Change a value here and re-run run_all.py; every table and plot is regenerated.
"""
import math

REG = {}


def p(key, value, unit, source, conf):
    REG[key] = dict(value=value, unit=unit, source=source, conf=conf)
    return value


G0 = 9.80665
LB_PER_KG = 2.20462262
PSF_PER_PA = 0.0208854342   # lbf/ft^2 per N/m^2

# ---------------------------------------------------------------- payload / crew
W_PAYLOAD = p('W_payload', 900.0, 'kg', 'Task brief: generic internal payload 700-1,000 kg (mid value); swept 700-1,000', 'A')
W_CREW = p('W_crew', 100.0, 'kg', 'One pilot + flight/pressure gear; ejection seat counted in empty weight (Raymer convention)', 'A')
PAYLOAD_DROP_FRACTION = p('payload_drop', 1.0, '-', 'All payload released at combat (missiles fired / stores dropped)', 'A')

# ---------------------------------------------------------------- geometry & aero
AR = p('AR', 2.5, '-', 'Between F-22 (13.6 m span, 78 m2 -> 2.36) and MiG-25 (~3.2); assumption', 'A')
SWEEP_LE_DEG = p('sweep_LE', 50.0, 'deg', 'Assumed; LE is supersonic above M~1.56 (Mach angle 19.5 deg at M3 -> >70.5 deg needed for subsonic LE)', 'L')
K1_SUB = p('K1_sub', 0.18, '-', 'Typical fighter induced-drag factor of Mattingly-style constraint examples (incl. partial LE-suction loss)', 'T/L')
K2 = p('K2', 0.0, '-', 'Symmetric polar assumed (Mattingly K2 term = 0)', 'A')
CDR = p('CDR', 0.0, '-', 'No external stores / additional drag: internal carriage (LO requirement)', 'A')
# Clean, internal-carriage fighter-class CD0 vs Mach referenced to wing area.
# Subsonic level and transonic peak shape follow Mattingly/Raymer-type fighter examples;
# M>2 values extrapolated so that (L/D)max at M3 ~ 4.9 (sibling aero note planning band 4-5.5).
CD0_TABLE = p('CD0_table', [(0.0, 0.0140), (0.8, 0.0140), (0.9, 0.0150), (1.0, 0.0220), (1.1, 0.0265),
                            (1.2, 0.0280), (1.4, 0.0272), (1.6, 0.0262), (1.8, 0.0252), (2.0, 0.0243),
                            (2.5, 0.0226), (3.0, 0.0213), (3.3, 0.0207)],
              '-', 'Representative fighter CD0(M); low confidence above M2 (no measured data found)', 'L')

# ---------------------------------------------------------------- field performance
CLMAX_TO = p('CLmax_TO', 1.2, '-', 'Thin (t/c~3-4%) moderately swept wing, LE/TE flaps, no slotted flaps', 'L')
K_TO = p('k_TO', 1.2, '-', 'V_TO = 1.2 V_stall (Mattingly/Raymer military practice)', 'T')
MU_ROLL = p('mu_roll', 0.03, '-', 'Rolling friction on dry concrete (textbook typical 0.02-0.03)', 'T')
T_ROT = p('t_rotation', 3.0, 's', 'Rotation time included in ground roll (Mattingly-style)', 'T')
CLMAX_L = p('CLmax_L', 1.3, '-', 'Landing CLmax, thin wing, no slotted flaps', 'L')
K_TD = p('k_TD', 1.15, '-', 'V_TD = 1.15 V_stall (military)', 'T')
T_FREE_ROLL = p('t_free_roll', 3.0, 's', 'Free-roll before braking', 'T')
MU_BRAKE = p('mu_brake', 0.35, '-', 'Effective deceleration coefficient: wheel brakes + drag chute', 'L')
BETA_LAND = p('beta_land', 0.65, '-', 'Landing weight / TOGW (empty + payload-dropped + reserves)', 'A')

# ---------------------------------------------------------------- propulsion
# Mattingly (Aircraft Engine Design 2nd ed., 2002) installed thrust-lapse & TSFC fits.
# Engine P2: TR chosen so the theta-break sits at Mach 3.0 in the isothermal stratosphere
#           (engine reaches T4max at Mach 3 cruise: J58-like concept).
TR_P2 = (216.65 / 288.15) * (1 + 0.2 * 3.0 ** 2)
ENGINES = {
    'P2': dict(kind='TJ', TR=p('TR_P2', round(TR_P2, 4), '-', 'theta0 at M3.0, 216.65 K: T4max reached at Mach 3 cruise (J58-like design intent)', 'A'),
               knockdown_supersonic=p('kd_P2', 1.0, '-', 'Extra installed-thrust knockdown for M>=2 (inlet/ejector uncertainty); 0.7 in sensitivity', 'L'),
               label='High-throttle-ratio AB turbojet / turbo-ramjet-like (Mach 3 capable)'),
    'P1': dict(kind='LBPTF', TR=p('TR_P1', 1.07, '-', 'Typical fighter turbofan throttle ratio (Mattingly AAF-type)', 'T/L'),
               knockdown_supersonic=1.0,
               label='Low-bypass mixed-flow AB turbofan (F119/F100-class, Mach ~2 class)'),
}
TSFC_SCALE = p('tsfc_scale', 1.0, '-', 'Multiplier on Mattingly TSFC fits (sensitivity 0.9-1.1)', 'L')

# ---------------------------------------------------------------- thermal / IR
PR = p('Pr', 0.71, '-', 'Air Prandtl number', 'T')
R_TURB = p('r_turb', 0.89, '-', 'Turbulent recovery factor ~Pr^(1/3) (brief: ~0.89)', 'V/T')
R_LAM = p('r_lam', 0.84, '-', 'Laminar recovery factor ~Pr^(1/2)', 'T')
CP_AIR = p('cp_air', 1005.0, 'J/(kg K)', 'Constant cp (slight underestimate of h at T*~450 K)', 'A')
X_STATIONS = p('x_stations', [1.0, 5.0], 'm', 'Distance from leading edge / nose for flat-plate heat transfer', 'A')
EMISSIVITIES = p('emissivities', [0.9, 0.5, 0.3], '-', '0.9 = high-emissivity black paint; 0.3-0.5 = notional low-e IR coatings', 'A')

# ---------------------------------------------------------------- mission rules
F_TAKEOFF = p('f_takeoff', 0.970, '-', 'Raymer Table 3.2 warm-up & takeoff', 'V')
F_CLIMB = p('f_climb', 0.985, '-', 'Raymer Table 3.2 climb (subsonic)', 'V')
F_LANDING = p('f_landing', 0.995, '-', 'Raymer Table 3.2 landing', 'V')
F_DESCENT = p('f_descent', 0.990, '-', 'Descent allowance (common textbook practice)', 'A')
RESERVE_LOITER_MIN = p('reserve_loiter', 20.0, 'min', 'MIL-C-5011A-style: 20 min loiter at sea level', 'T')
RESERVE_FRAC_MISSION = p('reserve_pct', 0.05, '-', '+5% of mission fuel (MIL-C-5011A-style)', 'T')
TRAPPED_FRAC = p('trapped', 0.01, '-', 'Trapped/unusable fuel, % of total', 'A')

# ---------------------------------------------------------------- empty weight
RAYMER_SIMPLE = p('Raymer_T3.1_jet_fighter', dict(A_lb=2.34, A_kg=2.11, C=-0.13, Kvs=1.00), '-',
                  'Raymer Table 3.1 jet fighter We/W0 = A W0^C Kvs (W0 in lb: A=2.34; kg: 2.11); Kvs=1.04 only for variable sweep', 'V')
RAYMER_DETAILED = p('Raymer_T6.1_jet_fighter', dict(a=-0.02, b=2.16, C1=-0.10, C2=0.20, C3=0.04, C4=-0.10, C5=0.08), '-',
                    'Raymer Table 6.1 jet fighter: We/W0 = a + b W0^C1 A^C2 (T/W)^C3 (W/S)^C4 Mmax^C5 (lb, lbf/ft2)', 'T')
MMAX = p('Mmax', 3.0, '-', 'Requirement', 'A')
# Raymer's detailed fit has (T/W)^0.04, i.e. almost no engine-size penalty. For design-point
# selection an explicit engine-mass delta is added:  dWe = (T/W - TW_REF) * W0 / TWR_ENG
TW_REF = p('TW_ref', 1.0, '-', 'T/W implicitly "contained" in the fighter regression (modern fighters ~1.0)', 'L')
TWR_ENG = p('TWR_eng', {'P2': 6.0, 'P1': 8.0}, '-',
            'Installed engine thrust/weight: P2 Mach-3 engine ~6 (J58 ~5.4-5.7, D-30F6 ~6.4, R-15B-300 ~4.2); P1 ~8 (F119-class ~9)', 'L')
K_WE_CASES = p('K_we_cases', {'historical fit (K=1.00)': 1.00, 'F-22-calibrated LO penalty (K=1.20)': 1.20}, '-',
               'K=1.0 lies on Raymer fit (MiG-25/31 sit on it); F-22 sits ~18-21% above it (see step4 sanity check)', 'A')

# ---------------------------------------------------------------- reference aircraft (step4)
# W0 = the takeoff weight used for ratios.  'src' lists URL keys explained in the notes.
REF_AIRCRAFT = {
    'MiG-25P': dict(We=20000, W0=36720, Wf=14100, S=61.4, span=14.0, T_ab=2 * 100.1e3, T_dry=2 * 73.5e3, Mmax=2.83,
                    note='We, W0 aerocorner; Wf flugzeuginfo (17,700 L); thrust flugzeuginfo; S, span commonly published (unverified)'),
    'MiG-31': dict(We=21820, W0=41000, Wf=16130, S=61.6, span=13.46, T_ab=2 * 151.9e3, T_dry=2 * 93.1e3, Mmax=2.83,
                   note='Wf Planehistoria; thrust Baidu/ArmyRecognition; MTOW 46,200 Fandom; We, normal W0 41,000, S, span unverified'),
    'SR-71A': dict(We=30617, W0=67104, Wf=36287, S=167.2, span=16.94, T_ab=2 * 144.6e3, T_dry=2 * 111.2e3, Mmax=3.2,
                   note='We 67,500 lb GlobalSecurity; fuel ~80,000 lb SR-71.org; W0 = We+fuel+2 crew (147,900 lb) because the NASA 140,000 lb gross implies partial fuel; S 1,800 ft2; thrust 32,500 lbf NASA; dry 25,000 lbf unverified'),
    'F-22A': dict(We=19700, W0=28965, Wf=8165, S=78.0, span=13.6, T_ab=2 * 155.7e3, T_dry=2 * 115.6e3, Mmax=2.25,
                  note='We af.mil; W0 = We + 18,000 lb internal fuel (unverified) + 1,100 kg pilot+AAM load (assumed); S 840 ft2 unverified; 35,000 lbf class af.mil'),
}


def dump_markdown():
    lines = ['| Key | Value | Unit | Source / rationale | Conf. |', '|---|---|---|---|---|']
    for k, v in REG.items():
        val = v['value']
        if isinstance(val, list) and val and isinstance(val[0], tuple):
            val = '; '.join(f'M{m:g}:{c:.4f}' for m, c in val)
        lines.append(f"| {k} | {val} | {v['unit']} | {v['source']} | {v['conf']} |")
    return '\n'.join(lines)


if __name__ == '__main__':
    print(dump_markdown())
