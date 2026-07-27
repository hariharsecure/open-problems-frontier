#!/usr/bin/env python3
"""
C07 deepen -- exact verification harness (Claude lineage).

Three exact sub-results, all integer/exact arithmetic:

  (A) Cohn-Umans reduction, verified on a concrete instance:
      a Triple Product Property (TPP) triple (S,T,U) in a group G makes the
      matrix-multiplication tensor <|S|,|T|,|U|> a RESTRICTION of the
      group-algebra structure tensor of C[G].  We verify this SYMBOLICALLY:
      "multiply" two matrices via the group algebra and confirm the result
      equals the true matrix product with NO spurious cross terms.

  (B) Abelian bound  |S||T||U| <= |G|  (Cohn-Umans 2003):
      proof = the sum-map (s,t,u) |-> s*t*u is injective under TPP for abelian G.
      Verified: TPP  <=>  sum-map-injective (abelian), the bound, and tightness,
      by EXHAUSTIVE search on small abelian groups.  Then the matmul-relevant
      "cube" capacity max{ n : exists TPP triple with |S|=|T|=|U|=n }, compared
      across cyclic Z/N (unbounded-exponent direction) vs elementary-abelian
      (Z/p)^k (bounded exponent) of EQUAL order.

  (C) Strassen: exhibit the 7 rank-one terms of <2,2,2>, confirm exact tensor
      equality over Z  =>  R(<2,2,2>) <= 7  =>  omega <= log2(7).

No floats except final decimal logs.  Small groups only (no RAM concern).
"""
import itertools, math
from fractions import Fraction
from sympy import symbols, expand, Integer, simplify

# ----------------------------------------------------------------------------
# Group abstraction: elements are ints 0..|G|-1; mul(a,b), inv(a), e=0.
# ----------------------------------------------------------------------------
class Group:
    def __init__(self, name, elements, mul, inv, e):
        self.name=name; self.elements=list(elements); self.mul=mul; self.inv=inv; self.e=e
        self.n=len(self.elements)
    def abelian(self):
        return all(self.mul(a,b)==self.mul(b,a) for a in self.elements for b in self.elements)

def cyclic(n):
    return Group(f"Z/{n}", range(n), lambda a,b:(a+b)%n, lambda a:(-a)%n, 0)

def direct_product(groups):
    # elements = tuples; encode as index into itertools.product
    tuples=list(itertools.product(*[g.elements for g in groups]))
    idx={t:i for i,t in enumerate(tuples)}
    def mul(a,b):
        ta,tb=tuples[a],tuples[b]
        return idx[tuple(g.mul(x,y) for g,x,y in zip(groups,ta,tb))]
    def inv(a):
        ta=tuples[a]
        return idx[tuple(g.inv(x) for g,x in zip(groups,ta))]
    e=idx[tuple(g.e for g in groups)]
    name="x".join(g.name for g in groups)
    return Group(name, range(len(tuples)), mul, inv, e)

# ----------------------------------------------------------------------------
# TPP: (S,T,U) satisfies the triple product property iff for all
#   s,s' in S, t,t' in T, u,u' in U:
#     (s^-1 s')(t^-1 t')(u^-1 u') = e  =>  s=s', t=t', u=u'.
# Direct check over the definition (no shortcut).
# ----------------------------------------------------------------------------
def is_tpp(G, S, T, U):
    mul,inv,e=G.mul,G.inv,G.e
    for s,sp in itertools.product(S,repeat=2):
        qs=mul(inv(s),sp)
        for t,tp in itertools.product(T,repeat=2):
            qt=mul(inv(t),tp)
            qsqt=mul(qs,qt)
            for u,up in itertools.product(U,repeat=2):
                qu=mul(inv(u),up)
                if mul(qsqt,qu)==e:
                    if not (s==sp and t==tp and u==up):
                        return False
    return True

# ----------------------------------------------------------------------------
# (A) Symbolic verification of the Cohn-Umans reduction on a concrete instance.
#   A indexed by S x T, B indexed by T x U.  Embed:
#     A -> sum_{s,t} A[s,t] * <group basis s^-1 t>
#     B -> sum_{t,u} B[t,u] * <group basis t^-1 u>
#   multiply in the group algebra, read coefficient at basis element s^-1 u.
#   Claim (TPP): that coefficient == sum_t A[s,t] B[t,u]  (true matmul), exactly.
# ----------------------------------------------------------------------------
def verify_reduction_symbolic(G, S, T, U):
    a,b,c=len(S),len(T),len(U)
    A={(s,t):symbols(f"A_{si}_{ti}") for si,s in enumerate(S) for ti,t in enumerate(T)}
    B={(t,u):symbols(f"B_{ti}_{ui}") for ti,t in enumerate(T) for ui,u in enumerate(U)}
    mul,inv=G.mul,G.inv
    # group-algebra product: coeff on each group element g
    prod={g:Integer(0) for g in G.elements}
    for (s,t),av in A.items():
        gA=mul(inv(s),t)
        for (t2,u),bv in B.items():
            gB=mul(inv(t2),u)
            prod[mul(gA,gB)] += av*bv
    ok=True; details=[]
    for si,s in enumerate(S):
        for ui,u in enumerate(U):
            g=mul(inv(s),u)
            got=expand(prod[g])
            want=expand(sum(A[(s,t)]*B[(t,u)] for t in T))
            if simplify(got-want)!=0:
                ok=False; details.append((s,u,str(got),str(want)))
    # also confirm no spurious support: the target basis elements s^-1 u must be
    # distinct across (s,u) (injectivity of the read-out map) -- part of TPP.
    readout=[mul(inv(s),u) for s in S for u in U]
    distinct_readout=(len(set(readout))==len(readout))
    return ok, distinct_readout, details

