
def tasks(T, ddl, profit):
    if ddl == -1:
        return profit

    i = len(T) - 1
    while i >= 0 and T[i][1] != ddl:
        i -= 1

    maks = 0
    while i >= 0 and T[i][1] == ddl:
        maks = max(maks, T[i][0])
        i -= 1

    return tasks(T, ddl - 1, profit + maks)



def taski(T):
    profit = 0
    maks = 0
    ddl = T[0][1]
    i = 0
    while i < len(T):
        if ddl != T[i][1]:
            ddl = T[i][1]
            profit += maks
            maks = 0
            i = i - 1
        else:
            maks = max(maks, T[i][0])
        i += 1

    profit += maks
    return profit


T = [(1, 1), (1, 3), (2, 5), (2, 6), (3, 1), (2, 2), (2, 6)] #(zysk, czas)
T.sort(key = lambda T :  T[1])
print(T)
print(tasks(T, 7, 0))
print(taski(T))