# Step 3 output: mission sizing, design-point selection, sensitivities

## Design-point selection along the P2 constraint envelope (K_we = 1.0, detailed Raymer We)

T/W = constraint envelope at each W/S; W0 in tonnes for Profile A (interceptor) and B (strike/air superiority). `*` = above 60 t practical limit; NC = no closure.

| W_TO/S (N/m2) | T_SL/W_TO | W0 A (t) | W0 B (t) |
|---|---|---|---|
| 2000 | 1.039 | 54.3 | 43.1 |
| 2100 | 1.027 | 48.6 | 38.8 |
| 2200 | 1.017 | 44.1 | 35.4 |
| 2300 | 1.035 | 43.5 | 35.0 |
| 2400 | 1.059 | 43.9 | 35.3 |
| 2500 | 1.085 | 44.7 | 35.9 |
| 2600 | 1.111 | 45.7 | 36.7 |
| 2700 | 1.138 | 47.0 | 37.8 |
| 2800 | 1.165 | 48.5 | 39.0 |
| 2900 | 1.193 | 50.4 | 40.5 |
| 3000 | 1.221 | 52.6 | 42.2 |
| 3100 | 1.250 | 55.1 | 44.1 |
| 3200 | 1.279 | 58.0 | 46.3 |
| 3300 | 1.308 | 61.4* | 48.7 |
| 3400 | 1.338 | 65.1* | 51.5 |
| 3500 | 1.368 | 69.4* | 54.5 |
| 3600 | 1.398 | 74.2* | 58.0 |
| 3700 | 1.429 | 79.6* | 61.8* |
| 3800 | 1.459 | 85.8* | 66.1* |
| 3900 | 1.490 | 92.8* | 70.9* |
| 4000 | 1.521 | 100.6* | 76.3* |
| 4100 | 1.552 | 109.5* | 82.3* |
| 4200 | 1.584 | 119.5* | 89.1* |
| 4300 | 1.615 | 130.8* | 96.7* |
| 4400 | 1.647 | 143.6* | 105.4* |

**Selected P2 design point:** W_TO/S = 2300 N/m2 (235 kg/m2), T_SL/W_TO = 1.035 (minimum of max(W0_A, W0_B)).

**P1 (no Mach 3) design point for Profile B:** W_TO/S = 3300 N/m2, T_SL/W_TO = 1.213.

## (f)/(g) Sizing results

| Case | W0 (kg) | We (kg) | Wf (kg) | We/W0 | Wf/W0 | S (m2) | W/S (N/m2) | T/W | T_SL total (kN) | per engine, twin (kN) | fuel burned/W0 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A interceptor, P2; historical fit (K=1.00) | 43516 | 25994 | 16522 | 0.597 | 0.380 | 185.5 | 2300 | 1.035 | 442 | 221 | 0.359 |
| A-dash (M3 dash 100 km only), P2; historical fit (K=1.00) | 25200 | 15918 | 8282 | 0.632 | 0.329 | 107.4 | 2300 | 1.035 | 256 | 128 | 0.311 |
| B strike/air-sup, P2 (Mach 3 capable); historical fit (K=1.00) | 34972 | 21363 | 12609 | 0.611 | 0.361 | 149.1 | 2300 | 1.035 | 355 | 177 | 0.341 |
| B strike/air-sup, P1 (Mach 2 class, no M3); historical fit (K=1.00) | 22095 | 13735 | 7360 | 0.622 | 0.333 | 65.7 | 3300 | 1.213 | 263 | 131 | 0.315 |
| A interceptor, P2; F-22-calibrated LO penalty (K=1.20) | 196501 | 120446 | 75055 | 0.613 | 0.382 | 837.8 | 2300 | 1.035 | 1994 | 997 | 0.361 |
| A-dash (M3 dash 100 km only), P2; F-22-calibrated LO penalty (K=1.20) | 98212 | 64651 | 32561 | 0.658 | 0.332 | 418.8 | 2300 | 1.035 | 996 | 498 | 0.314 |
| B strike/air-sup, P2 (Mach 3 capable); F-22-calibrated LO penalty (K=1.20) | 150817 | 94996 | 54821 | 0.630 | 0.363 | 643.0 | 2300 | 1.035 | 1530 | 765 | 0.344 |
| B strike/air-sup, P1 (Mach 2 class, no M3); F-22-calibrated LO penalty (K=1.20) | 81624 | 53073 | 27551 | 0.650 | 0.338 | 242.6 | 3300 | 1.213 | 971 | 485 | 0.319 |

