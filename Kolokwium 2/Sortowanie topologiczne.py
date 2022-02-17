
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


def DFS(graph):
    n = len(graph)
    parent = [-1]*n
    visited = [None]*n


    def DFSVisit(graph, u, visited, parent, path):
        visited[u] = True
        for v in graph[u]:
            if v != None and not visited[v]:
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


graph = [[1, 2],
         [2, 3],
         [],
         [4, 5, 6],
         [],
         [],
         [],
         [3],
         [7],
         ]

DFS(graph)


G=[[0,1,1,0,0,0,0,0,0],
   [0,0,1,1,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,1,1,1,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,1],
   [0,0,0,1,0,0,0,0,0]]

DFSmatrix(G)