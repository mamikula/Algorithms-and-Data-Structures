def binary_index(Arr,l,r,k,last=None):
    if l>r:
        return last
    half = (l+r)//2
    if Arr[half] < k:
        return binary_index(Arr,half+1,r,k,last)
    else:
        return binary_index(Arr,l,half-1,k,half)


def LIS(Arr):
    n = len(Arr)
    A = [None] * n
    if len(Arr) == 0:
        return 0
    A[0] = Arr[0]
    l = 1
    for i in range(1,n):
        k = Arr[i]
        if k < A[0]:
            A[0] = k
        elif k > A[l-1]:
            A[l] = k
            l += 1
            res = A[:l]
        else:
            A[binary_index(A,0,l-1,k)] = k
    return l, res


A = [0,8,4,12,2,10,12,7]
# [0] -> 1
# [0,8] -> 2
# [0,4] -> 2
# [0,4,12] -> 3
# [0,2,12,14] -> 3
# [0,2,10,14] -> 3
print(LIS(A))