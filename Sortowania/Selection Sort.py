#wybiera najmienszy element i porownoje z pozostalymi, jezeli nie jest najminejszy to zamienia,
#po porzejsciu listy dodaje nastepny element i znowu tak samo
def selection_sort(list_a):
    #indexing_length = range(0, len(list_a) - 1)  #ostatni element bedzie posortowamy

    for i in range(0, len(list_a) - 1): #indexing_length:
        min_value = i

        for j in range(i + 1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j


        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a

print(selection_sort([1,2,3,4,6,3,23,4,5,2,4,10]))