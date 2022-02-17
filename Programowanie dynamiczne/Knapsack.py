def printT(F):
    for i in range(len(F)):
        for j in range(len(F[i])):
            print(F[i][j], end=" ")
        print("\n")


def knapsack(W, P, MaxW):
    n = len(W)

    F = [[0]*(MaxW + 1) for _ in range(n)]

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]


    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i - 1][w]
            if w > W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])
                #print(F[i][w], W[i], P[i])
    printT(F)
    return F[n - 1][MaxW], F

def getsolution(F, W, P, i, w):
    if i < 0: return []
    if i == 0:
        if w > W[0]: return [0]
        return []

    if w > W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return getsolution(F, W, P, i - 1, w - W[i]) + [i]
    return getsolution(F, W, P, i - 1, w)

W = [4, 5, 12, 9, 1, 13]
P = [10, 8, 4, 5, 3, 7]
MaxW = 24

result = knapsack(W, P, MaxW)
print(result[0])
solution = getsolution(result[1], W, P, len(result[1]) - 1, MaxW)
print(solution)