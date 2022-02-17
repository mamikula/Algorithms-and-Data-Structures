from random import randint, shuffle, seed

def iSort (A, left, right):
  for i in range(left, right + 1):

    while A[i - 1] > A[i] and i > left:
      A[i], A[i - 1] = A[i - 1], A[i]
      i = i - 1


def partition (A, left, right):
  id = 0
  x = magicznePiatki(A, left, right)
  for i in range(left, right):
      if A[i] == x:
          id = i

  i = left - 1
  A[id], A[right] = A[right], A[id] #trzeba zamienic żeby pivot był "klasycznie" na koncu

  for j in range(left, right):
      if A[j] <= x:
          i += 1
          A[i], A[j] = A[j], A[i]
  A[i + 1], A[right] = A[right], A[i + 1]
  return i + 1


def magicznePiatki (A, l, r):  # l - left, r - right

    if r - l <= 5:
      iSort(A, l, r)
      #zwraca indeks elementu który jest pivotem zamiast wartości bo i tak cały czas operuje na głownej tablicy
      return A[(l + r) // 2]

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
      return A[l]

  q = partition(A, l, r)
  if q == k:
      return A[q]
  elif k < q:
      return select(A, l, q - 1, k)
  else:
      return select(A, q + 1, r, k)


n = 11
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = select(A, 0, len(A) - 1, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")

from random import randint, shuffle, seed


def iSort (A, left, right):  # insertion sort
    for i in range(left, right + 1):

        while A[i - 1] > A[i] and i > left:
            A[i], A[i - 1] = A[i - 1], A[i]
            i = i - 1


def partition(A, p, r):
    x = A[r] #pivot - element wedlog ktorego ustawiamy pozostale elementy
    i = p - 1 #ostatni element <= x, na poczatku ustawiamy go przed tablice
    for j in range(p, r): #j - aktualny element
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def select (A, l, r, k):
    if l == r:
        return A[l]

    q = partition(A, l, r)
    if q == k:
        return A[q]
    elif k < q:
        return select(A, l, q - 1, k)
    else:
        return select(A, q + 1, r, k)


def linearselect (A, k):
    return select(A, 0, len(A) - 1, k)


# seed(42)

n = 11
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")