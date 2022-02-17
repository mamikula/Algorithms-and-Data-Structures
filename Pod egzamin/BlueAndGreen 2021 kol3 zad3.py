from math import inf
import copy, collections

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]


def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


#Flod-Marshal
def FM(S):
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][j] == 0:
                S[i][j] = inf


    n = len(S)
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if u != v:
                    S[u][v] = min(S[u][v], S[u][t] + S[t][v])


def BlueAndGreen(T, K, d):
    FM(T)

    n = len(T)
    G = [[0]*(n + 2) for _ in range(n + 2)]

    for i in range(0, n):
        for j in range(0, n):
            if K[i] == "B":
                G[0][i + 1] = 1
                if T[i][j] >= d and K[j] == "G":
                    G[i + 1][j + 1] = 1
            else:
                G[i + 1][n + 1] = 1
                if T[i][j] >= d and K[j] == "B":
                    G[j + 1][i + 1] = 1

    return edmonds_karp(G, 0, len(G) - 1)




T = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
K = ["B", "B", "G", "G", "B"]
D = 2

BlueAndGreen(T, K, D)