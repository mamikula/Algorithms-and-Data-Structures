def countsort(A, k):
    C = [0]*k
    B = [0]*len(A)

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    for i in range(len(A) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    for i in range(len(A)):
        A[i] = B[i]

A = [1, 3, 2, 4, 0 ,3, 2]
countsort(A, 5)
print(A)