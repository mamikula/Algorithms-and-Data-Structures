
def DFSmatrix(graph):
    n = len(graph)
    res = [[0 for _ in range(n)] for _ in range(n)]
    vis = [False]*n


    def DFSVisit(graph, u, vis, res):
        vis[u] = True
        n = len(graph)
        for v in range(n):
            if not vis[v] and graph[u][v] == 1:#and res[u][v] == 0:
                vis[v] = True
                DFSVisit(graph, v,  vis, res)


    for u in range(n):
        DFSVisit(graph, u,  vis, res)
        for i in range(n):
            if vis[i]:
                res[u][i] = 1
                vis[i] = False


    for i in res:
        print(i)


graph = [[0, 1, 1, 0],
         [0, 0, 1, 0],
         [1, 0, 0, 1],
         [0, 0, 0, 1]
         ]


DFSmatrix(graph)