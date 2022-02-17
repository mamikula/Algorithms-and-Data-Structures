from queue import PriorityQueue
from math import inf


def Djikstra(graph, s):

    n = len(graph)
    parent = [-1]*n
    d = [inf]*n

    Q = PriorityQueue()
    d[s] = 0

    Q.put((d[s], s))


    while not Q.empty():
        u = Q.get()[1]

        for v in range(n):
            if graph[u][v] != 0:
                if d[v] > d[u] + graph[u][v]:
                    d[v] = d[u] + graph[u][v]
                    parent[v] = u
                    Q.put((d[v], v))


    print(d)
    print(parent)