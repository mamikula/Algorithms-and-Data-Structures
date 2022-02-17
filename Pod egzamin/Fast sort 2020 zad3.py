from math import log
from random import randint


def insertion_sort(A):
    for i in range(1, len(A)):
        while A[i - 1] > A[i] and i > 0:
            A[i], A[i - 1], = A[i - 1], A[i]
            i = i - 1

    return A

def bucket_sort(A):
    n = len(A)
    B = []

    for i in range(n):
        B.append([])

    for i in A:
        id = int(n * i)
        B[id].append(i)

    for i in range(n):
        B[i] = insertion_sort(B[i])

    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1

    return A
x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
print("Sorted Array is:")
# print(bucket_sort(x))


def fast_sort(tab, a):
    n = len(tab)
    B = []
    maxi = log(max(tab), a) + 1


    for i in range(n):
        B.append([])

    for i in tab:
        id = int(log(i, a)/maxi * n)
        B[id].append(i)

    for i in range(n):
        insertion_sort(B[i])

    k = 0

    for i in range(n):
        for j in range(len(B[i])):
            tab[k] = B[i][j]
            k += 1

    return tab

n = 100
T = [randint(1, 1000) for i in range(n)]

print(fast_sort(T, 2))

flaga = False
for i in range(n - 1):
    if T[i] > T[i + 1]:
        print("Błąd!")
        flaga = True
        break

if flaga == False:
    print("OK!")