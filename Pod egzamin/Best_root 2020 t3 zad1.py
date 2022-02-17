from queue import Queue

def BFS(graph, s):
    n = len(graph)
    Q = Queue()
    visited = [False] * n
    parent = [None] * n
    d = [-1] * n
    d[s] = 0
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.put(v)

    node = -1
    maxd = 0
    for i in range(n):
        if d[i] > maxd:
            maxd = d[i]
            node = i

    return (node, parent, maxd//2)


def best_root(L):

    node = BFS(L, 0)[0]
    res = BFS(L, node)
    parent = res[1]
    top = res[0]
    for i in range(res[2]):
        top = parent[top]

    print(top)

L = [[2],
     [2],
     [0, 1, 3],
     [2, 4],
     [3, 5, 6],
     [4, 7],
     [4],
     [5]]

best_root(L)
