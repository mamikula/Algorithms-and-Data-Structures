def tankowanie(S, Fuel):#S - polozenie stacji w odlegosci od miasta A-poczatkowego
    n = len(S)
    res = 0
    i = 0
    j = i + 1
    while True:

        if S[i] + Fuel < S[j]:
            print("nie da sie")
            return

        if S[i] + Fuel >= S[n - 1]:
            return res

        while S[i] + Fuel >= S[j]:
            j += 1

        i = j - 1
        res += 1


#S = [0, 10, 18, 60, 66, 100, 105]

# Fuel = 10
# S = [3, 7, 11, 15, 18, 24, 33, 38, 42]

#print(tankowanie(S, Fuel))


def tankowanieb(S, P, Fuel):
    #sprawdzamy stacje przedzialami, porownujemy koszty
    print(S)


    S = [0] + S
    P = [0] + P
    n = len(S) - 1
    cost = 0
    i = 0
    maxf = Fuel


    while True:
        j = i + 1
        best = P[i]
        best2 = 10000
        bid = i
        bid2 = 0


        if S[i] + maxf < S[j]:
            print("nie da sie")
            return

        while j <= n and maxf >= S[j] - S[i]:

            if best >= P[j]:
                best = P[j]
                bid = j

            elif best2 >= P[j]:
                best2 = P[j]
                bid2 = j
            j += 1


        if bid == i:
            cost += (maxf - Fuel)*P[i]
            Fuel = maxf - (S[bid2] - S[i])
            i = bid2


        else:
            if S[bid] - S[i] < Fuel:
                Fuel = Fuel - (S[bid] - S[i])
                i = bid
            else:
                cost += (S[bid] - S[i] - Fuel) * P[i]
                Fuel = 0
                i = bid

        if i == n:
            return cost


# Fuel = 10
# S = [3, 7, 11, 15, 18, 20, 24, 29, 31, 33, 36, 42, 45]
# P = [1.2, 2.1, 3.4, 5.2, 1.4, 4.20, 1.337, 2.115, 9.97, 6.9, 2.5, 2.021, 0]
#
# S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 21]
# P = [2, 1, 2, 3, 3, 1, 1, 3, 2, 2, 1, 2, 2, 3, 2, 3, 3, 1, 1, 2, 0]
# print(tankowanieb(S, P, Fuel))

def tankowaniec(S, P, Fuel, d):
    res = 100000
    n = len(S)
    t = [1000 for _ in range(n + 1)]
    t[0] = 0
    S = [0] + S
    P = [0] + P
    for i in range(1, n + 1):
        j = i - 1
        while j >= 0 and S[i] - S[j] <= Fuel:
            t[i] = min(t[i], t[j] + (S[i] - S[j])*P[i])
            j -= 1

    j = n
    while d - S[j] <= Fuel:
        res = min(res, t[j])
        j -= 1

    return (t, res)

#Fuel = 10
# S = [3, 7, 11, 15, 18, 20, 24, 29, 31, 33, 36, 42, 45]
# P = [1.2, 2.1, 3.4, 5.2, 1.4, 4.20, 1.337, 2.115, 9.97, 6.9, 2.5, 2.021, 0]
# S = [3, 7, 11, 15, 18, 20, 24, 29, 31, 35, 37, 42, 45]
# P = [1.2, 2.1, 3.4, 5.2, 1.4, 4.20, 1.337, 2.115, 9.97, 2.6, 2.5, 2.02, 0]
# S = [8, 11, 15, 16, 23]
# P = [40, 7, 15, 12, 0]
Fuel = 14
S = [1, 9, 15, 16, 17, 27, 28]
P = [1, 100, 10, 15, 1, 30, 30]
d = 30

print(tankowaniec(S, P, Fuel, d))