"""1976 U.S. Standard Atmosphere (NOAA-S/T 76-1562), 0-84.852 km geopotential.

Inputs are GEOMETRIC altitude in metres by default; converted to geopotential
altitude H = r0*z/(r0+z) with r0 = 6,356,766 m (the 1976 standard's value).

Constants are those of the 1976 standard: R* = 8.31432 J/(mol K),
M0 = 28.9644 g/mol, g0 = 9.80665 m/s^2, gamma = 1.4, Sutherland mu with
beta = 1.458e-6 kg/(m s K^0.5), S = 110.4 K.

Run this file directly to execute the self-test against tabulated 1976 values.
"""
import math

G0 = 9.80665
R_STAR = 8.31432
M_AIR = 0.0289644
R_AIR = R_STAR / M_AIR          # 287.0531 J/(kg K)
GAMMA = 1.4
R_EARTH = 6356766.0
T_SL = 288.15
P_SL = 101325.0
RHO_SL = P_SL / (R_AIR * T_SL)  # 1.2250 kg/m^3
A_SL = math.sqrt(GAMMA * R_AIR * T_SL)

# (base geopotential altitude m, lapse rate K/m) for each layer
_LAYERS = [(0.0, -6.5e-3), (11000.0, 0.0), (20000.0, 1.0e-3), (32000.0, 2.8e-3),
           (47000.0, 0.0), (51000.0, -2.8e-3), (71000.0, -2.0e-3), (84852.0, None)]


def _build_bases():
    bases = []
    T, p = T_SL, P_SL
    for i, (Hb, L) in enumerate(_LAYERS[:-1]):
        bases.append((Hb, T, p, L))
        dH = _LAYERS[i + 1][0] - Hb
        if L == 0.0:
            p = p * math.exp(-G0 * dH / (R_AIR * T))
        else:
            Tn = T + L * dH
            p = p * (Tn / T) ** (-G0 / (R_AIR * L))
            T = Tn
    return bases


_BASES = _build_bases()


def geopotential(z):
    return R_EARTH * z / (R_EARTH + z)


def isa(z, geometric=True):
    """Return dict(T [K], p [Pa], rho [kg/m3], a [m/s], mu [Pa s], H [m geopotential])."""
    H = geopotential(z) if geometric else z
    if H < 0 or H > 84852.0:
        raise ValueError("altitude outside 0-84.852 km geopotential")
    for Hb, Tb, pb, L in reversed(_BASES):
        if H >= Hb:
            break
    if L == 0.0:
        T = Tb
        p = pb * math.exp(-G0 * (H - Hb) / (R_AIR * Tb))
    else:
        T = Tb + L * (H - Hb)
        p = pb * (T / Tb) ** (-G0 / (R_AIR * L))
    rho = p / (R_AIR * T)
    a = math.sqrt(GAMMA * R_AIR * T)
    mu = 1.458e-6 * T ** 1.5 / (T + 110.4)
    return dict(T=T, p=p, rho=rho, a=a, mu=mu, H=H)


# Tabulated 1976 USSA values at GEOMETRIC altitude (z [m], T [K], p [Pa], rho [kg/m3])
_CHECK = [(0.0, 288.150, 101325.0, 1.2250),
          (11000.0, 216.774, 22699.9, 0.36480),
          (20000.0, 216.650, 5529.3, 0.088910),
          (25000.0, 221.552, 2549.2, 0.040084)]


def self_test(tol=1e-3):
    rows = []
    for z, T, p, rho in _CHECK:
        s = isa(z)
        ok = (abs(s['T'] / T - 1) < tol and abs(s['p'] / p - 1) < tol
              and abs(s['rho'] / rho - 1) < tol)
        rows.append((z, s['T'], T, s['p'], p, s['rho'], rho, ok))
        if not ok:
            raise AssertionError(f"USSA76 self-test failed at z={z}: {s}")
    return rows


if __name__ == "__main__":
    for r in self_test():
        print("z=%7.0f m  T=%.3f (tab %.3f)  p=%.1f (tab %.1f)  rho=%.5f (tab %.5f)  ok=%s" % r)
