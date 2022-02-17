#Proszę zaproponować/zaimplementować algorytm scalający k posortowanych tablic o łącznej długości n
#w jedną posortowaną tablicę w czasie O(n ∗ log(k)).

def merge_tablicas(arr1):
    result = []
    k = len(arr1) - 1
    while k >= 0:
        result = merge(arr1[k], result)
        k -= 1

    return result


def merge(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)

    if size2 == 0:
        return arr1

    result = [0]*(size1 + size2)
    i = 0
    j = 0
    k = 0
    while i < size1 and j < size2:
        if arr1[i] <= arr2[j]:
            result[k] = arr1[i]
            i += 1
        else:
            result[k] = arr2[j]
            j += 1
        k += 1

    while i < size1:
        result[k] = arr1[i]
        i += 1
        k += 1

    while j < size2:
        result[k] = arr2[j]
        j += 1
        k += 1
    #print(result)
    return result


TAB = [[1, 7, 11],
       [2, 8, 14],
       [1, 3, 5, 9, 10],
       [2, 3, 4, 12, 13]]
G = merge_tablicas(TAB)
print(G)
#arr2 = []
#print(len(arr2))