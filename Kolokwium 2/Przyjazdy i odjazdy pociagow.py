def heapify(A, n, i): #n - ilosc wezlow w kopcu, i - potencjalnie zepsuty
    l = 2*i + 1
    r = 2*i + 2
    m = i #m - powininen to byc indeks pod ktorym jest element o najwiekszej wartosci w kopcu
    if l < n and A[l] < A[m]: m = l
    if r < n and A[r] < A[m]: m = r
    if m != i:
        #print(A, A[m], A[i])
        A[m], A[i] = A[i], A[m]
        heapify(A, n, m)


def add_to_heap(A, num):
    A.append(num)
    n = len(A) - 1
    parent = (n - 1) // 2
    while parent >= 0:
        if A[n] > A[parent]:
            #print(A[n], A[parent])
            A[n], A[parent] = A[parent], A[n]
            n = parent
            parent = (n - 1) // 2
            #print(A[n], A[parent])
        else: break


def pociagi(A, m):
    n = len(A)
    kopiec = []
    kopsize = 0


    for i in range(0, n):
        if kopsize != 0:
            if A[i][0] > kopiec[0]:
                kopiec.pop(0)
                kopsize -= 1


        add_to_heap(kopiec, A[i][1])
        kopsize += 1
        heapify(kopiec, kopsize, 0)

        if kopsize > m:
            return False

    return True


#A = [(0, 2), (1, 3), (2, 3), (3, 5), (4, 9), (5, 8), (6, 7)]
A = [(7, 9), (7, 7.34), (7.40, 8), (10, 10.21), (10.12, 10.17), (10.34, 11), (10.54, 10.57), (12, 12.3), (12, 13.32),
     (12.30, 12.43), (12.42, 13.32), (14, 14.21)]
print(pociagi(A, 3))