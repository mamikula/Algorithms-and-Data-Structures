B = [(0,0.2), (0.25, 0.45), (0.4,0.9), (0.8,1)]
C = [(0, 0.15), (0.1, 0.25), (0.05, 0.4), (0.35, 0.6), (0.75, 0.85), (0.15, 0.3), (0.35, 0.7), (0, 0.25), (0.65, 0.95), (0.55, 0.8)]
A = [(0, 0.15), (0.1, 0.25), (0.05, 0.4), (0.35, 0.6), (0.75, 0.85), (0.15, 0.3), (0.35, 0.7), (0, 0.25), (0.65, 0.95),
     (0.85, 1), (0.55, 0.8), (0.95, 1)]


def segments(A):
    A.sort(key = lambda A: A[0])
    n = len(A)

    i = 0
    res = []
    best = 0
    last = 0
    idx = 0
    while i < n:
        while i < n and last >= A[i][0]:
            if A[i][1] > best:
                best = A[i][1]
                idx = i
            i += 1

        if best == last:
            return None

        last = best
        res.append(A[idx])
        if best == 1:
            return res



print(segments(A))