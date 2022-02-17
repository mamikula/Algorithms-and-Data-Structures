#f(i)(j) - najtansza mozliwa sciezka do tego miejsca
#dp[i][j] = min(dp[i -1][j] , dp[i][j - 1]) + A[i][j]
#


def printT(F):
    for i in range(len(F)):
        for j in range(len(F[i])):
            print(F[i][j], end=" ")
        print("\n")


def road(A):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]

    F[0][0] = A[0][0]
    for i in range(1, n):
        for j in range(1, n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                F[i][j] = F[i][j - 1] + A[i][j]
            elif j == 0:
                F[i][j] = F[i - 1][j] + A[i][j]
            else:
                F[i][j] = min(F[i - 1][j], F[i][j - 1]) + A[i][j]

    return F[n-1][n-1], F

A = [ [1, 1, 1, 2],
    [2, 1, 3, 1],
    [3, 1, 2, 4],
    ]

print(road(A))