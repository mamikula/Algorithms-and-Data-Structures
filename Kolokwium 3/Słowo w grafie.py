from queue import PriorityQueue
from math import inf

def Djikstra(L, E, W):

    n = len(L)
    mini = inf

    for s in range(n):

        if L[s] == W[0]:

            d = [inf] * n
            Q = PriorityQueue()
            d[s] = 0
            Q.put((d[s], s, 1))


            while not Q.empty():
                tmp = Q.get()
                u = tmp[1]
                id = tmp[2]

                if id == len(W):
                    mini = min(mini, tmp[0])
                    break

                for v in range(n):

                    if E[v][0] == u and L[E[v][1]] == W[id]:
                        d[E[v][1]] = d[u] + E[v][2]
                        Q.put((d[E[v][1]], E[v][1], id + 1))

                    elif E[v][1] == u and L[E[v][0]] == W[id]:
                        d[E[v][0]] = d[u] + E[v][2]
                        Q.put((d[E[v][0]], E[v][0], id + 1))

    return mini


L=["k","k","o","o","t","t"]
E=[(0,2,2),(1,2,1),(1,4,3),(1,3,2),(2,4,5),(3,4,1),(3,5,3)]
G=(L,E)

print(Djikstra(L, E, "ktot"))