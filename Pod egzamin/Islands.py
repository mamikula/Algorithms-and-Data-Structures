from math import inf


def Matrix_Dijkstra(G, s, t):
    n = len(G)
    d = [[inf, inf, inf] for _ in range(n)]

    visited = [False] * n
    d[s] = [0, 0, 0]

    def Min_Distance(d, visited):
        ind = -1
        mini = inf
        for i in range(len(d)):
            for j in range(3):
                if mini > d[i][j] and visited[i] == False:
                    mini = d[i][j]
                    ind = i

        return ind

    for s in range(n):
        u = Min_Distance(d, visited)
        visited[u] = True

        for v in range(n):
            if G[u][v] > 0 and visited[v] == False:
                for i in range(3):
                    for j in range(3):
                        if d[v][j] > d[u][i] + G[u][v] and j != (G[u][v] // 4) and i != (G[u][v] // 4):
                            d[v][j] = d[u][i] + G[u][v]



    print(d)

d = [[inf, inf, inf] for _ in range(10)]
d[0] = [0, 0, 0]
print(d)
G2=[[0,8,0,0,0,8],
    [8,0,5,0,5,0],
    [0,5,0,8,0,0],
    [0,0,8,0,1,0],
    [0,5,0,1,0,1],
    [8,0,0,0,1,0]]

Matrix_Dijkstra(G2, 0, 3)