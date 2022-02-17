

def DFSmatrix(graph):
    n = len(graph)
    visited = [False]*n


    def DFSVisit(graph, u, visited, order):
        visited[u] = True
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                DFSVisit(graph, v, visited, order)

        order.append(u)


    order = []
    for u in range(n):
        if not visited[u]:
            order.reverse()
            DFSVisit(graph, u, visited, order)

    order.reverse()
    print(order)

    for i in range(n):
        visited[i] = False
        for j in range(n):
            if graph[i][j] == 1:
                graph[i][j] = 0
                graph[j][i] = 2



    for i in order:
        if not visited[i]:
            neworder = []
            DFSVisit(graph, i, visited, neworder)
            print(neworder)




graph = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
         ]

DFSmatrix(graph)