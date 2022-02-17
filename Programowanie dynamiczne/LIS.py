def lis(A):
    n = len(A)
    F = [1] * n
    P = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    #print(P)
    return (max(F), F, P)

def printSolution(A, P, i):
    if P[i] != -1:
        printSolution(A, P, P[i])
    print(A[i], end=" ")



A = [13, 7, 21, 42, 8, 2, 44, 53]
P = lis(A)[2]
i = lis(A)[0]

index_max = max(range(len(A)), key = A.__getitem__)
printSolution(A, P, index_max)
