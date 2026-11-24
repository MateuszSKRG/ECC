# Step 2 output: drag polar, propulsion models, constraint analysis

## Drag polar CD = CD0(M) + K1(M) CL^2 (wing-referenced)

K1: 0.18 for M<=0.9, Raymer no-suction supersonic formula (AR=2.5, LE sweep 50.0 deg) for M>=1.2, linear blend between.

| M | CD0 | K1 | (L/D)max | CL* | Kuchemann 4(M+3)/M bound |
|---|---|---|---|---|---|
| 0.3 | 0.0140 | 0.180 | 9.96 | 0.279 | - |
| 0.6 | 0.0140 | 0.180 | 9.96 | 0.279 | - |
| 0.9 | 0.0150 | 0.180 | 9.62 | 0.289 | - |
| 1.0 | 0.0220 | 0.180 | 7.95 | 0.350 | - |
| 1.2 | 0.0280 | 0.180 | 7.04 | 0.394 | 14.0 |
| 1.5 | 0.0267 | 0.219 | 6.54 | 0.349 | 12.0 |
| 1.6 | 0.0262 | 0.239 | 6.32 | 0.331 | 11.5 |
| 1.8 | 0.0252 | 0.278 | 5.98 | 0.301 | 10.7 |
| 2.0 | 0.0243 | 0.315 | 5.72 | 0.278 | 10.0 |
| 2.5 | 0.0226 | 0.403 | 5.24 | 0.237 | 8.8 |
| 2.83 | 0.0217 | 0.460 | 5.00 | 0.217 | 8.2 |
| 3.0 | 0.0213 | 0.489 | 4.90 | 0.209 | 8.0 |
| 3.2 | 0.0209 | 0.523 | 4.78 | 0.200 | 7.8 |

## Installed thrust lapse alpha = T/T_SL,max (Mattingly fits)

P1 = Low-bypass mixed-flow AB turbofan (F119/F100-class, Mach ~2 class), TR=1.07; P2 = High-throttle-ratio AB turbojet / turbo-ramjet-like (Mach 3 capable), TR=2.1052. alpha=0 means the fit predicts no net thrust (beyond validity).

| M | h (km) | theta0 | delta0 | P1 dry | P1 max | P2 dry | P2 max | MIL-E-5007D recovery (ref.) |
|---|---|---|---|---|---|---|---|---|
| 0.0 | 0.0 | 1.000 | 1.000 | 0.600 | 1.000 | 0.800 | 1.000 | 1.000 |
| 0.9 | 9.0 | 0.926 | 0.514 | 0.308 | 0.514 | 0.349 | 0.477 | 1.000 |
| 0.9 | 11.0 | 0.874 | 0.379 | 0.227 | 0.379 | 0.257 | 0.357 | 1.000 |
| 1.5 | 11.0 | 1.091 | 0.822 | 0.458 | 0.767 | 0.529 | 0.699 | 0.971 |
| 1.7 | 13.0 | 1.186 | 0.808 | 0.304 | 0.530 | 0.511 | 0.657 | 0.954 |
| 2.0 | 15.0 | 1.353 | 0.935 | 0.115 | 0.250 | 0.579 | 0.704 | 0.925 |
| 2.5 | 18.0 | 1.692 | 1.276 | 0.000 | 0.000 | 0.762 | 0.809 | 0.870 |
| 2.5 | 20.0 | 1.692 | 0.932 | 0.000 | 0.000 | 0.557 | 0.591 | 0.870 |
| 2.83 | 20.0 | 1.956 | 1.550 | 0.000 | 0.000 | 0.906 | 0.845 | 0.830 |
| 3.0 | 20.0 | 2.105 | 2.005 | 0.000 | 0.000 | 1.159 | 0.993 | 0.809 |
| 3.0 | 22.0 | 2.124 | 1.467 | 0.000 | 0.000 | 0.828 | 0.699 | 0.809 |
| 3.0 | 24.0 | 2.143 | 1.077 | 0.000 | 0.000 | 0.592 | 0.493 | 0.809 |
| 3.2 | 24.0 | 2.333 | 1.450 | 0.000 | 0.000 | 0.605 | 0.398 | 0.783 |

