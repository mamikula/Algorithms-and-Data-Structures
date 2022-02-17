from math import inf

def zbigniew(A):
    n = len(A)
    dp = [[inf]*n for _ in range(n)]
    if A[0] != 0:
        dp[0][A[0]] = 0

    for i in range(0, n):
        for y in range(n):
            if dp[i][y] != inf:
                for v in range(1, y + 1):
                    if i + v < n and y - v + A[i + v] < n:
                        dp[i + v][y - v + A[i + v]] = min(dp[i + v][y - v + A[i + v]], dp[i][y] + 1)

    for i in dp:
        print(i)

    return min(dp[n - 1])

A = [2, 2, 1, 0, 0, 0]
B = [4, 5, 2, 4, 1, 2, 1, 0]
print(zbigniew(A))

print(zbigniew(B))