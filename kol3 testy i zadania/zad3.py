from zad3testy import runtests
from zad3EK    import edmonds_karp
from math import inf

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

runtests( BlueAndGreen ) 
