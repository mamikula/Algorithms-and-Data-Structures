from queue import PriorityQueue
from math import inf

# class Top:
#     def __init__(self):
#         pass

def relax(u, v, d, parent, w, Q, visited):
    if d[v] > d[u] + w[u][v]:
        d[v] = d[u] + w[u][v]
        parent[v] = u
        Q.put((d[v], v))


def Djikstra(graph, s):

    n = len(graph)
    parent = [-1]*n
    d = [inf]*n

    Q = PriorityQueue()
    d[s] = 0

    Q.put((d[s], s))
    visited = [False]*n
    # for i in range(n):
    #     Q.put((d[i], i))


    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for v in graph[u]:
            if d[v] > d[u] + graph[u][v]:
                d[v] = d[u] + graph[u][v]
                parent[v] = u
                Q.put((d[v], v))


    print(d)
    #print(parent)



def Matrix_Dijkstra(G, s):
    n = len(G)
    d = [inf] * n
    parent = [-1] * n
    visited = [False] * n
    d[s] = 0

    def Min_Distance(d, visited):
        ind = -1
        mini = inf
        for i in range(len(d)):
            if mini > d[i] and visited[i] == False:
                mini = d[i]
                ind = i

        return ind

    for s in range(n):
        u = Min_Distance(d, visited)
        visited[u] = True

        for v in range(n):
            if G[u][v] > 0 and visited[v] == False and d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                parent[v] = u

    print(d)



G =[[0,1,5,0,0],
    [1,0,2,7,8],
    [5,2,0,0,3],
    [0,7,0,0,1],
    [0,8,3,1,0]]

G1 =[[0,1,5,0,0,0],
    [1,0,2,7,8,0],
    [5,2,0,0,3,4],
    [0,7,0,0,1,0],
    [0,8,3,1,0,0],
    [0,0,4,0,0,0]
     ]

Djikstra(G, 0)
Matrix_Dijkstra(G, 0)