## Installed TSFC (1/h) from Mattingly fits: LBPTF mil (0.9+0.30M)sqrt(theta), max (1.6+0.27M)sqrt(theta); TJ mil (1.1+0.30M)sqrt(theta), max (1.5+0.23M)sqrt(theta)

| M | h (km) | P1 LBPTF dry | P1 LBPTF max | P2 TJ dry | P2 TJ max |
|---|---|---|---|---|---|
| 0.0 | 0.0 | 0.90 | 1.60 | 1.10 | 1.50 |
| 0.9 | 11.0 | 1.01 | 1.60 | 1.19 | 1.48 |
| 1.5 | 13.0 | 1.17 | 1.74 | 1.34 | 1.60 |
| 2.5 | 20.0 | 1.43 | 1.97 | 1.60 | 1.80 |
| 3.0 | 21.0 | 1.56 | 2.09 | 1.74 | 1.90 |
| 3.2 | 24.0 | 1.63 | 2.16 | 1.80 | 1.96 |

Raymer Table 3.3-type cruise/loiter TSFC (for comparison): turbojet 0.9/0.8, low-bypass turbofan 0.8/0.7 (1/h).

Landing: s_L = 900 m, beta_L = 0.65, CLmax_L = 1.3, mu = 0.35 -> W_TO/S <= 4407 N/m2 (449 kg/m2).

## Constraint table, Mach 3 LO fighter, engine P2 (high-TR AB turbojet), all requirements

T_SL/W_TO required at W_TO/S (N/m2):

| Constraint | 2500 | 3000 | 3500 | 4000 | 4500 | 5000 | 6000 |
|---|---|---|---|---|---|---|---|
| M3.0 cruise 20 km (max AB) | 0.322 | 0.276 | 0.245 | 0.223 | 0.207 | 0.195 | 0.179 |
| M3.0 cruise 22 km (max AB) | 0.355 | 0.312 | 0.283 | 0.264 | 0.252 | 0.243 | 0.235 |
| M3.0 cruise 24 km (max AB) | 0.409 | 0.372 | 0.350 | 0.338 | 0.333 | 0.332 | 0.339 |
| Ps 50 m/s M2.5 18 km (accel margin) | 0.461 | 0.404 | 0.365 | 0.337 | 0.316 | 0.300 | 0.279 |
| Supercruise M1.7 13 km (dry) | 0.702 | 0.595 | 0.520 | 0.465 | 0.424 | 0.392 | 0.346 |
| Supercruise M1.8 15 km (dry) | 0.684 | 0.586 | 0.518 | 0.469 | 0.433 | 0.405 | 0.369 |
| 5 g sustained M0.9 9 km (max AB) | 1.085 | 1.221 | 1.368 | 1.521 | 1.679 | 1.840 | 2.167 |
| Ps 120 m/s M0.9 9 km (max AB) | 0.991 | 0.961 | 0.942 | 0.929 | 0.921 | 0.916 | 0.911 |
| Takeoff ground roll 800 m | 0.465 | 0.570 | 0.680 | 0.795 | 0.917 | 1.043 | 1.314 |
| ENVELOPE (max) | 1.085 | 1.221 | 1.368 | 1.521 | 1.679 | 1.840 | 2.167 |

**Design point P2:** W_TO/S = 2200 N/m2 (224 kg/m2, 45.9 lbf/ft2), T_SL/W_TO = 1.017; active constraint(s) at the minimum: Ps 120 m/s M0.9 9 km (max AB).

Plot: `out/constraint_diagram_P2.png`

## Constraint table, Same airframe with engine P1 (LBP AB turbofan), Mach 3 requirement removed

T_SL/W_TO required at W_TO/S (N/m2):

