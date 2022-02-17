from queue import PriorityQueue
from math import inf


def PathFinding(G, s, t):
    Q = PriorityQueue()
    visited = [False]*len(G)

    Q.put((0, s))
    d = [inf]*len(G)
    parent = [-1] * len(G)

    while not Q.empty():
        tmp = Q.get()
        u = tmp[1]
        maxi = tmp[0]
        visited[u] = True

        if u == t:
            print(d[t])
            res = [t]

            while t != s:
                res.append(parent[t])
                t = parent[t]
            res.reverse()
            return res


        for v in G[u]:
            if not visited[v[0]]:
                maxi = min(d[v[0]], max(maxi, v[1]))
                Q.put((maxi, v[0]))
                d[v[0]] = maxi
                if d[v[0]] < max(maxi, v[1]):
                    continue
                parent[v[0]] = u

    return []




G = [[(1,4), (2,3)], # 0
    [(3,2)], # 1
    [(3,5)], # 2
    []] # 3

G2 = [
    [(1,1),(2,10)],
    [(6,1)],
    [(1,5),(3,4),(5,4)],
    [(4,4)],
    [(5,4)],
    [(3,4),(6,3)],
    []
]

G3=[ [(1,60),(3,120)],
    [(0,60),(2,80)],
    [(1,80),(4,70)],
    [(0,120),(4,150)],
    [(2,70),(3,150)],
    ]

print(PathFinding(G3, 0, 3))