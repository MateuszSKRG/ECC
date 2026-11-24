# Step 4 output: sanity check against real aircraft

## Reference aircraft: published inputs and derived ratios

W0 conventions: MiG-25P loaded 36,720 kg; MiG-31 normal 41,000 kg; SR-71A = empty + 80,000 lb fuel + 2 crew; F-22A = empty + ~18,000 lb internal fuel + ~1,100 kg pilot/internal AAMs.

| Aircraft | W0 (kg) | We (kg) | Wf internal (kg) | We/W0 | Wf/W0 | T_AB/W0 | T_dry/W0 | W0/S N/m2 (kg/m2) | AR | Mmax |
|---|---|---|---|---|---|---|---|---|---|---|
| MiG-25P | 36,720 | 20,000 | 14,100 | 0.545 | 0.384 | 0.56 | 0.41 | 5,865 (598) | 3.19 | 2.83 |
| MiG-31 | 41,000 | 21,820 | 16,130 | 0.532 | 0.393 | 0.76 | 0.46 | 6,527 (666) | 2.94 | 2.83 |
| SR-71A | 67,104 | 30,617 | 36,287 | 0.456 | 0.541 | 0.44 | 0.34 | 3,936 (401) | 1.72 | 3.2 |
| F-22A | 28,965 | 19,700 | 8,165 | 0.680 | 0.282 | 1.10 | 0.81 | 3,642 (371) | 2.37 | 2.25 |

- MiG-25P: We, W0 aerocorner; Wf flugzeuginfo (17,700 L); thrust flugzeuginfo; S, span commonly published (unverified)
- MiG-31: Wf Planehistoria; thrust Baidu/ArmyRecognition; MTOW 46,200 Fandom; We, normal W0 41,000, S, span unverified
- SR-71A: We 67,500 lb GlobalSecurity; fuel ~80,000 lb SR-71.org; W0 = We+fuel+2 crew (147,900 lb) because the NASA 140,000 lb gross implies partial fuel; S 1,800 ft2; thrust 32,500 lbf NASA; dry 25,000 lbf unverified
- F-22A: We af.mil; W0 = We + 18,000 lb internal fuel (unverified) + 1,100 kg pilot+AAM load (assumed); S 840 ft2 unverified; 35,000 lbf class af.mil

## Raymer empty-weight fits vs actual (ratio > 1 = heavier than the historical fit)

| Aircraft | We/W0 actual | Raymer T3.1 simple | actual/simple | Raymer T6.1 detailed | actual/detailed |
|---|---|---|---|---|---|
| MiG-25P | 0.545 | 0.538 | 1.01 | 0.558 | 0.98 |
| MiG-31 | 0.532 | 0.531 | 1.00 | 0.543 | 0.98 |
| SR-71A | 0.456 | 0.498 | 0.92 | 0.480 | 0.95 |
| F-22A | 0.680 | 0.555 | 1.22 | 0.570 | 1.19 |

## Sized concepts (K_we = 1.0) on the same ratios

| Concept | W0 (kg) | We/W0 | Wf/W0 | T/W | W/S (N/m2) | S (m2) |
|---|---|---|---|---|---|---|
| A interceptor, P2 | 43,516 | 0.597 | 0.380 | 1.03 | 2,300 | 186 |
| A-dash (M3 dash 100 km only), P2 | 25,200 | 0.632 | 0.329 | 1.03 | 2,300 | 107 |
| B strike/air-sup, P2 (Mach 3 capable) | 34,972 | 0.611 | 0.361 | 1.03 | 2,300 | 149 |
| B strike/air-sup, P1 (Mach 2 class, no M3) | 22,095 | 0.622 | 0.333 | 1.21 | 3,300 | 66 |

## Breguet consistency check, SR-71A at M3.2 / 24 km (cruise from end of Raymer climb to empty + crew + 8% fuel reserve)

| L/D | c (1/h) | W start (kg) | W end (kg) | Cruise range (km) | (nmi) |
|---|---|---|---|---|---|
| 5.5 | 1.7 | 56,382 | 33,720 | 5,704 | 3,080 |
| 5.5 | 1.9 | 56,382 | 33,720 | 5,104 | 2,756 |
| 6.0 | 1.7 | 56,382 | 33,720 | 6,223 | 3,360 |
| 6.0 | 1.9 | 56,382 | 33,720 | 5,568 | 3,006 |
| 6.6 | 1.7 | 56,382 | 33,720 | 6,845 | 3,696 |
| 6.6 | 1.9 | 56,382 | 33,720 | 6,124 | 3,307 |

(L/D)max 6.6 for the A-12 family is a sourced value; c = 1.7-1.9/h and the published unrefuelled range (~2,900-3,200 nmi) are NOT verified this session.

## Inverse check: radius supported by the reference aircraft's own internal fuel in this mission model

| Aircraft / model | Mission variant | Model radius | Cruise detail |
|---|---|---|---|
| F-22A on Profile B (P1 engine model, TR 1.07) | 0 km supercruise each way | 544 km total radius (544 subsonic) | h=18.00 km, L/D=5.97, CL=0.236, mil, c=1.20/h, f=1.0000 |
| F-22A on Profile B (P1 engine model, TR 1.07) | 185 km supercruise each way | 527 km total radius (342 subsonic) | h=18.00 km, L/D=6.00, CL=0.239, mil, c=1.20/h, f=0.9785 |
| MiG-31 on M2.35 out-and-back (LBPTF, TR 1.956) | payload 2,850 kg released | 830 km radius | h=19.75 km, L/D=5.36, CL=0.247, max, c=1.94/h, f=0.8866 |

Published radius claims to compare against were NOT verified this session (commonly quoted: F-22 ~760 km class on internal fuel; MiG-31 ~720 km at M2.35, listed as unverified in the sibling Russian-programs note).
