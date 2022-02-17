from queue import PriorityQueue



def algo(graph, s, t):

    n = len(graph)
    Q = PriorityQueue()

    Q.put((0, s, [s]))


    while not Q.empty():
        tmp = Q.get()
        u = tmp[1]
        pw = tmp[0]
        res = tmp[2]

        if u == t:
            print(tmp)

        for v in range(n):
            if graph[u][v] != 0:
                if len(res) == 1:
                    pw = pw + graph[u][v]
                    Q.put((pw, v, res + [v]))
                else:
                    if graph[u][v] < graph[res[-2]][u]:
                        pw = pw + graph[u][v]
                        Q.put((pw, v, res + [v]))




G2 =[[0,1,5,0,0,0],
    [1,0,5,7,8,0],
    [5,5,0,0,3,2],
    [0,7,0,0,1,0],
    [0,8,3,1,0,0],
    [0,0,2,0,0,0]]

print(algo(G2, 4, 5))