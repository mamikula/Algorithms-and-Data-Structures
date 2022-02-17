def knapsackmin(W, C, maxw, cmin):
    n = len(W)
    suma = sum(C)
    dp = [[[0 for _ in range(cmin + 1)] for _ in range(maxw + 1)] for _ in range(n)]

    if C[0] <= cmin and W[0] <= maxw:
        for i in range(W[0], maxw + 1):
            for j in range(C[0] + 1):
                    dp[0][i][j] = 1

    for i in range(1, n):
        for w in range(maxw + 1):
            dp[i][w][0] = dp[i - 1][w][0]
            if w >= W[i]:
                dp[i][w][0] = dp[i - 1][w - W[i]][0] + 1


    for i in range(0, n):
        for w in range(1, maxw + 1):
            for c in range(1, cmin + 1):
                if c + C[i] > cmin and w + W[i] <= maxw:
                    dp[i][w][c] = dp[i - 1][w][c] + 1
                elif w + W[i] <= maxw:
                    dp[i][w][c] = dp[i - 1][w][c] + dp[i - 1][w - W[i]][c - C[i]]

    print(dp[n - 1][maxw][cmin])


# W = [4, 9, 3, 1, 8, 8, 7, 8, 2]
# C = [2, 4, 1, 1, 7, 1, 6, 8, 2]
# W = [4, 4]
# C = [3, 1]
W = [1, 2, 3]
C = [2, 1, 3]
knapsackmin(W, C, 3, 2)

