from queue import PriorityQueue
from math import inf


def PathFinding(G, s, t):
    Q = PriorityQueue()
    visited = [False]*len(G)
    Q.put((-inf, s))

    parent = [-1] * len(G)

    while not Q.empty():
        tmp = Q.get()
        u = tmp[1]
        visited[u] = True

        if u == t:
            res = [t]

            while t != s:
                res.append(parent[t])
                t = parent[t]
            res.reverse()
            return res
        for v in G[u]:
            if u != v[0] and not visited[v[0]]:
                Q.put((-v[1], v[0]))
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
    [(4, 150), (0, 120)],
    [(2, 70), (3, 70)]
    ]

G3 = [
    [(1, 60), (3, 120)],
    [(0, 60), (2, 80)],
    [(1, 80), (4, 70)],
    [(2, 70), (3, 150)],
    []
    ]

print(PathFinding(G2, 0, 6))