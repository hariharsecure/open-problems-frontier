#!/usr/bin/env python3
"""
M16 transfer-operator test (single-lineage; flag for Claude/Codex cross-check).

Builds the additive-dual (Fourier) Syracuse transfer operator L_n on Z/3^n Z,
exactly as defined in research/_lenses/analytic.md:

    (L g)(k) = sum_{a>=1} 2^{-a} * e(k * 2^{-a} / 3^n) * g(3 * 2^{-a} k mod 3^n),
    e(x) = exp(2*pi*i*x),  2^{-a} = modular inverse of 2^a mod 3^n (integer).

Value-only DP recursion it duals:  W_0=0, W_m = 2^{-a}(3 W_{m-1}+1) mod 3^n,
a_i iid Geom(P(a=k)=2^{-k}).  f_0 = 1, f_m = L f_{m-1},
P(W_n=b) = 3^{-n} sum_k e(-k b /3^n) f_n(k),  c_n = min_{3 not| b} P(W_n=b).

Deliverables:
  GATE : L reproduces c1=1/3, c2=2/63, c3=1598/262143 exactly (mpmath high prec).
  A    : spectrum of L_n (n=1..6): max|lambda|, lambda2, restricted spectral radius.
  B    : unit-(top-)shell block norms + the a=1 pinned mass (rate-floor test).
"""
import sys, math, time
from fractions import Fraction
import numpy as np

# ----------------------------------------------------------------------------
# operator builder
# ----------------------------------------------------------------------------
def build_L(n, dtype=np.complex128):
    """Dense L_n as a 3^n x 3^n matrix in the given numpy dtype (float path)."""
    mod = 3**n
    ordr = 2 * 3**(n-1)                 # multiplicative order of 2 mod 3^n
    tinv = pow(2, -1, mod)
    tpow = [1]*ordr
    for r in range(1, ordr):
        tpow[r] = (tpow[r-1]*tinv) % mod
    # geometric weight of a-residue class r (smallest positive a = r, or ordr if r==0)
    denom = 1.0 - 2.0**(-ordr)
    w = np.empty(ordr)
    for r in range(ordr):
        amin = r if r >= 1 else ordr
        w[r] = (2.0**(-amin)) / denom
    L = np.zeros((mod, mod), dtype=dtype)
    twopi = 2.0*math.pi
    for k in range(mod):
        for r in range(ordr):
            t = tpow[r]
            j = (3*t*k) % mod
            phase_arg = (k*t) % mod
            L[k, j] += w[r] * np.exp(1j*twopi*phase_arg/mod)
    return L, mod, ordr, w, tpow

def cn_from_L(L, n):
    """c_n via f_n = L^n 1, inverse DFT, min over units. numpy float path."""
    mod = 3**n
    f = np.ones(mod, dtype=np.complex128)
    for _ in range(n):
        f = L @ f
    # dist(b) = (1/mod) sum_k e(-k b/mod) f(k)   ==  inverse DFT (numpy ifft = 1/N sum e(+..))
    dist = np.fft.ifft(f).real          # ifft gives (1/N) sum_k f(k) e(+2pi i k b/N); we need e(-..)
    # e(-k b/mod): that's the forward DFT/N. Use conj trick:
    dist = (np.fft.fft(f).real)/mod     # (1/mod) sum_k f(k) e(-2pi i k b /mod)
    units = [b for b in range(mod) if b % 3 != 0]
    cvals = np.array([dist[b] for b in units])
    return cvals.min(), dist

