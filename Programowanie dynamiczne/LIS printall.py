#Marcin Mikuła

def lis(A): #funkcja z wykladu
    n = len(A)
    F = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1

    return (max(F), F)


def printres(A, F, i, ln, res): #res - tablica z wynikiem, na wejsciu zawiera ostatni element podciagu
    global cnt  #nie wiedziałem jak zwrocic z funkcji :(

    if ln == 1:
        for k in range(len(res) - 1, -1, -1):
            print(res[k], end=" ")
        cnt += 1
        print()

    for j in range(i):
        if A[j] < A[i] and F[j] + 1 == ln:
            res.append(A[j])            #jezeli rekurencja schodzi w dol, biore element
            printres(A, F, j, ln - 1, res)
            res.pop()                   #przy wyjsciu usuwam element z tablicy


A = [13, 7, 21, 42, 8, 2, 44, 53]
#A = [2, 1, 4, 3]
tmp = lis(A)
ln = tmp[0]
F = tmp[1]
cnt = 0
for i in range(len(A)):
    if F[i] == ln:
        printres(A, F, i, ln, [A[i]])
print(cnt)