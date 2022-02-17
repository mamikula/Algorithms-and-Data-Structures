#jezeli element po lewej jest wiekszy od elementu po prawej to zamuieniane sa miejscami
#algorytm konczy sie wtedy gdy nie zostanie dokonana zadna zamiana
def bubble_sort(list_a):
    #indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(list_a) - 1): #indexing_length):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]

    return list_a

print(bubble_sort([4, 6, 8, 3, 2, 5, 7, 8, 9]))


