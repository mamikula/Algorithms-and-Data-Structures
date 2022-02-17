#  Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.


def iSort (A, left, right):
  for i in range(left, right + 1):

    while A[i - 1] > A[i] and i > left:
      A[i], A[i - 1] = A[i - 1], A[i]
      i = i - 1


def partition (A, left, right):
  id = magicznePiatki(A, left, right)
  x = A[id]
  i = left - 1
  A[id], A[right] = A[right], A[id] #trzeba zamienic żeby pivot był "klasycznie" na koncu

  for j in range(left, right):
      if A[j] >= x:
          i += 1
          A[i], A[j] = A[j], A[i]
  A[i + 1], A[right] = A[right], A[i + 1]
  return i + 1


def magicznePiatki (A, l, r):  # l - left, r - right, indeksy fragmentu talibyc na którym wykonuje się funckja

    if r - l <= 5:
      iSort(A, l, r)
      #zwraca indeks na element który jest pivotem zamiast wartości bo i tak cały czas operuje na głownej tablicy
      return (l + r) // 2

    else:
      n = (r - l + 1) // 5 #ilość wszystkich całkowitych 5 w tablicy
      j = l
      for i in range(n):
        first = l + i * 5  # początek 'piątki'
        last = first + 4   # koniec 'piątki'

        iSort(A, first, last) #sortuje wnętrze piątki
        A[j], A[(first + last) // 2] = A[(first + last) // 2], A[j] #wstawia mediane na odpowiednie miejsce na poczatku tablicy
        j += 1

      if (r + 1 - l) % 5 != 0: #jezeli została część która nie jest pełną 5
        iSort(A, n * 5 + l, r) #sortuje pozostałą część
        A[j], A[(5 * n + r + l) // 2] = A[(5 * n + r + l) // 2], A[j]
        j += 1

      return magicznePiatki(A, l, j - 1)


def select (A, l, r, k):
  if l == r:
      return l
  q = partition(A, l, r)
  if q == k:
      return q
  elif k < q:
      return select(A, l, q - 1, k)
  else:
      return select(A, q + 1, r, k)


def quicksort(A, p, r):
    #1) wybierz pivot
    #2) podziel tablice na elementy <= od pivota i >= od pivota
    #3) posortuj rekurencyjne L i P
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def section(T, p, q):
    print(T)
    p1 = select(T, 0, len(T) - 1, p)
    q1 = select(T, p, len(T) - 1, q)
    #print(T)
    quicksort(T, p1, q1)
    print(T[p1:q1 + 1])


T = [2, 1, 0, 3, 6, 5, 4, 8, 9, 10, 7]
section(T, 3, 7)
#print(T)
