from queue import PriorityQueue
from math import inf
#lepiej po prostu pętlą dopóki wierzchołek stopnia 2 i szukamy najdłuższego, zaczynamy kiedy wierzchołek ma stopien 2 i jednego sąsiada st > 2

def Djikstra(G):

    mini = inf
    n = len(G)
    res = PriorityQueue()
    for s in range(n):
        if len(G[s]) <= 2:

            parent = [-1]*n
            d = [inf]*n

            Q = PriorityQueue()
            d[s] = 0

            Q.put((d[s], s))
            visited = [False]*n


            while not Q.empty():
                tmp = Q.get()

                u = tmp[1]
                visited[u] = True


                for i in G[u]:
                    v = i[0]
                    if d[v] > d[u] - i[1] and not visited[v] and len(G[v]) <= 2:
                        d[v] = d[u] - i[1]
                        parent[v] = u
                        Q.put((d[v], v))

                if min(d) <= mini:
                    mini = min(d)
                    res.put((min(d), u, parent))


    tmp = res.get()
    parent = tmp[2]
    s = tmp[1]
    odp = [s]
    s = parent[s]
    while s != -1:
        odp.append(s)
        s = parent[s]

    print(odp, -tmp[0], tmp[1])

    #print(tmp)



G=[[(1,1),(6,1)],
   [(0,1),(2,1),(6,1)],
   [(1,1),(3,1)],
   [(2,1),(4,7)],
   [(3,7),(5,1)],
   [(4,1),(6,1)],
   [(0,1),(5,1),(1,1)]]


G2 =[[0,1,5,0,0],
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

G4=[[(1,1),(6,1)],
   [(0,1),(2,1)],
   [(1,1),(3,1)],
   [(2,1),(4,1)],
   [(3,1),(5,1)],
   [(4,1),(6,1)],
   [(0,1),(5,1)]]

Djikstra(G4)