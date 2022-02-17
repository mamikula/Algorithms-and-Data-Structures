from queue import PriorityQueue
from math import inf

def Dijkstra(G, P, f, a, b):

    n = len(G)
    parent = [-1]*n
    d = [inf]*n

    Q = PriorityQueue()
    d[a] = 0
    Q.put((d[a], a, f))

    while not Q.empty():
        tmp = Q.get()
        u = tmp[1]
        fuel = tmp[2]
        if u == b:
            res = [b]
            b = parent[b]
            while b != -1:
                res.append(b)
                b = parent[b]

            res.reverse()
            return res

        for v in range(n):
            if G[u][v] != -1:
                if d[v] > d[u] + G[u][v] and G[u][v] <= fuel:
                    d[v] = d[u] + G[u][v]
                    parent[v] = u
                    fuel -= G[u][v]
                    if v in P:
                        fuel = f
                    Q.put((d[v], v, fuel))

    return None

G = [[-1, 6, -1, 5, 2],
     [-1, -1, 1, 2, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 4, -1, -1],
     [-1, -1, 8, -1, -1]]

P = [0, 1, 3]

print(Dijkstra(G, P, 5, 0, 2))
print(Dijkstra(G, P, 6, 0, 2))
print(Dijkstra(G, P, 3, 0, 2))

