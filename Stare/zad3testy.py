#Marcin Mikuła
#
# Algorytm działa najpierw zliczajac ropę w górnym wierszu. Stosuje się do tego BFS, wszystkie zliczone
# jednostki są zamienione na 0. Zliczanie jest ograniczone przez m-1-x, bo dla tej wartosci osiagnelismy ilosc ropy potrzebnej do przejechania calej drogi.
#  Dlatego  najgorszą złożnością będzie O(m^2).
#
# Następny krok jest algorytmem dynamicznym (zadanie bardzo podobne do problemu żaby). Mamy miejsca, w których możemy zatankować ropę, i powinno
# jej wystarczyć, żeby przejść do końca. Tworzymy tablicę, która dla dp[x][y] oznacza, że z miasta A do
# punktu x mając w tym punkcie y energii można dostać się w minimalnie dp[x][y] kroków. Funkcja rekurencyjna -
# f(x, E) = min(f(x-1, E+1), 1 + f(x-1, E+1-E[x])), czyli lub przeszliśmy do następnego punktu bez tankowania, lub tankowaliśmy
# , i dlatego zwiększamy ilość kroków. E[x] - ilość dostępnej energii w punkcie x.

#chyba wszystkie odpowiedzi
from pprint import pprint



from collections import deque

INF = 10000


def neighs (x, y, T):
    neighs = []

    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:

        if 0 <= x + dx < len(T[0]) and 0 <= y + dy < len(T) and T[y + dy][x + dx] > 0:
            neighs.append((x + dx, y + dy))
    return neighs


def plan (T):
    n = len(T)
    m = len(T[0])

    for x in range(m):
        accumulated = 0
        if not T[0][x]:
            continue

        queue = deque()
        queue.append((x, 0))

        while len(queue) > 0:
            qx, qy = queue.popleft()
            accumulated += T[qy][qx]
            T[qy][qx] = 0

            if accumulated >= m - 1 - x:
                for nx in range(x + 1, m):
                    T[0][nx] = 0
                break

            for nx, ny in neighs(qx, qy, T):
                queue.append((nx, ny))

        T[0][x] = accumulated

    E = T[0]
    dp = [[INF for x in range(m)] for y in range(m)]
    for y in range(E[0] + 1):
        dp[0][E[0]] = 1

    for x in range(1, m):
        for y in range(m - 1):
            if y + 1 - E[x] < 0:
                dp[x][y] = dp[x - 1][y + 1]
            else:
                dp[x][y] = min(dp[x - 1][y + 1], 1 + dp[x - 1][y + 1 - E[x]])
        if E[x]:
            dp[x][m - 1] = 1 + dp[x - 1][y + 1 - E[x]]

    stops = []
    idx = 0
    for x in range(m - 1, 0, -1):

        if dp[x][idx] == dp[x - 1][idx + 1]:
            idx += 1
        else:

            idx = idx + 1 - E[x]
            stops.append(x)

    stops.append(0)

    return stops[::-1]

T0 = [
    [1, 0],
    [0, 0],
]

T1 = [
    [3, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

T2 = [
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

T3 = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

r0_T4 = [6, 0, 2, 0, 3, 0, 1, 0, 1, 0, 0, 1]
T4 = [
         r0_T4
     ] + (
             [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * (len(r0_T4) - 1)
     )

T5 = [
    [1, 0, 1, 0, 1, 0, 0, 2, 2, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

T6 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

T7 = [
    [5, 0, 1, 0, 0, 2, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
]

TESTS = [
    (T0, [0]),
    (T1, [0, 3]),
    (T2, [0, 4]),
    (T3, [0, 2]),
    (T4, [0, 2, 4]),
    (T5, [0, 2, 7]),
    (T6, [0]),
    (T7, [0, 5]),
]


def runtests(f):
    OK = True
    for no, (T, expected) in enumerate(TESTS):
        print(f"---------------------- #{no}")
        print("T: ")
        pprint(T)
        print(f"oczekiwany wynik: {expected}")
        assert all(len(T[i]) == len(T) for i in range(len(T))), f"len(T): {len(T)}, len(T[0]): {len(T[0])}"
        actual = f(T)
        print(f"uzyskany wynik  : {actual}")
        if actual != expected:
            print("PROBLEM!!!!!!")
            OK = False

    print("----------------------")
    if not OK:
        print("PROBLEMY!")
    else:
        print("OK")
runtests(plan)