# ----------------------------------------------------------------------------
# GATE: exact high-precision reproduction of c1,c2,c3 (and c4,c5,c6 as bonus)
# ----------------------------------------------------------------------------
def gate_mpmath(nmax=3, dps=60):
    import mpmath as mp
    mp.mp.dps = dps
    out = {}
    for n in range(1, nmax+1):
        mod = 3**n
        ordr = 2*3**(n-1)
        tinv = pow(2, -1, mod)
        tpow = [1]*ordr
        for r in range(1, ordr):
            tpow[r] = (tpow[r-1]*tinv) % mod
        denom = 1 - mp.mpf(2)**(-ordr)
        w = []
        for r in range(ordr):
            amin = r if r >= 1 else ordr
            w.append((mp.mpf(2)**(-amin))/denom)
        # L as mpmath matrix
        L = mp.matrix(mod, mod)
        for k in range(mod):
            for r in range(ordr):
                t = tpow[r]; j = (3*t*k) % mod
                ph = mp.e**(2j*mp.pi*((k*t) % mod)/mod)
                L[k, j] += w[r]*ph
        f = mp.matrix([1]*mod)
        for _ in range(n):
            f = L*f
        # dist(b) = (1/mod) sum_k e(-k b/mod) f(k)
        cbest = None
        for b in range(mod):
            if b % 3 == 0:
                continue
            s = mp.mpf(0)
            for k in range(mod):
                s += mp.e**(-2j*mp.pi*k*b/mod)*f[k]
            val = (s/mod).real
            if cbest is None or val < cbest:
                cbest = val
        out[n] = cbest
    return out

# ----------------------------------------------------------------------------
# spectrum + block norms
# ----------------------------------------------------------------------------
def analyze(n):
    L, mod, ordr, w, tpow = build_L(n)
    # gate float
    cn_float, dist = cn_from_L(L, n)
    # spectrum
    ev = np.linalg.eigvals(L)
    mags = np.sort(np.abs(ev))[::-1]
    lam1 = mags[0]
    lam2 = mags[1] if len(mags) > 1 else 0.0
    # "restricted spectral radius" = largest |eigenvalue| excluding the trivial 1
    # (the k=0 mass-conservation mode). Identify it: eigenvalue closest to 1.
    idx_trivial = np.argmin(np.abs(ev - 1.0))
    ev_rest = np.delete(ev, idx_trivial)
    restricted_sr = np.max(np.abs(ev_rest)) if len(ev_rest) else 0.0
    # unit (top) shell: k coprime to 3 (valuation 0)
    units = [k for k in range(mod) if k % 3 != 0]
    # forward block S: rows = units, cols = images (which live in valuation-1 shell)
    S = L[np.ix_(units, units)]         # unit->unit diagonal block (structurally ~0)
    # full forward action of unit rows (all columns):
    Urows = L[units, :]
    # operator norms
    sv_S = np.linalg.svd(Urows, compute_uv=False)
    sigma1 = sv_S[0]
    fro = np.linalg.norm(Urows)
    max_rowl1 = np.max(np.sum(np.abs(Urows), axis=1))
    # a=1 pinned mass (weight of the a=1 term)
    w1 = w[1]
    return dict(n=n, mod=mod, ordr=ordr, cn_float=cn_float,
                lam1=lam1, lam2=lam2, restricted_sr=restricted_sr,
                unit_block_diag_norm=np.linalg.norm(L[np.ix_(units, units)]),
                sigma1_unitrows=sigma1, fro_unitrows=fro, max_rowl1=max_rowl1,
                w1=w1, mags_top6=mags[:6])

# ----------------------------------------------------------------------------
# exact c_n from fraction files -> ladder, a_n, d_n
# ----------------------------------------------------------------------------
def load_exact_cn():
    import os
    base = os.path.expanduser("~/.sanshar/problems/research/M16/c9_sol_valueonly")
    c = {}
    for i in range(1, 10):
        p = os.path.join(base, f"c{i}_fraction.txt")
        if os.path.exists(p):
            with open(p) as fh:
                txt = fh.read().strip()
            num, den = txt.split("/")
            c[i] = Fraction(int(num), int(den))
    return c

def log3(fr):
    # -log3 via high precision
    import mpmath as mp
    mp.mp.dps = 50
    return float(-mp.log(mp.mpf(fr.numerator)/mp.mpf(fr.denominator), 3))

