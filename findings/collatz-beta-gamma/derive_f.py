#!/usr/bin/env python3
"""
Derive the transmission map g(beta) = f(beta): Syracuse min-mass exponent beta
-> Collatz preimage-density exponent gamma, then solve f(beta*) = 0.84 (Krasikov-Lagarias).

Tao (2020 blog, arXiv:1909.03562) gives ONLY:
  - c_n = 3^{-beta n + o(n)},  beta >= 1,  submultiplicativity c_{a+b-1} >= c_a c_b
  - Prop 3: beta = 1  =>  #{preimages <= x} >> x^{1-o(1)}   (i.e. gamma -> 1)
  - "gamma < f(beta), f explicitly computable, f(beta)->1 as beta->1"  (NO closed form given)
  - improving beta improves KL 0.84 "in principle achievable numerically"

We DERIVE f from the preimage-counting mechanism and CALIBRATE it to the one hard
anchor Tao states: f(1) = 1. Then solve f(beta*) = 0.84.

Mechanism (large deviation / entropy count of backward Syracuse paths):
  An n-step preimage N of a fixed target corresponds to a length-n geometric path
  (a_1..a_n), a_i>=1, P(a_i=k)=2^{-k}, with total A = sum a_i, and size
     N  ~  2^A / 3^n.
  Size constraint N <= x = 2^L  =>  A <= A_max(n) = L + n*log2(3).
  # length-n paths with sum A  ~  C(A-1,n-1) ~ 2^{A h(n/A)}  (h = binary entropy).
  Fraction hitting the fixed target residue mod 3^n ~ c_n = 3^{-beta n} (min-mass).
  Submultiplicativity makes c_N >= 3^{-beta_{m-1} N} rigorous for all N, so an UPPER
  bound beta<=B transmits to a rigorous LOWER bound gamma >= f(B).  (Direction OK.)

  #preimages(<=x) ~ sum_n 3^{-beta n} * C(A_max(n), n)
    exponent(u) = -beta*u*c + (1+u*c)*h( u/(1+u*c) ),  c=log2(3), n=uL, A_max=(1+uc)L
    f(beta) = max_u exponent(u).
Calibration check: this MUST give f(1)=1 (reproduces Tao Prop 3). It does (below).
"""
import math

c = math.log2(3)  # 1.58496...

def h(w):
    if w <= 0.0 or w >= 1.0:
        return 0.0
    return -w*math.log2(w) - (1-w)*math.log2(1-w)

def exponent(u, beta):
    s = 1.0 + u*c            # A_max / L
    w = u/s                  # n/A_max
    return -beta*c*u + s*h(w)

def f(beta):
    # maximize over u>0
    best = -1e9
    bu = 0.0
    # coarse then fine
    u = 1e-4
    while u < 6.0:
        e = exponent(u, beta)
        if e > best:
            best, bu = e, u
        u += 1e-4
    # refine
    lo, hi = max(1e-5, bu-2e-4), bu+2e-4
    for _ in range(60):
        m1 = lo + (hi-lo)/3; m2 = hi - (hi-lo)/3
        if exponent(m1,beta) < exponent(m2,beta): lo = m1
        else: hi = m2
    um = (lo+hi)/2
    return exponent(um, beta), um

# 1) calibration
f1, u1 = f(1.0)
print(f"CALIBRATION  f(1.0) = {f1:.5f}  (argmax u={u1:.3f})   [must be ~1.000 to match Tao Prop 3]")

# 2) table
print("\n beta    f(beta)=gamma   argmax u")
for beta in [1.0,1.02,1.03,1.04,1.05,1.055,1.06,1.07,1.08,1.10,1.15,1.20,1.30,
             1.43,1.48,1.4796,1.555,1.638,1.756]:
    fb, ub = f(beta)
    star = "  <-- KL 0.84 level" if abs(fb-0.84)<0.01 else ""
    print(f" {beta:6.4f}   {fb:8.4f}      {ub:6.3f}{star}")

# 3) solve f(beta*) = 0.84 by bisection (f decreasing in beta)
target = 0.84
lo, hi = 1.0, 1.5
for _ in range(80):
    mid = (lo+hi)/2
    if f(mid)[0] > target: lo = mid
    else: hi = mid
bstar = (lo+hi)/2
print(f"\nTHRESHOLD  f(beta*) = 0.84  =>  beta* = {bstar:.4f}")

# 4) reachable comparison
for label,beta in [("reachable n=9 (~1.43)",1.43),("dual-verified (1.4796)",1.4796),
                   ("conjectured limit (1.0)",1.0)]:
    print(f"   f({beta}) = {f(beta)[0]:.4f}   [{label}]")
