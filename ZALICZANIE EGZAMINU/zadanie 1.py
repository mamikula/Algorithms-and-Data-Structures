from copy import deepcopy
from math import inf

def mergeSort(arr):
    if len(arr) > 1:
        size = len(arr)
        mid = size // 2
        L = [0] * mid
        R = [0] * (size - mid)
        #przepisywanie tablicy do tablic pomocniczych
        for i in range(mid):
            L[i] = arr[i]

        for i in range(mid, size):
            R[i - mid] = arr[i]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



def Chaos_index(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)

    A = deepcopy(T)
    mergeSort(A)
    print(A)
    k = -inf
    for i in range(n):
        k = max(k, i - T[A[i][1]][1])

    return k

T = [0, 2, 1.1, 2]
print(Chaos_index(T))