| Constraint | 2500 | 3000 | 3500 | 4000 | 4500 | 5000 | 6000 |
|---|---|---|---|---|---|---|---|
| Supercruise M1.7 13 km (dry) | 1.181 | 1.001 | 0.875 | 0.782 | 0.713 | 0.659 | 0.583 |
| Supercruise M1.8 15 km (dry) | 1.488 | 1.273 | 1.126 | 1.019 | 0.941 | 0.882 | 0.802 |
| 5 g sustained M0.9 9 km (max AB) | 1.006 | 1.132 | 1.268 | 1.410 | 1.557 | 1.706 | 2.009 |
| Ps 120 m/s M0.9 9 km (max AB) | 0.919 | 0.891 | 0.873 | 0.862 | 0.854 | 0.849 | 0.845 |
| Takeoff ground roll 800 m | 0.447 | 0.546 | 0.651 | 0.760 | 0.874 | 0.994 | 1.248 |
| ENVELOPE (max) | 1.488 | 1.273 | 1.268 | 1.410 | 1.557 | 1.706 | 2.009 |

**Design point P1:** W_TO/S = 3250 N/m2 (331 kg/m2, 67.9 lbf/ft2), T_SL/W_TO = 1.199; active constraint(s) at the minimum: 5 g sustained M0.9 9 km (max AB).

Plot: `out/constraint_diagram_P1.png`

## Mach 3 with the conventional fighter turbofan (P1)

| h (km) | P1 alpha_max at M3 | T_SL/W_TO required (W/S=4000) |
|---|---|---|
| 20.0 | 0.000 | inf |
| 22.0 | 0.000 | inf |
| 24.0 | 0.000 | inf |

- LBPTF with TR=1.07: alpha_max at M3/20 km = 0.000; at M2.5/18 km = 0.000
- LBPTF with TR=1.3: alpha_max at M3/20 km = 0.000; at M2.5/18 km = 0.242
- LBPTF with TR=1.5: alpha_max at M3/20 km = 0.000; at M2.5/18 km = 0.770
- LBPTF with TR=1.8: alpha_max at M3/20 km = 0.987; at M2.5/18 km = 1.276
- LBPTF with TR=2.1: alpha_max at M3/20 km = 1.987; at M2.5/18 km = 1.276

## Design-point sensitivity (engine P2)

| Variant | W/S (N/m2) | T/W | Active constraint | Worst M3 cruise T/W at that W/S |
|---|---|---|---|---|
| Baseline | 2200 | 1.017 | Ps 120 m/s M0.9 9 km (max AB) | 0.443 |
| Turn 4 g instead of 5 g | 3550 | 0.941 | 4 g sustained M0.9 9 km (max AB) | 0.349 |
| Turn 6 g | 2000 | 1.271 | 6 g sustained M0.9 9 km (max AB) | 0.473 |
| Takeoff roll 600 m | 2200 | 1.017 | Ps 120 m/s M0.9 9 km (max AB) | 0.443 |
| Takeoff roll 900 m | 2200 | 1.017 | Ps 120 m/s M0.9 9 km (max AB) | 0.443 |
| CLmax_TO 1.0 | 2200 | 1.017 | Ps 120 m/s M0.9 9 km (max AB) | 0.443 |
| Supersonic thrust knockdown 0.7 (M>=2.5) | 2200 | 1.017 | Ps 120 m/s M0.9 9 km (max AB) | 0.632 |
| Supersonic CD0 x1.2 | 2200 | 1.017 | Ps 120 m/s M0.9 9 km (max AB) | 0.516 |
| Subsonic K1 0.14 (more LE suction / vortex lift) | 2850 | 0.960 | Ps 120 m/s M0.9 9 km (max AB) | 0.381 |

## Altitude for (L/D)max at Mach 3 (beta = 0.8)

| W_TO/S (N/m2) | q* (kPa) | altitude for CL* (km) | (L/D)max |
|---|---|---|---|
| 3000 | 11.5 | 27.2 | 4.90 |
| 3500 | 13.4 | 26.2 | 4.90 |
| 4000 | 15.3 | 25.3 | 4.90 |
| 5000 | 19.2 | 23.8 | 4.90 |
| 6000 | 23.0 | 22.7 | 4.90 |

## Reference aircraft on the same axes (W_TO/S, T_SL,max/W_TO)

| Aircraft | W/S (N/m2) | T/W |
|---|---|---|
| MiG-25P | 5865 | 0.56 |
| MiG-31 | 6527 | 0.76 |
| SR-71A | 3936 | 0.44 |
| F-22A | 3642 | 1.10 |
