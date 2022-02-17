from math import inf
from copy import deepcopy



def Students(T, i):
    return (T[i][2] - T[i][1]) * T[i][0]


def prev(T):
    n = len(T)
    res = [-1] * n
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if T[j][2] <= T[i][1]:
                res[i] = j
                break

    return res

def Select_buildings(T, p):
    A = deepcopy(T)
    T.sort(key = lambda T:T[2])


    n = len(T)
    dp = [[-inf] * (p + 1) for _ in range(n)]

    for i in range(T[0][3], p + 1):
        dp[0][i] = Students(T, 0)


    for i in range(n):
        cost = T[i][3]
        for j in range(p + 1):
            for v in range(i):
                if j >= cost and T[v][2] < T[i][1]:
                    dp[i][j] = max(dp[i - 1][j], Students(T, i) + dp[v][j - cost])



    for i in dp:
        print(i)

    id = -1
    mv = -inf
    for i in range(p + 1):
        if dp[n - 1][i] > mv:
            mv = dp[n - 1][i]
            id = i

    #print(id, mv)

    i = n - 1
    j = id
    val = mv
    res = []
    #poprawic odczytywanie, ma byc z odejmowaniem kolejnych elementow i szukaniem kolejnego najwiekszego w nowej kolumnie
    while i >= 0 and j >= 0:
        if j - 1 >= 0 and dp[i][j - 1] == val:
            j -= 1
        elif i - 1 >= 0 and dp[i - 1][j] == val:
            i -= 1
        else:
            res += [i]
            i -= 1
            val = dp[i][j]

    res.reverse()
    #print(res)
    result = []

    for i in res:
        for j in range(len(A)):
            if T[i] == A[j]:
                result.append(j)

    #print(result)
    result.sort()
    return result


T = [ (2, 1, 5, 3),
    (3, 7, 9, 2),
    (2, 8, 11, 1) ]
p = 5

T2 = [(8,2,6,2),(9,4,8,5),(9,8,9,2),(3,10,15,1),]
p2 = 7

# T4=[(1,8,12,5),(4,7,8,2),(3,2,3,6),(9,7,8,5),(8,21,22,8),(5,4,7,10),(1,21,24,10),(7,14,16,1)]
T4 = [(3, 2, 3, 6), (5, 4, 7, 10), (4, 7, 8, 2), (9, 7, 8, 5), (1, 8, 12, 5), (7, 14, 16, 1), (8, 21, 22, 8), (1, 21, 24, 10)]
p4 = 32

T5 = [(4, 7, 8, 2), (9, 7, 8, 5)]
p5 = 7


# T4.sort(key = lambda T4:T4[2])
# print(T4)

print(Select_buildings(T, p))