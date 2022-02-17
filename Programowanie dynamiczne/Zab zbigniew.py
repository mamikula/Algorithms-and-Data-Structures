
def zbyslaw(A):
    n = len(A)
    inf = 100
    res = [[inf] * n for _ in range(n)]


    for i in range(A[0]):
        res[0][i] = 0


    for i in range(n):
        for j in range(1, n):

            if res[i][j] == inf: continue

            for k in range(j):

                if i + k >= n: continue
                if j - k + A[i + k] >= n: continue
                res[i + k][j - k + A[i + k]] = min(res[i][j] + 1, res[i + k][j - k + A[i + k]])



    odp = 100
    for i in res:
        print(i)


    for i in range(n):
        odp = min(odp, res[i][n - 1])

    return res[n - 1][n - 1]

#A = [2, 1, 3, 2, 5, 1, 6, 0]
#A=[3,1,0,2,1,2,0,2,1,7,1,1,1,1,1,1,0]
#A = [2, 2, 1, 0, 0, 0]
A = [2, 0, 0, 0]
#A = [4, 5, 2, 4, 1, 2, 1, 0]
print(zbyslaw(A))