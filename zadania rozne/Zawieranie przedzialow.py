def partition(A, p, r, id):
    x = A[r][id] #pivot - element wedlog ktorego ustawiamy pozostale elementy
    i = p - 1 #ostatni element <= x, na poczatku ustawiamy go przed tablice
    for j in range(p, r): #j - aktualny element
        if A[j][id] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r, id):
    #1) wybierz pivot
    #2) podziel tablice na elementy <= od pivota i >= od pivota
    #3) posortuj rekurencyjne L i P
    if p < r:
        q =partition(A, p, r, id)
        quicksort(A, p, q - 1, id)
        quicksort(A, q + 1, r, id)


T=[(1,6),(3,5),(2,10),(4,7),(5,8),(9,11)]

def przedzialy(T):
    quicksort(T, 0, len(T) - 1, 1)
    maxcnt = 0
    a = 0
    b = 0
    cnt = 0

    for i in range(1, len(T) - 1):
        for j in range(i - 1, -1, -1):
            if T[i][0] > T[j][1]:
                break

            if T[i][0] > T[j][0]:
                cnt += 1
            else:
                if cnt > maxcnt:
                    a = T[i][0]
                    b = T[i][1]
                    cnt = 0

        if cnt > maxcnt:
            a = T[i][0]
            b = T[i][1]
            cnt = 0

    return (a, b)

print(przedzialy(T))