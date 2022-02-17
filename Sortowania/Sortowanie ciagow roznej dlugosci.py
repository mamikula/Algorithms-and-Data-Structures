def zadom(A):
    n = len(A)

    C = [0] * n
    B = [0] * n
    for i in range(n):
        b = A[i] % n
        C[b] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        b = A[i] % n
        C[b] -= 1
        B[C[b]] = A[i]

    for i in range(n):
        A[i] = B[i]

################################################

    C = [0]*n
    B = [0]*n

    for i in range(n):
        a = A[i] // n
        C[a] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        a = A[i] // n
        C[a] -= 1
        B[C[a]] = A[i]

    for i in range(n):
        A[i] = B[i]


T = [80, 2, 25, 1, 12, 44, 36, 19, 1]

zadom(T)
print(T)
