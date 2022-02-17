from queue import Queue

def BFS2(graph, s):
    Q = Queue()
    visited = [False]*len(graph)
    parent = [None]*len(graph)
    d = [-1]*len(graph)
    d[s] = 0
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in range(len(graph[u])):
            if graph[u][v] == 1 and visited[v] == False:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.put(v)

            elif graph[u][v] == 1 and visited[v] == True and d[v] == 2 and d[u] == 1:
                res = [v]
                res.append(parent[v])
                res.append(parent[u])
                res.append(u)
                res.append(v)
                return res

    return None


def cycleFour(graph):
    n = len(graph)
    if n < 4:
        return None
    for i in graph:
        if sum(i) != n - 1:
            res = None
            for i in range(n):
                if res is None:
                    res = BFS2(G2, i)

                else:
                    return res

    return [0, 1, 2, 3, 0]


G1 = [[0, 1, 1, 1],
      [1, 0, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 0]]


G2 = [
    [0,1,1,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0],
    [1,1,0,1,0,0,0,0,0,0],
    [0,0,1,0,1,1,1,1,0,1],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0],
    [0,0,0,1,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,1,0,1],
    [0,0,0,1,0,0,0,0,1,0]
]

# graf pelny bez jednej krawedzi
G3 = [
    [0,1,1,1,1],
    [1,0,1,1,1],
    [1,1,0,0,1],
    [1,1,0,0,1],
    [1,1,1,1,0]
]


print(cycleFour(G2))

