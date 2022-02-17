# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)

def countsortwielok(A, jednok, wielok):
    C = [0] * 11
    B = [0] * len(A)
    D = [0] * len(A)

    for i in range(len(A)):
        C[wielok[i]] += 1

    for i in range(1, 11):
        C[i] = C[i] + C[i - 1]

    for i in range(len(A) - 1, -1, -1):
        C[wielok[i]] -= 1
        B[C[wielok[i]]] = A[i]
        D[C[wielok[i]]] = jednok[i]
    for i in range(len(A)):
        A[i] = B[i]
        jednok[i] = D[i]


def countsortjednok(A, jednok):
    C = [0]*11
    B = [0]*len(A)

    for i in range(len(A)):
        C[jednok[i]] += 1

    for i in range(9, -1, -1):
        C[i] = C[i] + C[i + 1]

    for i in range(len(A) - 1, -1, -1):
        C[jednok[i]] -= 1
        B[C[jednok[i]]] = A[i]

    for i in range(len(A)):
        A[i] = B[i]


def pretty_sort(T):
    wielok = [0] * len(T)
    jednok = [0] * len(T)
    id = 0
    for i in T:
        tmp = [0] * 10
        nice = 0
        ugly = 0
        while i > 0:
            if tmp[i % 10] == 0:
                tmp[i % 10] += 1
                nice += 1
            elif tmp[i % 10] != 2:
                nice -= 1
                ugly += 1
                tmp[i % 10] += 1

            i //= 10

        jednok[id] = nice
        wielok[id] = ugly
        id += 1


    countsortwielok(T, jednok, wielok)
    countsortjednok(T, jednok)


T = [123, 455, 1266, 114577, 2344, 67333, 1234567890]
pretty_sort(T)
print(T)

