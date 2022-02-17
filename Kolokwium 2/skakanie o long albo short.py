# struct field {
# int value;
# int long j;
# int short j;
# };
# Z każdego pola można skakać tylko o ilość pól zapisaną w long j lub short j. Napisać program
# który zwróci maksymalną wartość jaką możemy osiągnąć poprzez przejście z pola 0 do n-1.
# Można założyć że z każdego pola da się dojść do pola n-1.
class field:
    def __init__ (self, value, short, long):
        self.value = value
        self.long = short
        self.short = long

A = []
A.append(field(5, 2, 3))
A.append(field(1, 1,2))
A.append(field(3, 2, 4))
A.append(field(6, 2, 6))
A.append(field(1, 1, 2))
A.append(field(4, 4, 4))
A.append(field(3, 1, 3))
A.append(field(1, 2, 4))
A.append(field(5, 4, 6))
A.append(field(1, 1, 2))
A.append(field(0, 0, 0))

def fun(A):
    n = len(A)
    res = [0]*n
    res[0] = A[0].value

    for i in range(0, n):
        if i + A[i].long < n:
            res[i + A[i].long] = max(res[i + A[i].long], res[i] + A[i + A[i].long].value )
        if i + A[i].short < n:
            res[i + A[i].short] = max(res[i + A[i].short], res[i] + A[i + A[i].short].value)

    print(res)
    return res[n - 1]



print(fun(A))