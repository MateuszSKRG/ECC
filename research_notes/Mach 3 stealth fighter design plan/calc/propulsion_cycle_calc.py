import math
g=1.4; cp=1.004; R=0.287; h=42800.0  # kJ/kg (Mattingly hydrocarbon h_PR)
T0=216.65; Tstd=288.15
a0=math.sqrt(g*R*1000*T0)
print("a0 stratosphere m/s",round(a0,1))
print("\n== Stagnation (compressor-face) temperature, stratosphere T0=216.65K ==")
for M in [0,0.9,1.5,2.0,2.5,2.83,3.0,3.2,3.5,4.0]:
    tr=1+0.2*M*M; Tt=T0*tr; pr=tr**3.5
    th=(T0/Tstd)*tr
    rec = 1.0 if M<=1 else 1-0.075*(M-1)**1.35
    print(f"M{M:4}: Tt2={Tt:6.1f}K ({Tt-273.15:6.1f}C) theta0={th:5.3f} ram Pt/P={pr:7.2f} MIL-E-5007D eta_r={rec:5.3f}")
print("\n== Max compressor PR if compressor exit Tt3 limited (ideal, isentropic) ==")
for Tt3max in [900,950,1000]:
    row=[]
    for M in [0,2.0,2.5,3.0,3.2]:
        Tt2 = (288.15 if M==0 else T0*(1+0.2*M*M))
        pc=(Tt3max/Tt2)**3.5
        row.append(f"M{M}:{pc:6.1f}")
    print(f"Tt3max={Tt3max}K ->", " ".join(row))
def turbojet(M,pic,Tt4,Tt7=None):
    tr=1+0.2*M*M; tl=Tt4/T0; tc=pic**(0.4/1.4)
    if tl - tr*tc <= 0: return None
    tt=1-tr/tl*(tc-1)
    if Tt7 is None:
        arg=2/0.4*tl/(tr*tc)*(tr*tc*tt-1)
        f=cp*T0*(tl-tr*tc)/h
    else:
        tlab=Tt7/T0
        arg=2/0.4*tlab*(1-1/(tr*tc*tt))
        f=cp*T0*(tlab-tr)/h
    if arg<=0: return None
    V9a0=math.sqrt(arg)
    Fm=a0*(V9a0-M)
    if Fm<=0: return (Fm,None,f)
    S=f/Fm*1e6  # mg/(N s)
    return Fm,S,f
def ramjet(M,Tt4):
    tr=1+0.2*M*M; tl=Tt4/T0
    if tl<=tr: return None
    V9a0=M*math.sqrt(tl/tr); Fm=a0*(V9a0-M); f=cp*T0*(tl-tr)/h
    return Fm,f/Fm*1e6,f
conv=3600/1e6*9.80665  # mg/(N s) -> 1/hr  : S[kg/(N s)]*g*3600
conv=1e-6*9.80665*3600
print("\n== Ideal cycle specific thrust (N/(kg/s)) and TSFC (1/h), Tt4=1800K, AB/ramburner Tt7=2200K, stratosphere ==")
print("M    | TJ pic=12 dry        | TJ pic=12 AB         | TJ pic=5 dry         | TJ pic=5 AB          | Ramjet Tt=2200K")
for M in [0.9,1.5,2.0,2.5,3.0,3.2,3.5,4.0]:
    out=[]
    for args in [(12,1800,None),(12,1800,2200),(5,1800,None),(5,1800,2200)]:
        r=turbojet(M,*args)
        if r is None or r[1] is None: out.append("   n/a              ")
        else: out.append(f"{r[0]:6.0f} / {r[1]*conv:5.2f}/h     ")
    r=ramjet(M,2200)
    out.append("n/a" if r is None or r[1] is None or r[0]<=0 else f"{r[0]:6.0f} / {r[1]*conv:5.2f}/h")
    print(f"{M:4} | "+" | ".join(out))
print("\n== Compressor-exit temperature Tt3 for pic=12 vs Mach (shows why high-OPR engine must throttle back) ==")
for M in [0,2.0,2.5,3.0,3.2]:
    Tt2 = (288.15 if M==0 else T0*(1+0.2*M*M))
    print(f"M{M}: Tt3 = {Tt2*12**(0.4/1.4):6.0f} K; pic=25: {Tt2*25**(0.4/1.4):6.0f} K")
print("\n== Breguet range R = (V/(c)) (L/D) ln(Wi/Wf) ==")
def breguet(M,TSFC_h,LD,Wi,Wf,T=216.65):
    V=M*math.sqrt(1.4*287*T)  # m/s
    Vkmh=V*3.6
    R=Vkmh/TSFC_h*LD*math.log(Wi/Wf)
    return V,R
cases=[("SR-71-like M3.2 cruise",3.2,1.9,6.0,1.6),
       ("SR-71-like, TSFC 1.6",3.2,1.6,6.0,1.6),
       ("M3 fighter, AB-cruise TJ TSFC 1.9, L/D 4.5, Wi/Wf 1.35",3.0,1.9,4.5,1.35),
       ("M3 fighter, VCE/turboramjet TSFC 1.5, L/D 4.5, Wi/Wf 1.35",3.0,1.5,4.5,1.35),
       ("Supercruise M1.6 dry TSFC 1.1, L/D 5.5, Wi/Wf 1.35",1.6,1.1,5.5,1.35),
       ("Subsonic M0.85 TSFC 0.85, L/D 10, Wi/Wf 1.35",0.85,0.85,10,1.35)]
for n,M,c,LD,wr in cases:
    V,Rr=breguet(M,c,LD,wr,1.0)
    print(f"{n}: V={V:5.0f} m/s; Range factor V*LD/c={V*3.6/c*LD:7.0f} km; R={Rr:6.0f} km ({Rr/1.852:5.0f} nmi)")
print("\n== Fuel sensible heat sink Q = cp_avg * dT (cp_avg ~2.1-2.6 kJ/kgK) ==")
for name,Tin,Tmax,cpavg in [("JP-8/Jet A limit 163C(325F)",40,163,2.2),("JP-8+100 ~288C(550F)",40,288,2.4),("JP-7 ~ 345C(650F) assumed",40,345,2.5),("JP-900 goal 482C(900F)",40,482,2.6)]:
    print(f"{name}: dT={Tmax-Tin} K -> ~{cpavg*(Tmax-Tin):5.0f} kJ/kg")
print("\n== Adiabatic wall (recovery) temperature, r=0.89, stratosphere ==")
for M in [2.0,2.5,2.83,3.0,3.2]:
    Taw=T0*(1+0.89*0.2*M*M); print(f"M{M}: Taw={Taw:5.0f} K ({Taw-273.15:4.0f} C)")
print("\n== Fuel flow implied: Wf_dot = TSFC*D ; D = W/(L/D) ==")
for W_kg,LD,c in [(25000,4.5,1.9),(25000,4.5,1.5),(30000,4.5,1.9)]:
    D=W_kg*9.80665/LD; wf=c*D/9.80665  # kg/h
    print(f"W={W_kg} kg, L/D={LD}, TSFC={c}/h: D={D/1000:5.1f} kN, fuel flow={wf:6.0f} kg/h = {wf/60:5.1f} kg/min")
