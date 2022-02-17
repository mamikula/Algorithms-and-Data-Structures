#Marcin Mikuła


# Złożoność algorytmu O(V + E) o ile dwukrotnie wykonujemy BFS'a
#
# Algorytm polega na użyciu BFS. Najpierw przechodzimy BFS'em zaczynając od wierzchołka s.
# Szukamy t, więc gdy go znajdziemy, to przerywamy działanie BFS'a. Nalezy zliczać odległości.
# Zapisujemy rodziców z których przychodzimy. Jeżeli widzimy już
# odwiedzony wierzchołek (dostaliśmy się do niego z innego rodzica), i jeżeli ten wierzchołek
# jest w tej samej odległości od s (z tej samej fali BFS), to zapisujemy nowego
# rodzica do listy. Będzie on nam potrzebny dalej.
#
# Gdy nie znajdziemy t, to zwracamy None - nie ma ścieżki. Gdy znaleźliśmy, to:
#  - z wierzchołka t możemy wrócić do wierzchołka s wykorzystując zapisane listy parents
#  - możliwości powrotu jest dokładnie tyle samo, ile możliwych najkrótszych ścieżek z s do t.
#    Jest tak dlatego, że dodawaliśmy wierzchołek do parents, nawet jak był już odwiedzony, jeżeli odległości
#    się zgadzały.
#
# Wracając możemy zliczać ile jest różnych krawędzi na tych najkrótszych ścieżkach,
# po których możemy przejść z odległości k na k+1. Jeżeli jest tylko 1 krawędź, to znaleźliśmy krawędź, po
# usunięciu której najkrótsza ścieżka od s do t będzie dłuższa, dlatego, że ta
# krawędź będzie należeć do wszystkich najkrótszych ścieżek od s do t.
#
# Jeżeli ilość tych krawędzi będzie zawsze >= 2, to szukana krawędź nie istnieje i zwracamy None.

from collections import deque

INF = 1000



class Node:
    def __init__ (self, id):
        self.id = id
        self.visited = False
        self.parents = []
        self.out = []
        self.dist = INF


def enlarge(G, s, t):
    graph = [Node(i) for i in range(len(G))]

    for i, neighbors in enumerate(G):  # nie jestem pewien czy można
        for neigh in neighbors:
            graph[i].out.append(graph[neigh])

    queue = deque()
    queue.append(graph[s])
    graph[s].dist = 0
    graph[s].visited = True

    while len(queue) > 0:
        top = queue.popleft()
        if top.id == t:
            break

        new_dist = top.dist + 1
        for neigh in top.out:

            if neigh.dist < new_dist:
                continue
            elif neigh.dist == new_dist:
                neigh.parents.append(top)

            else:
                neigh.visited = True
                neigh.dist = new_dist
                neigh.parents.append(top)
                queue.append(neigh)

    if not graph[t].visited:
        return None
    queue.clear()

    for top in graph:
        top.visited = False
    queue.append(graph[t])

    curr_dist = graph[t].dist + 1
    while len(queue) > 0:
        curr_dist -= 1
        possible_paths = 0

        if curr_dist == 0:
            return None

        top = None
        while len(queue) > 0 and queue[0].dist == curr_dist:
            top = queue.popleft()
            possible_paths += len(top.parents)

            for parent in top.parents:
                if not parent.visited:
                    queue.append(parent)

        if possible_paths <= 1:
            return (min(top.id, top.parents[0].id), max(top.id, top.parents[0].id))

    return None




G1 = [ [1, 2],
       [0, 2],
       [0, 1] ] 
s1 = 0
t1 = 2
r1 = (0,2)


G2 = [ [1,4],  # 0
       [0,2],  # 1
       [1,3],  # 2
       [2,5],  # 3
       [0,5],  # 4
       [4,3]]  # 5
s2 = 0
t2 = 3
r2 = None

s3 = 0
t3 = 2
r3 = [(0,1),(1,2)]

G4 = [ [1,4,3],  # 0
       [0,2],    # 1
       [1,3],    # 2
       [2,5,0],  # 3
       [0,5],    # 4
       [4,3]]    # 5
s4 = 0
t4 = 2
r4 = None

        

TESTS = [(G1,s1,t1,r1),
         (G2,s2,t2,r2),
         (G2,s3,t3,r3),
         (G4,s4,t4,r4)
        ]



def runtests( f ):
  OK = True
  for (G,s,t,r) in TESTS:
    print("----------------------")
    print("G: ", G )
    print("s: ", s )    
    print("t: ", t )
    print("oczekiwany wynik: ", r)
    sol = f(G,s,t)
    print("uzyskany wynik  : ", sol)
    if not( (sol == r) or (sol in r) ):
      print("PROBLEM!!!!!!")
      OK = False
     
  print("----------------------")
  if not OK:
    print("PROBLEMY!")
  else:
    print("OK")

runtests(enlarge)