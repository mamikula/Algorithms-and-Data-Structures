# Marcin Mikuła
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


# runtests(plan)
T1 = [
    [3, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]
print(plan(T1))