# Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
# chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
# ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
# int goodThief( int A[], int n );
# która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
# kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
# poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
# jak najszybszy (ale przede wszystkim poprawny).




def goodThief(A):
    n = len(A)
    path = []
    res = [0]*n
    res[0] = A[0]
    res[1] = A[1]

    for i in range(2, n):
        res[i] = max(res[j] + A[i] for j in range(i - 1))

    j = 0
    num = 0
    for i in range(n - 1, -1, -1):
        if res[j] < res[i]:
            j = i
            num = res[j]


    for s in range(j, -1, -1):
        if num == res[s]:
            path.append(s)
            num -= A[s]

    return(res[j], path)



A = [2, 4, 8, 7, 10, 20, 1, 5, 10, 4]
print(goodThief(A))