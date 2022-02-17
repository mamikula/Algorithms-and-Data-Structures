C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1], [" szczecin", 1, 3],] #["Rzeszow" ,5, 1,]]
# Wrocław, Kraków, Warszawa, Gdańsk, paprykarz, Wrocław
#C = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],['I', 0.5, 2.5], ['J', 1.5, 3.5]]
#A I J H D E G F C B A
#C = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3], ["F",0.5,-2]]
#A F D B C E A
C.sort(key = lambda C: C[1])
print(C)


def prinT (T):
    for i in range(len(T)):
        for j in range(len(T[0])):
            print(T[i][j], end = " ")
        print()
    print()

n = len(C)
D = [[0] * n for _ in range(n)]
F = [[100] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        D[i][j] = int(((C[j][1] - C[i][1]) ** 2 + (C[j][2] - C[i][2]) ** 2) ** 0.5)

F[0][1] = D[0][1]
B = [[10] * n for _ in range(n)]

def tspf (i, j, F, D, B):

    if F[i][j] != 100:
        return F[i][j]
    if i == j - 1:
        best = 100
        id = -1
        for k in range(j - 1):
            tmp = tspf(k, j - 1, F, D, B) + D[k][j]
            if tmp < best:
                best = tmp
                id = k

        F[j - 1][j] = best
        B[j - 1][j] = id

    else:
        F[i][j] = tspf(i, j - 1, F, D, B) + D[j - 1][j]
        B[i][j] = j - 1
    return F[i][j]


for i in range(n - 1):
    tspf(i, n - 1, F, D, B)

#prinT(D)
#prinT(F)
prinT(B)


res = [C[n - 1][0]]
res.append(C[B[n - 2][n - 1]][0])
print(B[n - 2][n - 1], B[n - 2][n - 1], n - 1)
print(res)

def appitem(res, C, i, j, prev):
    print(i, j, res)
    if B[i][j] != 10:
        if prev < B[i][j]:
            res = [C[B[i][j]][0]] + res
            if prev != 0:
                appitem(res, C, i, j - 1, B[i][j])
            else:
                appitem(res, C, i, j - 1, prev)
        elif prev > B[i][j]:
            res.append(C[B[i][j]][0])
            if prev != 0:
                appitem(res, C, B[i][j], j - 1, B[i][j])
            else:


appitem(res, C, B[n - 2][n - 1], n - 1, B[n - 2][n - 1])
print(res)

min(F[i][n-1] + D[i][n-1] for i in range(n - 1))

def bitonicTSP (C):
    pass

bitonicTSP(C)