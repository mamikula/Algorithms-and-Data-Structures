

def merge(arr, first, mid, last):
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
        merge2(arr, first, mid, last)


def merge2(arr, first, mid, last):
    n1 = mid - first + 1 #rozmiar lewej tymczasowej tablicy
    n2 = last - mid      #rozmiar prawej tymczasowej tablicy
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

    for k in range(first, last + 1): #first ma byc a nie 0 bo jak skleja np przedostatni i ostatni element to nie bedzie 0
        if i < n1:
            if j < n2:
                if R[j] <= L[i]:
                    arr[k] = R[j]
                    j += 1
                else:
                    arr[k] = L[i]
                    i += 1
            else:
                arr[k] = L[i]
                i += 1
        elif j < n2:
            arr[k] = R[j]
            j += 1

#wersja z gfg
def merge_Sort (arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]

        R = arr[mid:]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        #rozdzielanie tablicy głownej do twoj tablic pomocniczych
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # sprawdzanie czy cos zostało
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#moja wersja ostateczna
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
            if L[i] < R[j]:
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


arr = [12, 11, 13, 5, 6, 7, 1]
print("Given array is", end = "\n")
print(arr)
#merge_sort(arr, 0, len(arr)-1)
mergeSort(arr)
print("Sorted array is: ", end = "\n")
print(arr)

