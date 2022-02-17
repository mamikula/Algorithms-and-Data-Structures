#bierzemy element i wstawiamy go do posortowanej listy na odpowiednie miejsce
#poprzez porownywanie kolejnych elementow z listy posortowanej
def insertion_sort(list_a):
    idl = range(1, len(list_a)) #ilosc liczb do posortowania
    for i in idl:
        value_to_sort = list_a[i] #wartosc do przestawienia w odpowiednie miejsce

        while list_a[i-1] > value_to_sort and i > 0: #dopoki element do wstawienia jest mniejszy niz odpowiednie elementy w liscie   python pozwala na ujemne indeksy
            list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
            i = i - 1


    return list_a

#print(insertion_sort([7, 6, 43, 2, 12, 1, 2, 2, 2, 3, 4, ]))

def insertion_sort_2(list_b):

    for i in range(1, len(list_b)):

        while list_b[i - 1] > list_b[i] and i > 0:
            list_b[i], list_b[i - 1] = list_b[i - 1], list_b[i]
            i = i - 1

    return list_b

print(insertion_sort_2([7, 6, 43, 2, 12, 1, 2, 2, 2, 3, 4]))