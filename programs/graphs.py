from itertools import product
def fib_cube(n):
    # length-n binary strings, no "11" substring
    verts=[s for s in product((0,1),repeat=n) if all(not(s[i]==1 and s[i+1]==1) for i in range(n-1))]
    return _mkadj(verts)
def lucas_cube(n):
    if n==1: verts=[(0,)]  # single vertex to match L_1=1
    else:
        verts=[s for s in product((0,1),repeat=n)
               if all(not(s[i]==1 and s[i+1]==1) for i in range(n-1)) and not(s[0]==1 and s[n-1]==1)]
    return _mkadj(verts)
def _mkadj(verts):
    idx={v:i for i,v in enumerate(verts)}
    m=len(verts)
    adj=[[] for _ in range(m)]
    for v,i in idx.items():
        for k in range(len(v)):
            w=list(v); w[k]^=1; w=tuple(w)
            j=idx.get(w)
            if j is not None: adj[i].append(j)
    return m,adj
def fib(n):
    a,b=1,1
    for _ in range(n-1): a,b=b,a+b
    return a  # F_1=1,F_2=1
def lucas(n):
    a,b=2,1
    for _ in range(n-1): a,b=b,a+b
    return b  # L_1=1
if __name__=="__main__":
    for n in range(1,11):
        m,_=fib_cube(n); print("Fib",n,"|V|=",m,"F_{n+2}=",fib(n+2), "OK" if m==fib(n+2) else "MISMATCH")
    for n in range(1,11):
        m,_=lucas_cube(n); print("Luc",n,"|V|=",m,"L_n=",lucas(n),"OK" if m==lucas(n) else "MISMATCH")
