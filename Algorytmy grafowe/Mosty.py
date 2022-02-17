
def DFSmatrix(graph):
    n = len(graph)
    parent = [-1]*n
    visited = [None]*n
    D = [-1] * n
    Low = [1000]*n

    def DFSVisit(graph, u, visited, parent, D, Low):
        nonlocal time
        visited[u] = True
        D[u] = time
        Low[u] = time
        time += 1
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] == 1:
                visited[v] = True
                parent[v] = u
                DFSVisit(graph, v, visited, parent, D, Low)
            if graph[u][v] == 1 and visited[v] and v != parent[u]:
                Low[u] = min(D[v], D[u])

        for i in range(len(graph)):
            if graph[u][i] == 1 and i != parent[u]:
                Low[u] = min(Low[u], Low[i])


    time = 1
    for u in range(n):
        if not visited[u]:
            DFSVisit(graph, u, visited, parent, D, Low)
    #print(visited))

    print(Low)
    print(D)

#
# G = [[0, 1, 1, 0, 0, 0],
#      [1, 0, 1, 1, 0, 0],
#      [1, 1, 0, 0, 0, 0],
#      [0, 1, 0, 0, 1, 1],
#      [0, 0, 0, 1, 0, 1],
#      [0, 0, 0, 1, 1, 0]]

G = [[0, 1, 0, 0, 1, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 1, 1, 0],
     [1, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 0, 1, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0]
]

# G=[[0,1,0,0,1,0,0,0],
#    [1,0,1,0,0,0,0,0],
#    [0,1,0,1,1,0,0,0],
#    [0,0,1,0,0,1,1,0],
#    [1,0,1,0,0,0,0,1],
#    [0,0,0,1,0,0,1,0],
#    [0,0,0,1,0,1,0,0],
#    [0,0,0,0,1,0,0,0]]

print(DFSmatrix(G))