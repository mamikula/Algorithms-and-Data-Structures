class Node:
    def __init__ (self):
        self.next = None
        self.value = None


def tab2list(tab):
    Head = Node()
    C = Head
    for i in range(len(tab)):
        X = Node()
        X.value = tab[i]
        C.next = X
        C = X
    return Head.next


def printlist(first):

    while first != None:
        print(first.value, "->", end = " ")
        first = first.next
    print("|")


def merge(L1, L2):
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


def cutlist(L):
    #zwrócić głowę po aktualnej

    if L is None: return None

    while L.next is not None and L.next.value >= L.value:
        L = L.next

    head = L.next
    L.next = None
    return head

'''
def mergesort2(L): #by falisz
    if L is None: return None

    while True:
        NH = None #new head
        NT = None #new tail
        while True:
            if L == None: break

            A = L
            L = cutlist(L) #co ciekawe wpływa także na A
            if L is None and NH is None:
                return A
            if L is None: #do posortowanej listy dokleja pozostałą nieposortowana część(reszte)
                NT.next = A
                break

            B = L
            L = cutlist(L)
            (C, D) = merge(A, B)

            if NT is None:
                NH = C
                NT = D
            else:
                NT.next = C
                NT = D

        L = NH
'''


def mergesort(first): #byme
    if first == None: return None

    while True:
        newhead = None
        newtail = None
        while True:
            part1 = first
            first = cutlist(first)

            if first == None and newhead == None:
                return part1

            if first == None:
                newtail.next = part1
                break

            part2 = first
            first = cutlist(first)

            (parthead, parttail) = merge(part1, part2)

            if newtail == None:
                newhead = parthead
                newtail = parttail
            else:
                newtail.next = parthead
                newtail = parttail

        first = newhead


tab = [1, 3, 5, 2, 5, 6, 4, 8, 9, 3, 7, 7]
L = tab2list(tab)
printlist(L)
mergesort(L)
printlist(L)
to_list(L)