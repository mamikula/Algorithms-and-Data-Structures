# Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który
# znajduje takie dwie liczby x i y z A, że y −x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
# że x < z < y (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla
# których A[i + 1] − A[i] jest największe)

def mmm(A):
    maxi = A[0]
    mini = A[0]
    n = len(A)
    for i in range(n):
        maxi = max(A[i], maxi)
        mini = min(A[i], mini)


    k = (maxi + mini) / n

    B = [[] for _ in range(n)]


    for i in range(n):
        id = int((A[i] - mini) / k)
        B[id].append(A[i])


    pmax = max(B[0])
    result = 0
    for i in range(1, n):
        if len(B[i]) != 0:
            cmin = min(B[i])
            result = max(result, cmin - pmax)
            pmax = max(B[i])


    return result

A = [0.5, 0.3, 0.01, 0.7, 0.2, 0.92, 0.11, 0.91]
res = mmm(A)
print(res)
A.sort()
print(A)