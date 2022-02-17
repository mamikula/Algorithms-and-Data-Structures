from queue import Queue


def remtop(graph, s):
    Q = Queue()
    visited = [False] * len(graph)
    #parent = [None] * len(graph)
    order = []
    #d = [-1] * len(graph)
    #d[s] = 0
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        #order.append(u)
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                #d[v] = d[u] + 1
                #parent[v] = u
                Q.put(v)
                #order.append(u)

    #order.reverse()
    print(order)
    #print(visited)
    #print(parent)
    #print(d)



graph = [[1, 2],
         [0, 2],
         [0, 1, 3],
         [2, 4, 5, 6, 7, 8],
         [3],
         [3],
         [3, 7],
         [6, 3, 9],
         [3, 9,],
         [7, 8]
         ]
s = 7

graph2 = [[8],
          [8],
          [9],
          [9],
          [10],
          [10],
          [11],
          [11],
          [0, 1, 12],
          [2, 3, 12],
          [4, 5, 13],
          [6, 7, 14],
          [8, 9, 13],
          [12, 10, 14],
          [13, 11]
          ]



remtop(graph, s)


