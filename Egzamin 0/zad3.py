from zad3testy import runtests
from math import inf


def jumper(G, s, w):
    n = len(G)
    d = [[inf, inf] for _ in range(n)]
    visited = [False] * n

    d[s][0], d[s][1] = 0, 0

    def Min_Distance (d, visited):
        ind = -1
        mini = inf
        for i in range(len(d)):
            if mini > d[i][0] and visited[i] == False:
                mini = d[i][0]
                ind = i
            if mini > d[i][1] and visited[i] == False:
                mini = d[i][1]
                ind = i

        return ind

    for s in range(n):
        u = Min_Distance(d, visited)
        visited[u] = True

        for v in range(n):
            if d[v][0] > d[u][0] + G[u][v] and G[u][v] > 0 and visited[v] == False:
                d[v][0] = d[u][0] + G[u][v]

                for k in range(n):
                    if d[k][1] > d[u][0] + max(G[v][k], G[u][v]) and G[v][k] > 0 and visited[k] == False:
                        d[k][1] = d[u][0] + max(G[v][k], G[u][v])

            if d[v][0] > d[u][1] + G[u][v] and G[u][v] > 0 and visited[v] == False:
                d[v][0] = d[u][1] + G[u][v]

    return min(d[w][0], d[w][1])


runtests(jumper)