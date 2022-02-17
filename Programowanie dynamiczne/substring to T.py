# (1) funckja
# f(i, s) - czy istnieje podciag sumujacy sie do s
# (2) sformulowanie rekurencyjne
# A:      1 3 4 1 2 11 5
# f(i, s) 1 0 1 1 1  1 1 1 1   1  1 1  ...
#     s:  1 2 3 4 5  6 7 9 10 11 12 13 ...
def printT(F):
    for i in range(len(F)):
        for j in range(len(F[i])):
            print(F[i][j], end=" ")
        print("\n")

def substring(A, T):
    n = len(A)
    dp = [[1] + [0] * T for _ in range(n)]

    if A[0] <= T:
        dp[0][A[0]] = 1

    for i in range(1, n):
        for s in range(1, T + 1):
            dp[i][s] = dp[i - 1][s]
            if A[i] <= s and dp[i][s] == 0:
                dp[i][s] = dp[i - 1][s - A[i]]
    printT(dp)
    return dp[n - 1][T]



#A = [5, 5, 5, 5]
A = [1, 2, 3, 4, 20]
T = 9
# for i in range(1, sum(A)):
#     print(substring(A, i), i)

print(substring(A, T))