### Segment log: A interceptor, P2, K_we = 1.0 (W0 = 43516 kg)

| Segment | W start (kg) | W end (kg) | Wi/Wi-1 | fuel (kg) | details |
|---|---|---|---|---|---|
| 1 Warm-up, taxi, takeoff | 43516 | 42211 | 0.9700 | 1305 | f=0.970 |
| 2 Climb & accelerate to M3.0 | 42211 | 37145 | 0.8800 | 5065 | Raymer fit, f=0.8800 |
| 3 Mach 3.0 cruise-out 500 km | 37145 | 34601 | 0.9315 | 2544 | h=25.00 km, L/D=4.20, CL=0.118, max, c=1.92/h, f=0.9315 |
| 4 Combat 2 min max AB (M1.5, 12 km) | 34601 | 33166 | 0.9585 | 1435 | 2 min max AB, alpha=0.598, c=1.60/h |
| 5 Payload released | 33166 | 32266 | 0.9729 | 0 | -900 kg payload |
| 6 Re-accelerate to M2.5 | 32266 | 30683 | 0.9509 | 1583 | Raymer fit, f=0.9509 |
| 7 Return at M2.5, 500 km | 30683 | 28501 | 0.9289 | 2182 | h=25.00 km, L/D=4.59, CL=0.140, max, c=1.82/h, f=0.9289 |
| 8 Descent | 28501 | 28216 | 0.9900 | 285 | f=0.990 |
| 9 Reserve 20 min loiter, SL | 28216 | 27121 | 0.9612 | 1095 | SL, M=0.27, L/D=9.96, c=1.18/h, f=0.9612 |
| 10 Landing | 27121 | 26986 | 0.9950 | 136 | f=0.995 |

Mission fuel burned 14536 kg, reserve loiter 1095 kg, +5% mission fuel reserve, +1% trapped -> Wf = 16522 kg.

### Segment log: A-dash (M3 dash 100 km only), P2, K_we = 1.0 (W0 = 25200 kg)

| Segment | W start (kg) | W end (kg) | Wi/Wi-1 | fuel (kg) | details |
|---|---|---|---|---|---|
| 1 Warm-up, taxi, takeoff | 25200 | 24444 | 0.9700 | 756 | f=0.970 |
| 2 Climb to subsonic cruise | 24444 | 24077 | 0.9850 | 367 | f=0.985 |
| 3 M0.9 cruise-out 400 km | 24077 | 22865 | 0.9497 | 1212 | h=14.50 km, L/D=9.62, CL=0.288, mil, c=1.19/h, f=0.9497 |
| 4 Accelerate to M3.0 | 22865 | 20590 | 0.9005 | 2275 | Raymer fit, f=0.9005 |
| 5 Mach 3.0 dash 100 km | 20590 | 20297 | 0.9858 | 293 | h=25.00 km, L/D=4.16, CL=0.116, max, c=1.92/h, f=0.9858 |
| 6 Combat 2 min max AB (M1.5, 12 km) | 20297 | 19466 | 0.9591 | 831 | 2 min max AB, alpha=0.598, c=1.60/h |
| 7 Payload released | 19466 | 18566 | 0.9538 | 0 | -900 kg payload |
| 8 M0.9 return 500 km | 18566 | 17385 | 0.9364 | 1181 | h=15.00 km, L/D=9.45, CL=0.239, mil, c=1.19/h, f=0.9364 |
| 9 Descent | 17385 | 17211 | 0.9900 | 174 | f=0.990 |
| 10 Reserve 20 min loiter, SL | 17211 | 16542 | 0.9611 | 669 | SL, M=0.28, L/D=9.96, c=1.18/h, f=0.9611 |
| 11 Landing | 16542 | 16460 | 0.9950 | 83 | f=0.995 |

Mission fuel burned 7171 kg, reserve loiter 669 kg, +5% mission fuel reserve, +1% trapped -> Wf = 8282 kg.

### Segment log: B strike/air-sup, P2 (Mach 3 capable), K_we = 1.0 (W0 = 34972 kg)

