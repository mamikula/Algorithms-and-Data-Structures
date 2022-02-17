#Marcin Mikuła
from zad2testy import runtests
from queue import PriorityQueue


class Vertex:
    def __init__ (self, id, neighbours = []):
        self.id = id
        self.neighbours = neighbours  # tuples
        self.dist = 1 << 30
        self.parent = None

    def add_neigh (self, neigh):
        self.neighbours.append(neigh)

    def __lt__ (self, other):
        return self.dist < other.dist

    def __eq__ (self, other):
        return self.dist == other.dist


def relax (A, B, dist):
    if B.dist > A.dist + dist:
        B.dist = A.dist + dist
        return False
    return True


def dijkstra (A, B):
    A.dist = 0

    queue = PriorityQueue()
    queue.put(A)

    while not queue.empty():
        vert = queue.get()

        if vert == B: return vert.dist

        for neigh, dist in vert.neighbours:
            if relax(vert, neigh, dist): continue

            queue.put(neigh)
            neigh.parent = vert

    return 1 << 30


def calc_dist (i, it):
    if abs(i - it) == 1:
        return 60
    else:
        return 105 + (abs(i - it) - 2) * 30


def robot (L, A, B):
    n = len(L)
    m = len(L[0])

    graph = [[{'right': Vertex((i * n + j) * 4), 'left': Vertex((i * n + j) * 4 + 2),
               'up': Vertex((i * n + j) * 4 + 1), 'down': Vertex((i * n + j) * 4 + 3)}
              for j in range(m)]
             for i in range(n)]

    for i in range(n):
        for j in range(m):
            if L[i][j] == 'X': continue

            for fr in ['right', 'left', 'up', 'down']:
                for to in ['right', 'left', 'up', 'down']:
                    if fr == to: continue

                    if abs(graph[i][j][fr].id - graph[i][j][to].id) != 2:
                        graph[i][j][fr].add_neigh((graph[i][j][to], 45))
                    else:  # difference 2 in ids is only for pairs ('down', 'up') and ('right', 'left')
                        graph[i][j][fr].add_neigh((graph[i][j][to], 90))

            print(graph[1][1]['right'].neighbours)

            jt = j + 1
            while L[i][jt] != 'X':
                graph[i][j]['right'].add_neigh((graph[i][jt]['right'], calc_dist(j, jt)))
                jt += 1

            jt = j - 1
            while L[i][jt] != 'X':
                graph[i][j]['left'].add_neigh((graph[i][jt]['left'], calc_dist(j, jt)))
                jt -= 1

            it = i + 1
            while L[i][jt] != 'X':
                graph[i][j]['down'].add_neigh((graph[it][j]['down'], calc_dist(i, it)))
                it += 1

            it = i - 1
            while L[i][jt] != 'X':
                graph[i][j]['up'].add_neigh((graph[it][j]['up'], calc_dist(i, it)))
                it -= 1

    # print(graph[A[1]][A[0]]['right'].neighbours)
    # print(graph[1][1]['down'].neighbours)

    return min(dijkstra(graph[A[1]][A[0]]['right'], graph[B[1]][B[0]]['left']),
               dijkstra(graph[A[1]][A[0]]['right'], graph[B[1]][B[0]]['right']),
               dijkstra(graph[A[1]][A[0]]['right'], graph[B[1]][B[0]]['up']),
               dijkstra(graph[A[1]][A[0]]['right'], graph[B[1]][B[0]]['down']))


runtests(robot)