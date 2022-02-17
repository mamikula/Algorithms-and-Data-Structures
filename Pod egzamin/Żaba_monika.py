from queue import PriorityQueue
from math import inf


def Djikstra(G, s, t):

    n = len(G)
    Q = PriorityQueue()
    Q.put((0, s, -1))



    while not Q.empty():
        tmp = Q.get()
        d = tmp[0]
        u = tmp[1]
        last = tmp[2]
        #print(tmp)


        if u == t:
            return d

        for v in G[u]:
            if last == 4:
                if v[1] == 1:
                    Q.put((d + 1, v[0], v[1]))
            else:
                Q.put((d + 1, v[0], v[1]))


def ES(a, b):
    return ((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5

def Zaba_monika(M, L):
    n = len(M)
    G = [[]]*n

    for i in range(n):
        for j in range(n):
            if i != j:
                if ES(M[i], M[j]) <= 0.5*L:
                    G[i] = G[i] + [(j, 1)]
                elif 0.5*L < ES(M[i], M[j]) <= L:
                    G[i] = G[i] + [(j, 2)]
                elif L < ES(M[i], M[j]) <= 2*L:
                    G[i] = G[i] + [(j, 4)]

    for i in G:
        print(i)

    return Djikstra(G, 0, n - 1)






M = [(1, 3), (2, 1), (2, 4), (6, 6), (6, 4), (8, 6), (4, 1), (2, 6), (8, 8), (6, 3), (4, 7)]
#M = [(0, 0), (0, 3), (0, 2), (3, 0), (3, 3)]
#M = [(0, 0), (1, 0), (2, 0), (3, 0)]
#M = [(0, 0), (0, 1), (1, 0), (5, 5)]
M.sort(key = lambda M:M[0])
print(M)
print()
L = 2
print(Zaba_monika(M, L))