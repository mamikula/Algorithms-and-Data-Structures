#Proszę zaimplementować algorytm zliczający liczbę inwersji w tablicy
inwersje = 0
def merge(arr, first, mid, last):
    global inwersje
    n1 = mid - first + 1 #rozmiar lewej tymczasowej tablicy
    n2 = last - mid     #rozmiar prawej tymczasowej tablicy
    L = [0]*n1
    R = [0]*n2

    #przepisywanie wartosci do tymczasowych tablic
    for i in range(n1):
        L[i] = arr[first + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    #indeksy do przechodzenia przez tablice tymczasowe
    i = 0
    j = 0
    k = first

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            inwersje += 1*len(L)
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, first, last):
    if first != last:
        mid = (first + last) // 2
        merge_sort(arr, first, mid)
        merge_sort(arr, mid + 1, last)
        merge(arr, first, mid, last)


t=[6,5,4,3,1]
merge_sort(t, 0, len(t) - 1)
print(t, inwersje)