if __name__ == "__main__":
    t0 = time.time()
    print("="*70)
    print("GATE (mpmath, exact-fraction comparison)")
    print("="*70)
    exact = load_exact_cn()
    gate = gate_mpmath(3, dps=60)
    import mpmath as mp
    mp.mp.dps = 60
    gate_ok = True
    for n in (1, 2, 3):
        ex = mp.mpf(exact[n].numerator)/mp.mpf(exact[n].denominator)
        diff = abs(gate[n]-ex)
        ok = diff < mp.mpf(10)**(-40)
        gate_ok = gate_ok and ok
        print(f"  n={n}: L-operator c_n = {mp.nstr(gate[n],30)}")
        print(f"        exact  c_n = {mp.nstr(ex,30)}   |diff|={mp.nstr(diff,3)}  {'OK' if ok else 'FAIL'}")
    print(f"\n  GATE {'PASS' if gate_ok else 'FAIL'}")

    print("\n" + "="*70)
    print("SPECTRA (numpy float) n=1..6")
    print("="*70)
    rows = []
    for n in range(1, 7):
        r = analyze(n)
        rows.append(r)
        # float gate check vs exact
        exn = float(exact[n]) if n in exact else float('nan')
        gerr = abs(r['cn_float']-exn)
        print(f"n={n} mod={r['mod']:4d} ord={r['ordr']:4d} | c_n(float)={r['cn_float']:.10e} "
              f"exact={exn:.10e} err={gerr:.1e}")
        print(f"      |lambda|_top6 = {np.array2string(r['mags_top6'], precision=4, floatmode='fixed')}")
        print(f"      lam1={r['lam1']:.6f} lam2={r['lam2']:.3e} restricted_sr={r['restricted_sr']:.3e}")
        print(f"      unit-rows: sigma1={r['sigma1_unitrows']:.6f} fro={r['fro_unitrows']:.4f} "
              f"maxrowL1={r['max_rowl1']:.6f} | a=1 mass w1={r['w1']:.10f}")

    print("\n" + "="*70)
    print("TEST A table: -log3(restricted spectral radius) vs beta ladder")
    print("="*70)
    # beta ladder beta_m = -log3(c_{m+1})/m
    a = {n: log3(exact[n]) for n in exact}
    print(f"{'n':>2} {'restr_sr':>12} {'-log3(sr)':>12} {'beta_n(DP)':>12} {'lam2':>10}")
    for r in rows:
        n = r['n']
        sr = r['restricted_sr']
        nl = (-math.log(sr, 3)) if sr > 1e-12 else float('inf')
        beta_dp = (a[n+1]/n) if (n+1) in a else float('nan')
        print(f"{n:>2} {sr:12.3e} {nl:12.4f} {beta_dp:12.5f} {r['lam2']:10.2e}")

    print("\n" + "="*70)
    print("TEST B table: rate-floor  (a=1 mass, unit-shell block norm, exact d_n)")
    print("="*70)
    print("exact one-step defects d_n = a_2 + a_n - a_{n+1}  (a_n=-log3 c_n):")
    print(f"{'n':>2} {'d_n(exact)':>12} {'w1(a=1 mass)':>14} {'sigma1_unitrows':>16} {'maxRowL1':>10}")
    for n in range(2, 9):
        if n in a and (n+1) in a and 2 in a:
            dn = a[2] + a[n] - a[n+1]
        else:
            dn = float('nan')
        # match operator quantities where computed (n<=6)
        rr = next((x for x in rows if x['n'] == n), None)
        w1 = rr['w1'] if rr else float('nan')
        s1 = rr['sigma1_unitrows'] if rr else float('nan')
        ml = rr['max_rowl1'] if rr else float('nan')
        print(f"{n:>2} {dn:12.4f} {w1:14.10f} {s1:16.6f} {ml:10.6f}")

    print(f"\n[done in {time.time()-t0:.1f}s]")
