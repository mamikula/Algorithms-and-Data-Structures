# Napisać funkcję: void sortString(string A[]); Funkcja sortuje tablicę n stringów różnej
# długości. Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.


def sortString(A):

    buckets = []

    for i in A:
        while len(i) >= len(buckets):
            buckets.append([])
        buckets[len(i)].append(i)

    for i in range(len(buckets) - 1, 0, -1):    #jaka dlugość
        k = i - 1  #która literka

        for j in range(1, len(buckets[i])): #słówko w jaderku
            while j > 0:
                if buckets[i][j][k] < buckets[i][j - 1][k]:
                    buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
                j -= 1

        buckets[i - 1] += buckets[i]
        del buckets[i]
        k -= 1
    buckets = buckets[0]
    return buckets

A =  ["ko", "paf", "jakub", "martyna", "marcin", "sebastian", "dominik"]
print(A)
A = sortString(A)
print(A)