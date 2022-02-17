def radix_sort(A):

    n = len(A[0]) - 1
    while n >= 0:
        for i in range(1, len(A)):
            while i > 0 and A[i - 1][n] > A[i][n]:
                A[i - 1], A[i] = A[i], A[i - 1]
                i -= 1
        n -= 1

A = ["balka", "aolka", "acola", "ejola", "dkuba", "fseba"]
radix_sort(A)
print(A)
