
import queue
from math import inf
class Vertex:
    def __init__(self):
        self.parent=[]
        self.d=inf

e=0
def res(vertices, E, t):
    global e
    if vertices[t].parent==[]: return True

    for i in vertices[t].parent:
        if E[t][i]==0 or E[i][t]==0:
            E[t][i]=1
            E[i][t]=1
            e+=1
            res(vertices, E, i)


def dijkstra(G,s,t):
    n=len(G)
    E=[[0]*n for _ in range(n)]
    vertices=[]
    q=queue.PriorityQueue()
    for i in range(len(G)):
        vertices.append(Vertex())
    vertices[s].d = 0
    q.put((vertices[s].d,s))

    vertices[s].d=0
    while not q.empty():
        u=q.get()[1]
        for i in G[u]:
            if vertices[i[0]].d > vertices[u].d + i[1]:
                vertices[i[0]].d = vertices[u].d + i[1]
                vertices[i[0]].parent = [u]
                q.put((vertices[i[0]].d, i[0]))
            elif vertices[i[0]].d == vertices[u].d + i[1]:
                vertices[i[0]].parent.append(u)
                q.put((vertices[i[0]].d, i[0]))

    # for i in range(len(G)):
    #     print(i,vertices[i].parent)

    res(vertices, E, t)
    #print(e)
    return e

# G = [ [(1,2),(2,4)],
# [(0,2),(3,11),(4,3)],
# [(0,4),(3,13)], # itd.
# [(1,11),(2,13),(5,17),(6,1)],
# [(1,3),(5,5)],
# [(3,17),(4,5),(7,7)],
# [(3,1),(7,3)],
# [(5,7),(6,3)] ]
# s=0
# t=7


G2 = [ [(1,2),(2,4)],
      [(0,2),(3,11),(4,3)],
      [(0,4),(3,13)],
      [(1,11),(2,13),(5,17),(6,1)],
      [(1,3),(5,5)],
      [(3,17),(4,5),(7,7)],
      [(3,1),(7,3)],
      [(5,7),(6,3),] ]
s2 = 4
t2= 6

print(dijkstra(G2,s2,t2))