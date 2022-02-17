def insertion_sort(A):
    for i in range(1, len(A)):
        while A[i - 1] > A[i] and i > 0:
            A[i], A[i - 1], = A[i - 1], A[i]
            i = i - 1

    return A

def bucket_sort(A):
    n = len(A)
    B = []
    maxi = max(A) + 1

    for i in range(n):
        B.append([])

    for i in A:
        id = int(n * (i / maxi))
        B[id].append(i)

    for i in range(n):
        B[i] = insertion_sort(B[i])

    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1

    return A

def SortTab(T, P):
    print(T)
    n = len(P)
    B = [[] for _ in range(n)]

    for i in T:
        for j in range(n):
            if  i >= P[j][0] and i <= P[j][1]:
                B[j] = B[j] + [i]
                break


    id = 0
    for i in B:
        bucket_sort(i)
    for i in B:
        for j in i:
            T[id] = j
            id += 1


    return T



T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
P = [(1, 5, 0.75), (4, 8, 0.25)]
print(SortTab(T, P))