| Segment | W start (kg) | W end (kg) | Wi/Wi-1 | fuel (kg) | details |
|---|---|---|---|---|---|
| 1 Warm-up, taxi, takeoff | 34972 | 33923 | 0.9700 | 1049 | f=0.970 |
| 2 Climb to subsonic cruise | 33923 | 33414 | 0.9850 | 509 | f=0.985 |
| 3 M0.9 cruise-out 600 km | 33414 | 30923 | 0.9254 | 2491 | h=14.50 km, L/D=9.62, CL=0.285, mil, c=1.19/h, f=0.9254 |
| 4 Accelerate to M1.6 | 30923 | 30193 | 0.9764 | 729 | Raymer fit, f=0.9764 |
| 5 Supercruise M1.6 200 km | 30193 | 29158 | 0.9657 | 1035 | h=18.00 km, L/D=4.62, CL=0.144, mil, c=1.37/h, f=0.9657 |
| 6 Combat 3 min max AB (M0.9, 9 km) | 29158 | 27844 | 0.9549 | 1314 | 3 min max AB, alpha=0.477, c=1.52/h |
| 7 Payload released | 27844 | 26944 | 0.9677 | 0 | -900 kg payload |
| 8 Re-accelerate to M1.6 | 26944 | 26308 | 0.9764 | 636 | Raymer fit, f=0.9764 |
| 9 Supercruise M1.6 200 km | 26308 | 25313 | 0.9622 | 995 | h=18.00 km, L/D=4.18, CL=0.125, mil, c=1.37/h, f=0.9622 |
| 10 M0.9 return 600 km | 25313 | 23384 | 0.9238 | 1929 | h=15.00 km, L/D=9.41, CL=0.233, mil, c=1.19/h, f=0.9238 |
| 11 Descent | 23384 | 23151 | 0.9900 | 234 | f=0.990 |
| 12 Reserve 20 min loiter, SL | 23151 | 22252 | 0.9612 | 899 | SL, M=0.28, L/D=9.96, c=1.18/h, f=0.9612 |
| 13 Landing | 22252 | 22141 | 0.9950 | 111 | f=0.995 |

Mission fuel burned 11033 kg, reserve loiter 899 kg, +5% mission fuel reserve, +1% trapped -> Wf = 12609 kg.

### Segment log: B strike/air-sup, P1 (Mach 2 class, no M3), K_we = 1.0 (W0 = 22095 kg)

| Segment | W start (kg) | W end (kg) | Wi/Wi-1 | fuel (kg) | details |
|---|---|---|---|---|---|
| 1 Warm-up, taxi, takeoff | 22095 | 21432 | 0.9700 | 663 | f=0.970 |
| 2 Climb to subsonic cruise | 21432 | 21111 | 0.9850 | 321 | f=0.985 |
| 3 M0.9 cruise-out 600 km | 21111 | 19759 | 0.9360 | 1352 | h=12.25 km, L/D=9.62, CL=0.289, mil, c=1.01/h, f=0.9360 |
| 4 Accelerate to M1.6 | 19759 | 19293 | 0.9764 | 466 | Raymer fit, f=0.9764 |
| 5 Supercruise M1.6 200 km | 19293 | 18824 | 0.9757 | 469 | h=18.00 km, L/D=5.72, CL=0.210, mil, c=1.20/h, f=0.9757 |
| 6 Combat 3 min max AB (M0.9, 9 km) | 18824 | 17690 | 0.9398 | 1134 | 3 min max AB, alpha=0.514, c=1.65/h |
| 7 Payload released | 17690 | 16790 | 0.9491 | 0 | -900 kg payload |
| 8 Re-accelerate to M1.6 | 16790 | 16394 | 0.9764 | 396 | Raymer fit, f=0.9764 |
| 9 Supercruise M1.6 200 km | 16394 | 15962 | 0.9737 | 432 | h=18.00 km, L/D=5.27, CL=0.178, mil, c=1.20/h, f=0.9737 |
| 10 M0.9 return 600 km | 15962 | 14940 | 0.9360 | 1022 | h=14.00 km, L/D=9.62, CL=0.287, mil, c=1.01/h, f=0.9360 |
| 11 Descent | 14940 | 14791 | 0.9900 | 149 | f=0.990 |
| 12 Reserve 20 min loiter, SL | 14791 | 14304 | 0.9671 | 487 | SL, M=0.33, L/D=9.96, c=1.00/h, f=0.9671 |
| 13 Landing | 14304 | 14232 | 0.9950 | 72 | f=0.995 |

Mission fuel burned 6476 kg, reserve loiter 487 kg, +5% mission fuel reserve, +1% trapped -> Wf = 7360 kg.

## Climb/acceleration to Mach 3: Raymer fit vs energy-state integration (Profile A, K=1.0)

