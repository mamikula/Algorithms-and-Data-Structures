
def blocksy(kords):
    n = len(kords)
    res = [1] * n

    for i in range(n):
        for j in range(i):
            if kords[j][0] <= kords[i][0] and kords[j][1] >= kords[i][1] and res[j] + 1 > res[i]:
                res[i] = res[j] + 1

    print(res)
    #return n - max(res)
    return(max(res))




A=[(1,4),(2,3),(1,99),(2,4),(1,4),(2,9),(3,8),(4,11),(4,7),(9,12)]
B = [(1, 4), (0, 5), (1, 5), (2, 6), (2, 4)]
C = [(10, 15), (8, 14), (1, 6), (3, 10), (8, 11), (6, 15)]
print(blocksy(C))