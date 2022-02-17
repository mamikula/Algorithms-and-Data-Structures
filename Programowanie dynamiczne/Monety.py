#definicja funkcji  - czy i-ta kwote da sie obliczyc zapomoca danego zestawu monet, jezeli tak, to jaka jest minimalna liczba monet do odliczenia danej kwoty


def piniondz(monets, kwota):
    n = len(monets)
    res = [[1000] * (kwota + 1) for _ in range(n)]


    for i in range(kwota + 1):
        if i % monets[0] == 0:
            res[0][i] = i // monets[0]

    for i in range(n):
        res[i][0] = 0




    for i in range(1, n):
        for j in range(1, kwota + 1):
            res[i][j] = min(res[i][j - monets[i]] + 1, res[i - 1][j])

    for i in res:
        print(i)

    return res[n - 1][kwota]

monets = [1, 5, 8]
kwota = 15

print(piniondz(monets, kwota))