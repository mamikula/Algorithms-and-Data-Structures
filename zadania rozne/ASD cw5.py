def f (P, K, w):
    n = len(P)
    maxk = 1
    for k in K:
        maxk += k
    T = [[0] * maxk for _ in range(n)]

    # te petle chyba trzeba poprawic, bo j idzie od 0 do maxk-1, a rozmiar tablicy P[] jest inny
    for j in range(maxk):
        if K[0] > j:
            T[j] = P[j]  # T jest dwuwymiarowa

    for i in range(1, n):
        for j in range(maxk):
            if K[i] > j:
                T[i][j] = min(T[i - 1][j], T[i][j - K[i]] + P[i])
            else:
                T[i][j] = T[i - 1][j]

    for j in range(maxk - 1):
        if T[n - 1][j + 1] > w:
            return j


def subSum (t, s):
    if s < 0:
        return False
    q = [[False for _ in range(s + 1)] for _ in t]
    # q[i, j] - elementy 0..i
    # q[len(t), s]
    for k in range(s + 1):
        q[0][k] = (t[0] == k)
    for i in range(1, len(t)):
        for k in range(s + 1):
            q[i][k] = q[i - 1][k] or t[i] == k
            if not q[i][k] and k - t[i] >= 0:
                q[i][k] = q[i - 1][k - t[i]]
    return q[-1][-1]


def LCS (A, B):
    n = len(A)

    F = [None] * (n + 1)
    for i in range(n + 1):
        F[i] = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])

    return F[n][n]


# end def

A1 = [1, 3, 5, 4]
B1 = [4, 5, 2, 4]

print(LCS(A1, B1))

A = [
    [5, 4, 8, 1, 5],
    [3, 6, 8, 3, 4],
    [5, 7, 1, 3, 5],
    [7, 3, 2, 3, 5],
    [7, 9, 0, 1, 2]]


def printway (T3, row, col):
    if T3[row][col] == 1:
        printway(T3, row - 1, col)
        print("v")
    if T3[row][col] == 0:
        printway(T3, row, col - 1)
        print("->")
    return


def way (T):
    n = len(T)
    T2 = []
    T3 = []
    for i in range(n):
        T2.append([])
        T3.append([])
        for j in range(n):
            T2[i].append(None)
            T3[i].append(None)
    T2[0][0] = T[0][0]
    for i in range(1, n):
        T2[0][i] = T2[0][i - 1] + T[0][i]
        T2[i][0] = T2[i - 1][0] + T[i][0]
        T3[i][0] = 1
        T3[0][i] = 0
    for row in range(1, n):
        for col in range(1, n):
            if T2[row - 1][col] + T[row][col] > T2[row][col - 1] + T[row][col]:
                T2[row][col] = T2[row][col - 1] + T[row][col]
                T3[row][col] = 0
            else:
                T2[row][col] = T2[row - 1][col] + T[row][col]
                T3[row][col] = 1

    printray(T3, n - 1, n - 1)


