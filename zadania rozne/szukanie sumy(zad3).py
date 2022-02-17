tab = [1, 5, 8]
x = 10
def zad2cw2(tab, x):
    i = 0
    j = len(tab) - 1

    while i <= j:
        sum = tab[i] + tab[j]
        if sum < x:
            i += 1
        if sum > x:
            j -= 1
        if sum == x:
            return True

    return False

print(zad2cw2(tab, x))