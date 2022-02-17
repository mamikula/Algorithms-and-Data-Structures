# Dana jest tablica punktów (structy z intami x, y). Punkt 1 dominuje 2 gdy x1 > x2 i y1 > y2.
# Zaimplementuj algorytm znajdujący liczność najmniejszego zbioru, takiego że wybrane punkty dominują
# wszystkie niewybrane. W 1-2 zdaniach opisz jego działanie i oszacuj złożoność obliczeniową.



#Wybieramy 2 punkty: o największej współrzędnej x1 i (2) o największej współrzędnej y1. Dołączamy te
# punkty do zbioru dominującego. Z wybranych punktów tworzymy nowy o wspólrzędnych X2 - (współrzędna x punktu z y1),
# Y2 (współrzędna y puntku z x1). Ponieważ punkty zawierające x1 i y1 nie mogą być zdominowane ponieważ są największe w zbiorze
# na tych współrzędnych, do zbioru dominującego musimy dołączyć wszystkie punkty które mają wsp. x = x1 lub x >= x2 oraz y = y1 lub y >= y2,
# otrzymany zbiór jest najmniej licznym zbiorem dominującym

T = [(1, 3), (0, 5), (2, 10), (5, 6), (7, 8)]


def dominujace(T):
    n = len(T)
    x1 = -1
    y1= -1
    x2 = -1
    y2 = -1
    res = []

    for i in range(n):
        if x1 < T[i][0]:
            x1 = T[i][0]
            y2 = T[i][1]
        if y1 < T[i][1]:
            y1 = T[i][1]
            x2 = T[i][0]

    for i in range(n):
        if T[i][0] == x1 or T[i][0] >= x2:
            res.append(T[i])
        elif T[i][1] == y1 or T[i][1] >= y2:
            res.append(T[i])

    return res

print(dominujace(T))