from queue import Queue


def BFS(G, s):
    Q = Queue()
    n = len(G)
    visited = [False] * n
    res = []
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        u = Q.get()
        res.append(u)
        for v in range(n):
            if G[u][v] == 1 and visited[v] == False:
                visited[v] = True
                Q.put(v)


    for i in visited:
        if i == False:
            return None

    return res

def tasks(T):
    n = len(T)
    G = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if T[i][j] == 1:
                G[i][j] = 1
            elif T[i][j] == 2:
                G[j][i] = 1
            else:
                if i != j:
                    G[i][j] = 1
                    G[j][i] = 1

    for i in range(n):
        res = BFS(G, i)
        if res != None:
            return res

    return None

T = [ [0,2,1,1],
      [1,0,1,1],
      [2,2,0,1],
      [2,2,2,0] ]

print(tasks(T))



def DFSmatrix(graph):
    n = len(graph)
    parent = [-1]*n
    visited = [None]*n


    def DFSVisit(graph, u, visited, parent, path):
        visited[u] = True
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] == 1:
                visited[v] = True
                parent[v] = u
                DFSVisit(graph, v, visited, parent, path)

        path.append(u)
    path = []
    for u in range(n):
        if not visited[u]:
            DFSVisit(graph, u, visited, parent, path)

    path.reverse()
    print(path)


def tasks2(T):
    n = len(T)
    G = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if T[i][j] == 1:
                G[i][j] = 1

    DFSmatrix(G)

tasks2(T)