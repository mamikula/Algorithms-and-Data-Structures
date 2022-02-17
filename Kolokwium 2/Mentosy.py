
def mentosy(board):
    n = len(board)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    pref = [i for i in board]

    for i in range(n):
        dp[i][i] = board[i]
        if i > 0: pref[i] += pref[i - 1]

    print(pref)
    for l in range(2, n):
        for i in range(n - l):
            print(i, l)
            dp[i][i + l] = pref[i + l] - pref[i]
            dp[i][i + l] -= min(dp[i + 1][i + l], dp[i][i + l - 1])

    for i in dp:
        print(i)

    print(dp[0][n - 1])

#board = [2, 2, 4, 2, 5, 4, 4, 1, 1, 2]
#board = [2, 1, 1]
#board = [1, 4, 5, 6, 7, 3, 1]
mentosy(board)