# ----------------------------------------------------------------------------
# (B) abelian: TPP  <=>  sum-map (s,t,u)->s*t*u injective; bound |S||T||U|<=|G|.
# ----------------------------------------------------------------------------
def summap_injective(G,S,T,U):
    seen=set()
    for s in S:
        for t in T:
            st=G.mul(s,t)
            for u in U:
                v=G.mul(st,u)
                if v in seen: return False
                seen.add(v)
    return True

def exhaustive_abelian_check(G, max_report=None):
    """For small abelian G: over ALL subset triples, confirm
       (i) TPP <=> sum-map injective, (ii) TPP => product<=|G|, and report max product."""
    els=list(G.elements)
    all_subsets=[]
    for r in range(1,len(els)+1):
        for c in itertools.combinations(els,r):
            all_subsets.append(c)
    max_prod=0; equiv_ok=True; bound_ok=True; n_tpp=0; witness=None
    for S in all_subsets:
        for T in all_subsets:
            if len(S)*len(T)>G.n and False: pass
            for U in all_subsets:
                tpp=is_tpp(G,S,T,U)
                inj=summap_injective(G,S,T,U)
                if tpp!=inj:
                    equiv_ok=False
                if tpp:
                    n_tpp+=1
                    p=len(S)*len(T)*len(U)
                    if p>G.n: bound_ok=False
                    if p>max_prod:
                        max_prod=p; witness=(S,T,U)
    return dict(max_prod=max_prod, equiv_tpp_injective=equiv_ok,
                bound_holds=bound_ok, n_tpp=n_tpp, witness=witness, order=G.n)

def max_cube(G, nmax=None):
    """max n s.t. exists TPP triple with |S|=|T|=|U|=n. cube search."""
    els=list(G.elements)
    if nmax is None:
        nmax=int(round(G.n**(1/3)))+1
    best=0; wit=None
    for n in range(1,nmax+1):
        subs=list(itertools.combinations(els,n))
        found=False
        # WLOG one subset contains e (translation-invariance of TPP) to prune
        subs_with_e=[c for c in subs if G.e in c] or subs
        for S in subs_with_e:
            for T in subs:
                for U in subs:
                    if is_tpp(G,S,T,U):
                        found=True; wit=(S,T,U); break
                if found: break
            if found: break
        if found: best=n
        else: break
    return best, wit

# ----------------------------------------------------------------------------
# (C) Strassen <2,2,2> exact tensor check.
# indices: A entries (i,j), B entries (k,l), C entries (m,n), i,j,k,l,m,n in {0,1}
# T[a_ij, b_kl, c_mn] = [j==k][i==m][l==n]
# ----------------------------------------------------------------------------
def matmul_tensor(m,n,p):
    T={}
    for i in range(m):
        for j in range(n):
            for k in range(n):
                for l in range(p):
                    for mm in range(m):
                        for nn in range(p):
                            v=1 if (j==k and i==mm and l==nn) else 0
                            if v: T[((i,j),(k,l),(mm,nn))]=v
    return T  # sparse: only nonzero (all ones)

