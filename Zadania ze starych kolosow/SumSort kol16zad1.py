def iSort (A, left, right):  # insertion sort
    for i in range(left, right + 1):

        while A[i - 1] > A[i] and i > left:
            A[i], A[i - 1] = A[i - 1], A[i]
            i = i - 1


def partition (A, left, right):
    id = magicznePiatki(A, left, right)
    x = A[id]
    i = left - 1
    A[id], A[right] = A[right], A[id]  # trzeba zamienic żeby pivot był "klasycznie" na koncu

    for j in range(left, right):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1


def magicznePiatki (A, l, r):  # l - left, r - right, indeksy fragmentu talibyc na którym wykonuje się funckja

    if r - l <= 5:
        iSort(A, l, r)
        # zwraca indeks na element który jest pivotem zamiast wartości bo i tak cały czas operuje na głownej tablicy
        return (l + r) // 2

    else:
        n = (r - l + 1) // 5  # ilość wszystkich całkowitych 5 w tablicy
        j = l
        for i in range(n):
            first = l + i * 5  # początek 'piątki'
            last = first + 4  # koniec 'piątki'

            iSort(A, first, last)  # sortuje wnętrze piątki
            A[j], A[(first + last) // 2] = A[(first + last) // 2], A[
                j]  # wstawia mediane na odpowiednie miejsce na poczatku tablicy
            j += 1

        if (r + 1 - l) % 5 != 0:  # jezeli została część która nie jest pełną 5
            iSort(A, n * 5 + l, r)  # sortuje pozostałą część
            A[j], A[(5 * n + r + l) // 2] = A[(5 * n + r + l) // 2], A[j]
            j += 1

        return magicznePiatki(A, l, j - 1)


def select (A, l, r, k):
    if l == r:
        return
    q = partition(A, l, r)
    if q == k:
        return
    elif k < q:
        return select(A, l, q - 1, k)
    else:
        return select(A, q + 1, r, k)


def SumSort(A, B, n):
    for i in range(n, n * n, n):
        select(A, i - n, n * n - 1, i)

    for i in range(len(A)):
        B[i] = A[i]

    return B

T = [1, 1, 6, 2, 1, 3, 4, 4, 0]
B = [0]*len(T)
SumSort(T, B, 3)