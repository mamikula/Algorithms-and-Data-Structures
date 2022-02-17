#Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
#O(n), który stwierdza, czy istnieje liczba x (tzw. lider A),
#która występuje w A na ponad połowie pozycji.


def lider(tab):
    cnt = 1
    a = tab[0]
    for i in range(1,len(tab)):
        if a == tab[i]:
            cnt += 1
        else:
            if cnt != 0:
                cnt -= 1
            else:
                a = tab[i]
                cnt = 1

    cnt = 0
    for i in range(len(tab)):
        if tab[i] == a:
            cnt += 1

    print(a)
    if cnt > len(tab)//2:
        return True
    return False
#tab = [1, 1, 2, 2, 2, 1, 1, 1]
#tab = [1, 2, 1, 2, 1]
#tab = [1, 2, 1, 3, 1, 2, 1, 2, 2, 2, 2]
tab = [2, 2, 2, 2, 1, 1, 1, 1, 1]
print(lider(tab))