def strassen_terms():
    # each term: (u dict on (i,j), v dict on (k,l), w dict on (m,n))
    A=lambda i,j:(i,j); B=lambda k,l:(k,l); C=lambda m,n:(m,n)
    terms=[]
    # M1=(a11+a22)(b11+b22); c11+=M1,c22+=M1
    terms.append(( {A(0,0):1,A(1,1):1}, {B(0,0):1,B(1,1):1}, {C(0,0):1,C(1,1):1} ))
    # M2=(a21+a22) b11; c21+=,c22-=
    terms.append(( {A(1,0):1,A(1,1):1}, {B(0,0):1},          {C(1,0):1,C(1,1):-1} ))
    # M3=a11(b12-b22); c12+=,c22+=
    terms.append(( {A(0,0):1},          {B(0,1):1,B(1,1):-1}, {C(0,1):1,C(1,1):1} ))
    # M4=a22(b21-b11); c11+=,c21+=
    terms.append(( {A(1,1):1},          {B(1,0):1,B(0,0):-1}, {C(0,0):1,C(1,0):1} ))
    # M5=(a11+a12) b22; c11-=,c12+=
    terms.append(( {A(0,0):1,A(0,1):1}, {B(1,1):1},          {C(0,0):-1,C(0,1):1} ))
    # M6=(a21-a11)(b11+b12); c22+=
    terms.append(( {A(1,0):1,A(0,0):-1},{B(0,0):1,B(0,1):1}, {C(1,1):1} ))
    # M7=(a12-a22)(b21+b22); c11+=
    terms.append(( {A(0,1):1,A(1,1):-1},{B(1,0):1,B(1,1):1}, {C(0,0):1} ))
    return terms

def verify_strassen():
    T=matmul_tensor(2,2,2)
    terms=strassen_terms()
    recon={}
    for u,v,w in terms:
        for ai,ac in u.items():
            for bi,bc in v.items():
                for ci,cc in w.items():
                    key=(ai,bi,ci)
                    recon[key]=recon.get(key,0)+ac*bc*cc
    recon={k:v for k,v in recon.items() if v!=0}
    return recon==T, len(terms), len(T), len(recon)

# ----------------------------------------------------------------------------
if __name__=="__main__":
    print("="*72)
    print("(A) Cohn-Umans reduction verified symbolically on a concrete instance")
    print("="*72)
    # A concrete abelian TPP triple: G=Z/2 x Z/2 x Z/2? use Z/8 with a cube n=2.
    # Simplest nontrivial: G=Z/2xZ/2, realize <2,1,2>? Let's find a real cube triple.
    G=cyclic(7)
    # In Z/7 find TPP triple S,T,U (sizes to be seen). Try S={0,1},T={0,2},U={0,3}? test.
    # Instead: use direct-product Z2^3 (order 8) which has a clean n=2 cube.
    G8c=cyclic(8)
    Z2=cyclic(2)
    G8e=direct_product([Z2,Z2,Z2])  # elementary abelian order 8
    # find a cube-2 TPP triple in Z/8
    n2,wit=max_cube(G8c,nmax=3)
    print(f"Z/8 max cube n = {n2}, witness sizes {[len(x) for x in wit] if wit else None}")
    S,T,U=wit
    ok,distinct,details=verify_reduction_symbolic(G8c,S,T,U)
    print(f"   TPP triple in Z/8: S={S} T={T} U={U}")
    print(f"   group-algebra product == true matmul (symbolic, exact): {ok}")
    print(f"   read-out map (s^-1 u) distinct: {distinct}")
    if not ok: print("   MISMATCH:",details[:3])

    print()
    print("="*72)
    print("(B) abelian bound |S||T||U| <= |G| and TPP<=>sum-injective; cube capacity")
    print("="*72)
    for G in [cyclic(2),cyclic(3),cyclic(4),cyclic(5),cyclic(6),
              direct_product([cyclic(2),cyclic(2)])]:
        r=exhaustive_abelian_check(G)
        print(f"  {G.name:14s} |G|={r['order']:2d}  max|S||T||U|={r['max_prod']:2d}  "
              f"bound(<=|G|):{r['bound_holds']}  TPP<=>sum-inj:{r['equiv_tpp_injective']}  "
              f"#TPP-triples={r['n_tpp']}")
    print()
    print("  Cube capacity (matmul-relevant): max n with TPP triple |S|=|T|=|U|=n")
    pairs=[("Z/7",cyclic(7)),("Z/8 (cyclic, 2^3)",cyclic(8)),
           ("(Z/2)^3 (elem-abelian)",direct_product([Z2,Z2,Z2])),
           ("Z/9 (cyclic)",cyclic(9)),
           ("(Z/3)^2? order9",direct_product([cyclic(3),cyclic(3)]))]
    for label,G in pairs:
        n,wit=max_cube(G)
        triv=int(round(G.n**(1/3)))
        print(f"    {label:26s} |G|={G.n:2d}  max-cube n={n}  (floor|G|^(1/3)~{triv}, n^3={n**3})")

    print()
    print("="*72)
    print("(C) Strassen <2,2,2> exact tensor check")
    print("="*72)
    ok,nterms,nnz,nrecon=verify_strassen()
    print(f"  reconstruction == matmul tensor <2,2,2> (exact over Z): {ok}")
    print(f"  #rank-one terms = {nterms}  => R(<2,2,2>) <= 7")
    print(f"  nonzero target entries = {nnz}, reconstructed nonzeros = {nrecon}")
    if ok:
        w=math.log2(7)
        print(f"  => omega <= log2(7) = {w:.6f}   (Strassen 1969)")
