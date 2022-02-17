def tankb2(S, P, l, t):
    n = len(S)
    F = [0] * n#F(i) minimalny koszt dotarcia do stacji i zatankowania na tej stacji
    F[0] = P[0] * S[0]#do i = 0 można dotrzeć tylko w jeden sposób
    for i in range(1, n):
        j = i - 1
        minimal = F[j] + (S[i] - S[j]) * P[i]
        while j >= 0 and l >= S[i] - S[j]:#szukam minimum po wszystkich stacjach w zasięgu(z tyłu)
            minimal = min(minimal, F[j] + (S[i] - S[j]) * P[i])
            j -= 1
        if j == -1 and l >= S[i]:#jesli możemy dojechać od zera i nie opłaca się tankować na wcześniejszych
            minimal = min(minimal, P[i] * S[i])
        F[i] = minimal
    res = F[n - 1]
    for i in range(n):#rozwiązanie to min po wszystkich stacjach które mają w zasięgu t
        if t - S[i] <= l:
            res = min(F[i], res)
    return res


S = [1, 9, 15, 16, 17, 27, 28]
P = [1, 100, 10, 15, 1, 30, 30]
print(tankb2(S, P, 14, 30))




def tankb1(S, P, L, t):
    n = len(S) + 2
    stations = [[None, None] for _ in range(n)]
    stations[0][0], stations[0][1] = 0, 0

    for i in range(1, n - 1):
        stations[i][0], stations[i][1] = S[i - 1], P[i - 1]
    stations[n - 1][0], stations[n - 1][1] = t, 0

    fuel = 0
    cost = 0
    for i in range(n - 1):
        if i > 0:
            fuel -= (stations[i][0] - stations[i - 1][0])
        min_cost = stations[i][1]
        st = i
        for j in range(i, n):
            if stations[j][0] > stations[i][0] + L:
                break
            else:
                if stations[j][1] < min_cost:
                    min_cost, st = stations[j][1], j
                    break
        if st == i:
            cost += min(L - fuel, (t - stations[i][0]) - fuel) * stations[i][1]
            fuel = L
        else:
            cost += max(((stations[st][0] - stations[i][0]) - fuel) * stations[i][1], 0)
            fuel = max(fuel, stations[st][0] - stations[i][0])

    return cost


L = 10
S = [8, 11, 15, 16]
P = [40, 7, 15, 12]
t = 23
print(tankb1(S, P, L, t))


def job_sequeencing(T, limit_time):
    T.sort(key=lambda x: x[2], reverse=True)
    jobs = [-1]*limit_time
    result = [-1]*limit_time
    max_profit = 0
    for i in range(len(T)):
        for j in range(T[i][1]-1, -1, -1):
            if result[j] == -1 and j < len(T):
                result[j] = 1
                jobs[j] = T[i][0]
                max_profit += T[i][2]
                break
    print(jobs)
    return max_profit

# (numer zadania, deadline, zysk)
T = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]
time_limit = 3
print(job_sequencing(T, time_limit))