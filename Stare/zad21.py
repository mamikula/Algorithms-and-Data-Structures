#Marcin Mikuła


# Złożoność algorytmu O(V + E) o ile dwukrotnie wykonujemy BFS'a
#
# Algorytm polega na użyciu BFS. Najpierw przechodzimy BFS'em zaczynając od wierzchołka s.
# Szukamy t, więc gdy go znajdziemy, to przerywamy działanie BFS'a. Ważnym elementem jest
# liczenie odległości. Zapisujemy rodziców z których przechodzimy. Jeżeli widzimy już
# odwiedzony wierzchołek (dostaliśmy się do niego z innego rodzica), i jeżeli ten wierzchołek
# jest na takiej samej odległości od s przechodząc przez wszystkich rodziców, to zapisujemy nowego
# rodzica do listy. Będzie on nam potrzebny dalej.
#
# Gdy nie znajdziemy t, to zwracamy None - nie ma ścieżki. Gdy znaleźliśmy, to:
#  - z wierzchołka t możemy wrócić do wierzchołka s wykorzystując zapisane listy parents
#  - możliwości powrotu jest dokładnie tyle samo, ile możliwych najkrótszych ścieżek z s do t.
#    Jest tak dlatego, że dodawaliśmy wierzchołek do parents, nawet jak był już odwiedzony, byle by odległości
#    się zgadzały.
#
# Otóż, w tej chwili wracając możemy zliczać ile jest różnych krawędzi na tych najkrótszych ścieżkach,
# po których możemy przejść z odległości k na k+1. Jeżeli jest tylko 1 krawędź, to znaleźliśmy krawędź, po
# usunięciu której najmniejsza ścieżka od s do t będzie dłuższa, niż pierwotnie. Jest to dlatego, że ta
# krawędź będzie należyć do wszystkich najkrótszych ścieżek od s do t.
#
# Natomiast, jeżeli zawsze ta ilość będzie >= 2, to szukanej krawędzi nie istnieje i zwracamy None.


from collections import deque


INF = 1000

#Dzięki wskaźnikom łatwiej przechowywać listy sąsiadów
class Node:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.parents = []
        self.out = []
        self.dist = INF


def enlarge(G, s, t):
    graph = [Node(i) for i in range(len(G))]

    for i, neighbors in enumerate(G): #nie jestem pewien czy można
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

runtests( enlarge ) 
