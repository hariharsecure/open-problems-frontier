from collections import deque
from graphs import fib_cube, lucas_cube

def cuthill_mckee(m, adj):
    deg=[len(adj[i]) for i in range(m)]
    visited=[False]*m
    order=[]
    for start in sorted(range(m), key=lambda x:deg[x]):
        if visited[start]: continue
        q=deque([start]); visited[start]=True
        while q:
            v=q.popleft(); order.append(v)
            for w in sorted(adj[v], key=lambda x:deg[x]):
                if not visited[w]: visited[w]=True; q.append(w)
    return order

def max_frontier(m, adj, order):
    pos={v:i for i,v in enumerate(order)}
    # closing[v] = last position among v and its neighbors
    closing=[max([pos[v]]+[pos[u] for u in adj[v]]) for v in range(m)]
    active=set(); mx=0
    for i,v in enumerate(order):
        active.add(v)
        # remove forgotten (closing<=i)
        active={u for u in active if closing[u]>i}
        mx=max(mx,len(active))
    return mx

if __name__=="__main__":
    for name,fn,rng in [("Fib",fib_cube,range(4,10)),("Luc",lucas_cube,range(4,10))]:
        for n in rng:
            m,adj=fn(n)
            o1=list(range(m))              # natural (string int) order
            o2=cuthill_mckee(m,adj)
            print("%s n=%d |V|=%d  frontier: natural=%d  CM=%d"%(name,n,m,max_frontier(m,adj,o1),max_frontier(m,adj,o2)))

