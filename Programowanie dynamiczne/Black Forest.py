
def blackForest(profit):
    n = len(profit)
    res = [0]*n
    res[0] = profit[0]
    res[1] = profit[1]

    for i in range(2, n):
        res[i] = max(res[j] + profit[i] for j in range(0, i - 1))

    print(res)
    return res[n - 1]


profit = [5, 2 , 4, 8, 11, 3, 1, 1]
print(blackForest(profit))