| Method | Wi/Wi-1 | details | W0 A (t) |
|---|---|---|---|
| Raymer fit 0.991-0.007M-0.01M^2 | 0.8800 | Raymer fit, f=0.8800 | 43.5 |
| Energy method (max AB, this airframe) | 0.8992 | energy method, 4.5 min, f=0.8992 | 33.1 |

W0 (t) for all cases, K_we = 1.0, Raymer-fit vs energy-method climb/acceleration segments:

| Case | W0 Raymer | W0 energy | Wf/W0 Raymer | Wf/W0 energy |
|---|---|---|---|---|
| A interceptor, P2 | 43.5 | 33.1 | 0.380 | 0.355 |
| A-dash (M3 dash 100 km only), P2 | 25.2 | 19.9 | 0.329 | 0.303 |
| B strike/air-sup, P2 (Mach 3 capable) | 35.0 | 37.2 | 0.361 | 0.366 |
| B strike/air-sup, P1 (Mach 2 class, no M3) | 22.1 | 20.7 | 0.333 | 0.326 |

## Required installed SL static max (AB) thrust and engine class

| Case | K_we | Total (kN) | Twin: per engine (kN) | Single: one engine (kN) |
|---|---|---|---|---|
| A interceptor, P2 | 1.0 | 442 | 221 | 442 |
| A interceptor, P2 | 1.2 | 1994 | 997 | 1994 |
| A-dash (M3 dash 100 km only), P2 | 1.0 | 256 | 128 | 256 |
| A-dash (M3 dash 100 km only), P2 | 1.2 | 996 | 498 | 996 |
| B strike/air-sup, P2 (Mach 3 capable) | 1.0 | 355 | 177 | 355 |
| B strike/air-sup, P2 (Mach 3 capable) | 1.2 | 1530 | 765 | 1530 |
| B strike/air-sup, P1 (Mach 2 class, no M3) | 1.0 | 263 | 131 | 263 |
| B strike/air-sup, P1 (Mach 2 class, no M3) | 1.2 | 971 | 485 | 971 |

Reference AB classes (public): R-15B-300 ~100 kN; J58 145-151 kN; D-30F6 ~152 kN; F119 ~156 kN (35,000 lbf class). Single-engine values far above every listed fighter engine imply a twin-engine layout.

## Sensitivity S1: Profile A W0 (t) vs Mach 3 radius (M3 out, M2.5 back) and empty-weight factor K_we

| Radius (km) | K=1.0 | K=1.1 | K=1.2 | K=1.3 |
|---|---|---|---|---|
| 100 | 18.2 | 33.1 | 63.7* | 125.2* |
| 200 | 22.1 | 41.8 | 82.9* | 166.0* |
| 300 | 27.2 | 53.6 | 109.3* | 222.2* |
| 400 | 34.1 | 69.7* | 145.8* | 300.1* |
| 500 | 43.5 | 92.1* | 196.5* | NC |
| 600 | 56.5 | 123.3* | 267.7* | NC |
| 700 | 74.5* | 167.4* | 368.3* | NC |
| 800 | 100.1* | 230.1* | NC | NC |
| 1000 | 189.3* | NC | NC | NC |

## Sensitivity S2: W0 (t) vs empty-weight factor K_we (LO / hot-structure penalty)

| Case | K=0.9 | K=1.0 | K=1.05 | K=1.1 | K=1.15 | K=1.2 | K=1.25 | K=1.3 | K=1.35 |
|---|---|---|---|---|---|---|---|---|---|
| A interceptor, P2 | 21.9 | 43.5 | 63.0* | 92.1* | 134.7* | 196.5* | 284.7* | NC | NC |
| A-dash (M3 dash 100 km only), P2 | 14.1 | 25.2 | 34.8 | 48.7 | 69.0* | 98.2* | 139.8* | 198.3* | 279.6* |
| B strike/air-sup, P2 (Mach 3 capable) | 18.3 | 35.0 | 49.9 | 71.9* | 104.1* | 150.8* | 217.4* | 311.2* | NC |
| B strike/air-sup, P1 (Mach 2 class, no M3) | 12.8 | 22.1 | 30.0 | 41.4 | 57.9 | 81.6* | 115.3* | 162.5* | 228.0* |

## Sensitivity S3: one-at-a-time, Profile A baseline W0 = 43516 kg (K_we = 1.0)

