def knapsack3d(W, M, Hs, MaxM, MaxH):
    n = len(W)

    #dp = [[[0] * n for _ in range(MaxM + 1)] * (MaxH + 1) for __ in range(MaxH + 1)]
    dp = [[[0 for _ in range(MaxH + 1)] for _ in range(MaxM + 1)] for _ in range(n)]
    if M[0] < MaxM and Hs[0] < MaxH:
        for i in range(M[0], MaxM + 1):
            for j in range(Hs[0], MaxH + 1):
                dp[0][i][j] = W[0]



    for i in range(1, n):
        for m in range(1, MaxM + 1):
            for h in range(1, MaxH + 1):

                dp[i][m][h] = dp[i - 1][m][h]
                if m >= M[i] and h >= Hs[i]:
                    dp[i][m][h] = max(dp[i - 1][m][h], dp[i - 1][m - M[i]][h - Hs[i]] + W[i])


    #print(dp[n - 1][MaxM][MaxH])
    print(getsolution(dp, W, M, Hs, n - 1, MaxM, MaxH))
    return dp[n - 1][MaxM][MaxH]

def getsolution(dp, W, M, H, i, m, h):
    if i < 0: return []
    if i == 0:
        if m >= M[0] and h >= H[0]: return [0]
        return []

    if m >= M[i] and h >= H[i] and  dp[i][m][h] == dp[i - 1][m - M[i]][h - H[i]] + W[i]:
        return getsolution(dp, W, M, H, i - 1, m - M[i], h - H[i]) + [i]
    return getsolution(dp, W, M, H, i - 1, m, h)


W = [2,6,7,3,5,4,2,6,4]
M = [3,9,9,7,2,2,1,2,3]
H = [1,7,6,2,4,1,3,6,2]
print(knapsack3d(W, M, H, 25, 16))