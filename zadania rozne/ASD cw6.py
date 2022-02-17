def tree (tab, index, n, prev):
    if index == n:
        return 0

    x = tree(tab, index + 1, n, prev)
    d = 0
    if prev + 1 != index:
        d = tree(tab, index + 1, n, index) + tab[index]

    return max(x, d)


t = [5, 1, 2, 4, 6, 9, 1, 3]
n = len(t)
#print(tree(t, 0, n, -100))


# --------------------------------------------

def bricks (T):
    n = len(T)
    F = [1] * n
    for i in range(1, n):
        for j in range(i):
            if T[j][0] <= T[i][0] and T[j][1] >= T[i][1] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
    return (n - max(F))


T = [[1, 10], [2, 5], [2, 7], [5, 8], [5, 6]]
T1 = [[2, 4], [8, 10], [4, 8], [1, 2], [10, 11]]
#print(bricks(T1))


# ------------------------------------------

def treeDP (C):
    n = len(C)
    F = [0] * n
    F[0] = C[0]
    # Musimy wprowadzić 2 wartości początkowe, bo w "rekurencji" cofamy się o 2.
    F[1] = max(C[0], C[1])

    for i in range(2, n):
        F[i] = max(F[i - 2] + C[i], F[i - 1])

    return F[n - 1]


t = [50, 100, 55]
#print(treeDP(t))


# ------------------------------------------
def pas (T, L):
    n = len(T)
    F = [[[None] * (L + 1) for _ in range(L + 1)] for _ in range(n)]
    for i in range(L):
        for j in range(L):
            F[0][i][j] = 0
    print("ilość samochodów:", p(T, F, 0, L, L))


def p (T, F, i, l, r):
    if F[i][l][r] != None:
        return F[i][l][r]
    a = 0
    b = 0
    if T[i] <= l:
        a = p(T, F, i + 1, l - T[i], r) + 1
    if T[i] <= r:
        b = p(T, F, i + 1, l, r - T[i]) + 1
    F[i][l][r] = max(a, b)
    return F[i][l][r]


t = [1, 1, 2, 3, 5, 8, 7]
L = 8
pas(t, L)
