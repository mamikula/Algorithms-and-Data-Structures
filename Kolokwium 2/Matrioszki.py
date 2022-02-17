A = [(1, 2), (4, 5), (2, 6), (3, 1), (5, 5), (8, 2), (1, 1)]


def printSolution(A, P, i):
    if P[i] != -1:
        printSolution(A, P, P[i])
    print(A[i], end=" ")


def szasza(A):
    A.sort(key = lambda A: A[1])
    A.sort(key = lambda A: A[0])
    #print(A)

    n = len(A)
    P = [-1] * n
    F = [1] * n


    for i in range(n):
        for j in range(i):
            if A[j][0] < A[i][0] and A[j][1] < A[i][1] and F[j] + 1 > F[i]:
                P[i] = j
                F[i] = F[j] + 1

    print(max(F))
    return max(F), F, P


P = szasza(A)[2]
F = szasza(A)[1]

index_max = max(range(len(F)), key = F.__getitem__)
printSolution(A, P, index_max)


