class Node:
    def __init__ (self):
        self.next = None
        self.value = None


def tab2list (A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist (L):
    while L != None:
        print(L.value, "->", end = " ")
        L = L.next
    print("|")


def merge (L1, L2):
    head = Node()
    tail = head

    while L1 != None and L2 != None:
        if L1.value <= L2.value:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next

        tail = tail.next

    if L1 is None: tail.next = L2
    if L2 is None: tail.next = L1
    while tail.next != None: tail = tail.next

    return head.next, tail


def cutList (L):
    # zwrócić głowę po aktualnej

    if L is None:
        return None

    while L.next is not None and L.next.value >= L.value:
        L = L.next

    H = L.next
    L.next = None
    return H


def mergesort (L):
    if L is None:
        return None
    tail = cutList(L)
    S = L
    L = tail
    while (L is not None):
        tail = cutList(L)
        S, _ = merge(S, L)
        L = tail
    return S


def mergesortv2 (L):
    if L == None:
        return None

    while True:
        NH = None
        NT = None
        while True:
            #print("hello")
            #printlist(L)
            if L == None: break
            A = L
            #printlist(A)
            L = cutList(L)
            #printlist(A)
            if L == None and NH == None:
                return A

            if L == None:   #do posortowanej listy dokleja pozostałą nieposortowana część
                NT.next = A
                break

            B = L
            L = cutList(L)
            #printlist(A)
            #printlist(B)
            (C, T) = merge(A, B)

            if NT == None:
                NH = C
                NT = T
            else:
                NT.next = C
                NT = T

        L = NH


T = list(range(9))
T.reverse()
print(T)
L = tab2list(T)
#printlist(L)
H = mergesortv2(L)
#printlist(H)

# T1 = [0, 2, 4, 6, 8]
# T2 = [1, 3, 5, 7, 9]
# L1 = tab2list(T1)
# L2 = tab2list(T2)
# L,t = merge(L1, L2)
# printlist(L)
# printlist(t)