

class Node:
    def __init__(self):
        self.name = None
        self.parent = None
        self.visited = None
        self.sasiedzi = []


def DFS(graph):
    def DFSVisit(G, u):
        u.visited = True
        for v in u.sasiedzi:
            if not v.visited:
                v.parent = u
                DFSVisit(G, v)

    for v in graph:
        v.visited = False
        v.parent = True

    for u in graph:
        if not u.visited:
            DFSVisit(graph, u)


def DFSmatrix(graph):
    n = len(graph)
    parent = [-1]*n
    visited = [None]*n


    def DFSVisit(graph, u, visited, parent):
        visited[u] = True
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] == 1:
                visited[v] = True
                parent[v] = u
                DFSVisit(graph, v, visited, parent)


    for u in range(n):
        if not visited[u]:
            DFSVisit(graph, u, visited, parent)

    print(visited)
    print(parent)





# graph = [[0, 1, 1, 0, 0, 0, 0, 0],
#          [1, 0, 0, 0, 1, 0, 0, 0],
#          [1, 0, 0, 1, 0, 1, 0, 0],
#          [0, 0, 1, 0, 1, 0, 0, 0],
#          [0, 1, 0, 1, 0, 1, 0, 0],
#          [0, 0, 1, 0, 1, 0, 1, 0],
#          [0, 0, 0, 0, 0, 1, 0, 1],
#          [0, 0, 0, 0, 0, 0, 1, 0]
#          ]
# DFSmatrix(graph)

# def DFS(graph, s):
#     visited = [False] * len(graph)
#
#     def dfs_visit(u):
#         nonlocal graph, visited
#
#         visited[u] = True
#         for v in graph[u]:
#             if not visited[v]:
#                 dfs_visit(v)
#
#     dfs_visit(s)
#