| Change | W0 (kg) | dW0 | Wf/W0 | We/W0 |
|---|---|---|---|---|
| K_we 1.0 -> 1.2 (F-22-like LO penalty) | 196501 | +351.6% | 0.382 | 0.613 |
| Mach 3 radius 500 -> 300 km | 27235 | -37.4% | 0.337 | 0.627 |
| Mach 3 radius 500 -> 700 km | 74536 | +71.3% | 0.421 | 0.565 |
| Payload 900 -> 700 kg | 41364 | -4.9% | 0.380 | 0.600 |
| Payload 900 -> 1,000 kg | 44565 | +2.4% | 0.379 | 0.596 |
| TSFC x0.9 (better cycle) | 36037 | -17.2% | 0.363 | 0.609 |
| TSFC x1.1 | 53084 | +22.0% | 0.396 | 0.585 |
| Supersonic CD0 x0.85 (L/D_M3 ~5.3) | 37899 | -12.9% | 0.368 | 0.606 |
| Supersonic CD0 x1.2 (L/D_M3 ~4.5) | 52849 | +21.4% | 0.396 | 0.586 |
| Supersonic thrust knockdown 0.7 | 43516 | +0.0% | 0.380 | 0.597 |
| Energy-method climb instead of Raymer fit | 33089 | -24.0% | 0.355 | 0.614 |
| Simple Raymer We (Table 3.1) instead of detailed | 22705 | -47.8% | 0.377 | 0.579 |
| No explicit engine-mass correction | 40566 | -6.8% | 0.379 | 0.596 |
| Engine T/W 6 -> 8 (lighter Mach 3 engine) | 42753 | -1.8% | 0.380 | 0.597 |
| Engine T/W 6 -> 5 (heavier) | 44140 | +1.4% | 0.380 | 0.598 |
| Combat at M0.9/9 km instead of M1.5/12 km | 47083 | +8.2% | 0.386 | 0.593 |
| Mach 3 dash 100 km only (A-dash) | 25200 | -42.1% | 0.329 | 0.632 |
| Sustained turn 5 g -> 4 g (re-selected W/S 3600, T/W 0.95) | 22562 | -48.2% | 0.362 | 0.594 |
| Subsonic K1 0.18 -> 0.14 (re-selected W/S 2900, T/W 0.97) | 27329 | -37.2% | 0.364 | 0.599 |
| Mach 3/2.5 cruise ceiling 25 -> 28 km (re-selected W/S 2200, T/W 1.02) | 36885 | -15.2% | 0.366 | 0.607 |
| 4 g turn AND 28 km ceiling (re-selected W/S 3500, T/W 0.94) | 22460 | -48.4% | 0.361 | 0.594 |

## Sensitivity S4: W0 (t) for relaxed-requirement design points and K_we (engine P2)

| Design point | W/S / T/W | K_we | A | A-dash | B | S for A (m2) | A per-engine twin (kN) |
|---|---|---|---|---|---|---|---|
| Baseline 5 g, 25 km ceiling | 2300 / 1.03 | 1.0 | 43.5 | 25.2 | 35.0 | 186 | 221 |
| Baseline 5 g, 25 km ceiling | 2300 / 1.03 | 1.1 | 92.1* | 48.7 | 71.9* | 393 | 467 |
| Baseline 5 g, 25 km ceiling | 2300 / 1.03 | 1.2 | 196.5* | 98.2* | 150.8* | 838 | 997 |
| 4 g turn | 3600 / 0.95 | 1.0 | 22.6 | 16.0 | 18.8 | 61 | 105 |
| 4 g turn | 3600 / 0.95 | 1.1 | 42.7 | 28.0 | 34.4 | 116 | 199 |
| 4 g turn | 3600 / 0.95 | 1.2 | 84.9* | 52.2 | 66.5* | 231 | 395 |
| 4 g turn + 28 km ceiling | 3500 / 0.94 | 1.0 | 22.5 | 16.0 | 18.9 | 63 | 104 |
| 4 g turn + 28 km ceiling | 3500 / 0.94 | 1.1 | 42.6 | 28.0 | 34.6 | 119 | 197 |
| 4 g turn + 28 km ceiling | 3500 / 0.94 | 1.2 | 84.6* | 52.3 | 67.0* | 237 | 391 |

Weight growth factor dW0/dW_payload (Profile A, K=1.0) = 10.7 kg per kg of payload.

Plots: `out/sizing_radius_vs_W0.png`, `out/sizing_Kwe_vs_W0.png`, `out/sizing_tornado_A.png`, `out/constraint_diagram_P2_selected.png`
