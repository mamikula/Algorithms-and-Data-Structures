#Marcin Mikuła
from random import randint, seed

def mergesort(T):

  if len(T) > 1:
      size = len(T)
      mid = size // 2
      L = [0] * mid
      R = [0] * (size - mid)

      # przepisywanie tablicy do tablic pomocniczych
      for i in range(mid):
          L[i] = T[i]

      for i in range(mid, size):
          R[i - mid] = T[i]

      mergesort(L)

      mergesort(R)

      i = j = k = 0

      while i < len(L) and j < len(R):
          if L[i] < R[j]:
              T[k] = L[i]
              i += 1
          else:
              T[k] = R[j]
              j += 1
          k += 1
      #przepisywanie tego co zostalo
      while i < len(L):
          T[k] = L[i]
          i += 1
          k += 1

      while j < len(R):
          T[k] = R[j]
          j += 1
          k += 1
  return T


seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")