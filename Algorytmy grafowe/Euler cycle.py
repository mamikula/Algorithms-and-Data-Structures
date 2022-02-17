
def DFSmatrix(graph):

    for i in graph:
        if sum(i) % 2 == 1:
            return None

    def DFSVisit(graph, u, path, visited):

        for v in range(len(graph)):
            if graph[u][v] == 1:
                graph[u][v] = 0
                graph[v][u] = 0
                visited[v] = True
                DFSVisit(graph, v, path, visited)
                path.append(v)


        return path


    n = len(graph)
    first = 0
    visited = [False] * n

    res = DFSVisit(graph, first, [], visited)
    res.append(first)

    print(visited)
    print(res)
    for i in range(n):
        if visited[i] == False:
            return None
    return res


graph = [
        [0,1,0,0,0,1],
        [1,0,1,0,1,1],
        [0,1,0,1,1,1],
        [0,0,1,0,1,0],
        [0,1,1,1,0,1],
        [1,1,1,0,1,0]
        ]


# graph =  [[0,1,1,0,0,0],
#         [1,0,1,1,0,1],
#         [1,1,0,0,1,1],
#         [0,1,0,0,0,1],
#         [0,0,1,0,0,1],
#         [0,1,1,1,1,0]]

# G3 = [
#     [0,1,0,0,0,1],
#     [1,0,1,0,1,1],
#     [0,1,0,1,1,1],
#     [0,0,1,0,1,0],
#     [0,1,1,1,0,1],
#     [1,1,1,0,1,0]
# ]

# graph = [[0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 1, 0, 1],
#      [0, 0, 0, 0, 1, 1],
#      [0, 1, 0, 0, 0, 1],
#      [0, 0, 1, 0, 0, 1],
#      [0, 1, 1, 1, 1, 0]]

G = graph.copy()

DFSmatrix(G)

