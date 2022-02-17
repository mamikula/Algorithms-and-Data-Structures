from random import randint, seed


#     tmp = L.next
#     L.next= L.next.next
#     tmp.next = pivot_cop.next
#     pivot_cop.next = tmp
class Node:
    def __init__(self):
        self.next = None
        self.value = None


def partition(L, last):
    pivot = L
    start = L
    while L.next != last:

        if L.next.value < pivot.value:
            tmp = L.next
            L.next = L.next.next
            tmp.next = start
            start = tmp

        else: L = L.next

    return (start, pivot)


def quicksort(L, end):
    if L != end:
        L, p = partition(L, end)
        L = quicksort(L, p)
        p.next = quicksort(p.next, end)

    return L

def qsort(L):
    return quicksort(L, None)


def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
#L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")


