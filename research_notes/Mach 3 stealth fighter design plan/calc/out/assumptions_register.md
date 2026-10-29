# Assumption register (generated from assumptions.py)

| Key | Value | Unit | Source / rationale | Conf. |
|---|---|---|---|---|
| W_payload | 900.0 | kg | Task brief: generic internal payload 700-1,000 kg (mid value); swept 700-1,000 | A |
| W_crew | 100.0 | kg | One pilot + flight/pressure gear; ejection seat counted in empty weight (Raymer convention) | A |
| payload_drop | 1.0 | - | All payload released at combat (missiles fired / stores dropped) | A |
| AR | 2.5 | - | Between F-22 (13.6 m span, 78 m2 -> 2.36) and MiG-25 (~3.2); assumption | A |
| sweep_LE | 50.0 | deg | Assumed; LE is supersonic above M~1.56 (Mach angle 19.5 deg at M3 -> >70.5 deg needed for subsonic LE) | L |
| K1_sub | 0.18 | - | Typical fighter induced-drag factor of Mattingly-style constraint examples (incl. partial LE-suction loss) | T/L |
| K2 | 0.0 | - | Symmetric polar assumed (Mattingly K2 term = 0) | A |
| CDR | 0.0 | - | No external stores / additional drag: internal carriage (LO requirement) | A |
| CD0_table | M0:0.0140; M0.8:0.0140; M0.9:0.0150; M1:0.0220; M1.1:0.0265; M1.2:0.0280; M1.4:0.0272; M1.6:0.0262; M1.8:0.0252; M2:0.0243; M2.5:0.0226; M3:0.0213; M3.3:0.0207 | - | Representative fighter CD0(M); low confidence above M2 (no measured data found) | L |
| CLmax_TO | 1.2 | - | Thin (t/c~3-4%) moderately swept wing, LE/TE flaps, no slotted flaps | L |
| k_TO | 1.2 | - | V_TO = 1.2 V_stall (Mattingly/Raymer military practice) | T |
| mu_roll | 0.03 | - | Rolling friction on dry concrete (textbook typical 0.02-0.03) | T |
| t_rotation | 3.0 | s | Rotation time included in ground roll (Mattingly-style) | T |
| CLmax_L | 1.3 | - | Landing CLmax, thin wing, no slotted flaps | L |
| k_TD | 1.15 | - | V_TD = 1.15 V_stall (military) | T |
| t_free_roll | 3.0 | s | Free-roll before braking | T |
| mu_brake | 0.35 | - | Effective deceleration coefficient: wheel brakes + drag chute | L |
| beta_land | 0.65 | - | Landing weight / TOGW (empty + payload-dropped + reserves) | A |
| TR_P2 | 2.1052 | - | theta0 at M3.0, 216.65 K: T4max reached at Mach 3 cruise (J58-like design intent) | A |
| kd_P2 | 1.0 | - | Extra installed-thrust knockdown for M>=2 (inlet/ejector uncertainty); 0.7 in sensitivity | L |
| TR_P1 | 1.07 | - | Typical fighter turbofan throttle ratio (Mattingly AAF-type) | T/L |
| tsfc_scale | 1.0 | - | Multiplier on Mattingly TSFC fits (sensitivity 0.9-1.1) | L |
| Pr | 0.71 | - | Air Prandtl number | T |
| r_turb | 0.89 | - | Turbulent recovery factor ~Pr^(1/3) (brief: ~0.89) | V/T |
| r_lam | 0.84 | - | Laminar recovery factor ~Pr^(1/2) | T |
| cp_air | 1005.0 | J/(kg K) | Constant cp (slight underestimate of h at T*~450 K) | A |
| x_stations | [1.0, 5.0] | m | Distance from leading edge / nose for flat-plate heat transfer | A |
| emissivities | [0.9, 0.5, 0.3] | - | 0.9 = high-emissivity black paint; 0.3-0.5 = notional low-e IR coatings | A |
| f_takeoff | 0.97 | - | Raymer Table 3.2 warm-up & takeoff | V |
| f_climb | 0.985 | - | Raymer Table 3.2 climb (subsonic) | V |
| f_landing | 0.995 | - | Raymer Table 3.2 landing | V |
| f_descent | 0.99 | - | Descent allowance (common textbook practice) | A |
| reserve_loiter | 20.0 | min | MIL-C-5011A-style: 20 min loiter at sea level | T |
| reserve_pct | 0.05 | - | +5% of mission fuel (MIL-C-5011A-style) | T |
| trapped | 0.01 | - | Trapped/unusable fuel, % of total | A |
| Raymer_T3.1_jet_fighter | {'A_lb': 2.34, 'A_kg': 2.11, 'C': -0.13, 'Kvs': 1.0} | - | Raymer Table 3.1 jet fighter We/W0 = A W0^C Kvs (W0 in lb: A=2.34; kg: 2.11); Kvs=1.04 only for variable sweep | V |
| Raymer_T6.1_jet_fighter | {'a': -0.02, 'b': 2.16, 'C1': -0.1, 'C2': 0.2, 'C3': 0.04, 'C4': -0.1, 'C5': 0.08} | - | Raymer Table 6.1 jet fighter: We/W0 = a + b W0^C1 A^C2 (T/W)^C3 (W/S)^C4 Mmax^C5 (lb, lbf/ft2) | T |
| Mmax | 3.0 | - | Requirement | A |
| TW_ref | 1.0 | - | T/W implicitly "contained" in the fighter regression (modern fighters ~1.0) | L |
| TWR_eng | {'P2': 6.0, 'P1': 8.0} | - | Installed engine thrust/weight: P2 Mach-3 engine ~6 (J58 ~5.4-5.7, D-30F6 ~6.4, R-15B-300 ~4.2); P1 ~8 (F119-class ~9) | L |
| K_we_cases | {'historical fit (K=1.00)': 1.0, 'F-22-calibrated LO penalty (K=1.20)': 1.2} | - | K=1.0 lies on Raymer fit (MiG-25/31 sit on it); F-22 sits ~18-21% above it (see step4 sanity check) | A |
