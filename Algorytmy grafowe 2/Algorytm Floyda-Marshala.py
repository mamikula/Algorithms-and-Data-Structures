from math import inf

G=[[0,1,0,0,0,1],
   [1,0,1,0,0,1],
   [0,1,0,1,0,1],
   [0,0,1,0,1,0],
   [0,0,0,1,0,1],
   [1,1,1,0,1,0]]

S=[[0,4,0,0,0,3],
   [4,0,2,0,0,4],
   [0,2,0,4,0,2],
   [0,0,4,0,5,0],
   [0,0,0,5,0,7],
   [3,4,2,0,7,0]]

for i in range(len(S)):
    for j in range(len(S)):
        if S[i][j] == 0:
            S[i][j] = inf

def FM(G, S):
    n = len(G)
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if u != v:
                    S[u][v] = min(S[u][v], S[u][t] + S[t][v])

    for i in S:
        print(i)

FM(G, S)