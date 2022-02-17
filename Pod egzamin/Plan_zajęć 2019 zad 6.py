from math import inf

def impatient_bob(T, k):
    T.sort(key = lambda T:T[1])
    n = len(T)
    dp = [[inf] * (k + 1) for _ in range(n)]

    for i in range(n):
        dp[i][1] = 0


    for i in range(n): #zadania
        for j in range(1, k + 1): #przerwy międzi iloma zadaniami
            for v in range(i): #poprzednicy
                if T[v][1] <= T[i][0]:
                    dp[i][j] = min(dp[v][j - 1] + T[i][0] - T[v][1], dp[i][j])

    for i in dp:
        print(i)

    best = inf
    for i in range(n):
        best = min(best, dp[i][k])

    return best

T = [(0, 1), (2, 4), (0, 5), (3, 6), (5, 7), (2, 9), (4, 10), (9, 11), (10, 12)]
print(impatient_bob(T, 5))