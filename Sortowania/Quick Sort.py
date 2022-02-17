
def partition(A, p, r):
    x = A[r] #pivot - element wedlog ktorego ustawiamy pozostale elementy
    i = p - 1 #ostatni element <= x, na poczatku ustawiamy go przed tablice
    for j in range(p, r): #j - aktualny element
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def swap (A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Partition using Hoare's Partitioning scheme
def hoare(a, low, high):
    pivot = a[low]
    (i, j) = (low - 1, high + 1)

    while True:

        while True:
            i = i + 1
            if a[i] >= pivot:
                break

        while True:
            j = j - 1
            if a[j] <= pivot:
                break

        if i >= j:
            return j

        swap(a, i, j)


def quicksort(A, p, r):
    #1) wybierz pivot
    #2) podziel tablice na elementy <= od pivota i >= od pivota
    #3) posortuj rekurencyjne L i P
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def quicksort2(A, p ,r):
    while p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        p = q + 1


def quicksort3(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p <= r - q:
            quicksort(A, p, q - 1)
            p = q + 1
        else:
            quicksort(A, q + 1, r)
            r = q - 1



A = [9, 10, 7, 6, 5, 4, 7, 2, 6, 0]
print(A)
quicksort(A, 0, len(A) - 1)
print(A)
#A.reverse()
#print(A)
#quicksort2(A, 0, len(A) - 1)
#print(A)
