from queue import Queue

class Node:
    def __init__(self):
        self.nbs = []
        self.d = -1
        self.parent = None

#
# graph = [[0, 1, 1, 0, 0, 0, 0, 0],
#          [1, 0, 0, 0, 1, 0, 0, 0],
#          [1, 0, 0, 1, 0, 1, 0, 0],
#          [0, 0, 1, 0, 1, 0, 0, 0],
#          [0, 1, 0, 1, 0, 1, 0, 0],
#          [0, 0, 1, 0, 1, 0, 1, 0],
#          [0, 0, 0, 0, 0, 1, 0, 1],
#          [0, 0, 0, 0, 0, 0, 1, 0]
#          ]
# s = 0

def BFS2(graph, s):
    Q = Queue()
    visited = [False]*len(graph)
    parent = [None]*len(graph)
    d = [-1]*len(graph)
    d[s] = 0
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in range(len(graph[u])):
            if graph[u][v] == 1 and visited[v] == False:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.put(v)

    print(visited)
    print(parent)
    print(d)

# BFS2(graph, s)



# graph = [[1, 2],
#          [0, 4],
#          [0, 3, 5],
#          [2, 4],
#          [1, 3, 5],
#          [2, 4, 6],
#          [5, 7],
#          [6]
#          ]
# s = 0


### implementacja krawedziowa
def BFS3(graph, s):
    Q = Queue()
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    d = [-1] * len(graph)
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

    print(visited)
    print(parent)
    print(d)
#BFS3(graph, s)



def graphDwudzielny(graph, s):
    Q = Queue()
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    d = [-1] * len(graph)
    colors = [0]*len((graph))
    d[s] = 0
    visited[s] = True
    Q.put(s)
    colors[s] = -1
    while not Q.empty():
        u = Q.get()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                colors[v] = -colors[u]
                Q.put(v)
            elif visited[v] == True and colors[v] == colors[u]:
                print(colors)
                return False


    print(visited)
    print(parent)
    print(d)
    print(colors)
    return True

graph = [[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]

# graph = [[1, 2],
#          [0, 4],
#          [0, 3, 5],
#          [2, 4],
#          [1, 3, 5],
#          [2, 4, 6],
#          [5, 7],
#          [6]
#          ]
s = 0
print(graphDwudzielny(graph, s))

# tablica krawedzi:
# [[0, 3], [2, 4], [4, 3], [4, 2], [3, 4], [3, 0], [5, 1], [5, 0], [1, 5], [0, 5], [6, 1], [6, 0], [0, 6], [1, 6], [6, 4], [4, 6]]
# macierz:
# [[0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0]]
# sasiedztwo:
# [[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]