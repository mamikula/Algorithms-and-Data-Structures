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
                if u != v and S[u][v] != 0:
                    S[u][v] = min(S[u][v], S[u][t] + S[t][v])


n = len(T)
print(T)
FM(T)
T.append([0] * (n + 1))
for i in range(n + 1):
    T[i].append(0)
print(T)



for i in range(n - 2):
    if K[i] == 'B':
        T[n - 2][i] = 1
    else:
        T[i][n - 1] = 1


for i in range(n - 2):
    for j in range(n - 2):
        if T[i][j] < D:
            T[i][j] = 0
        else:
            if K[i] == 'B':
                T[j][i] = 0
            else:
                T[i][j] = 0




print(T)





