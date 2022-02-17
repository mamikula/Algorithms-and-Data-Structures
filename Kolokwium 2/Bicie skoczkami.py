# 1. Szachownica NxN, ustawiono pewną ilość skoczków. Opisać algorytm który sprawdzi czy jest
# możliwa sekwencja ruchów spełniająca:
# - każdy ruch kończy się zbiciem skoczka
# - sekwencja kończy się gdy zostanie jeden skoczek.

from queue import Queue

def possible(i, j, size):
    if i >= 0 and i < size and j >= 0 and j < size:
        return True
    return False


def makeGraph(chess):
    size = len(chess)
    horse = 0
    for i in range(size):
        for j in range(size):
            if chess[i][j] == 1:
                chess[i][j] = horse
                horse += 1
            else:
                chess[i][j] = -1

    jumps = [(1, -2), (1, 2), (2, -1), (2, 1)]
    graph = [[0]*horse for _ in range(horse)]

    for i in range(size):
        for j in range(size):
            if chess[i][j] != -1:
                for s in range(4):
                    x = i + jumps[s][0]
                    y = j + jumps[s][1]
                    if possible(x, y, size):
                        if chess[x][y] != -1:
                            graph[chess[i][j]][chess[x][y]] = 1
                            graph[chess[x][y]][chess[i][j]] = 1

    for i in graph:
        print(i)

    return graph


def remtop(graph, s):
    Q = Queue()
    visited = [False] * len(graph)
    order = []
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        order.append(u)
        for v in range(len(graph)):
            if graph[u][v] == 1 and visited[v] == False:
                visited[v] = True
                Q.put(v)

    order.reverse()
    print(order)


A = [[0, 0, 0, 1, 0, 0, 1, 0],
     [0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 1, 0]]


remtop(makeGraph(A), 0)