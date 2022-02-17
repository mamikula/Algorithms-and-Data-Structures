def universal_estuary(graph):
    i = j = 0
    while i < len(graph) and j < len(graph):
        if graph[i][j] == 1:
            i += 1
        else:
            j += 1
    i = min(i, j)
    for k in range(len(graph)):
        if graph[i][k] != 0:
            return False
        if graph[k][i] != 1 and k != i:
            return False
    return i


graph = [[0, 1, 0, 1, 1],
         [1, 0, 0, 0, 1],
         [0, 1, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [0, 0, 0, 1, 0]]

print(universal_estuary(graph))

from collections import deque

# def DFS(G, visited, n, v, start, parent):
#     visited[v] = True
#     if n == 0:
#         visited[v] = False
#         if start in G[v]:
#             while v != start:
#                 print(v, end = " ")
#                 v = parent[v]
#             print(start)
#             return True
#         else:
#             return#  False
#     for i in G[v]:
#         if not visit#ed[i]:
#             parent[i] = v
#             return DFS(G, visited, n - 1, i, start, parent)
#     visited[v] = False

# def findCycle(G, n):
#     V = len(G)
#     visited = [False] * V
#     parent = [-1 for _ in range(V)]
#     for i in range(V - (n - 1)):
#         if DFS(G, visited, n - 1, i, i, parent):
#             return True
#         visited[i] = True
#     return False

# G = [[1, 2, 3], [0, 2, 4], [1, 3], [0, 2, 4], [1, 3]]


# def cykl4(G):
# 	n = len(G)

# 	for i in range(n):
# 		for j in range(n):
# 			if i != j:
# 				cnt = 0
# 				vert = []
# 				for k in range(n):
# 					if G[i][k] == 1 and G[j][k] == 1:
# 						cnt += 1
# 						vert.append(k)
# 				    if cnt == 2:
# 					    vert.append(i)
# 					    vert.append(j)
# 					    return vert
# 	return None

# G = [
# 	[0,0,1,0,0,0],
# 	[0,0,1,0,0,0],
# 	[1,1,0,1,0,0],
# 	[0,0,1,0,1,0],
# 	[0,0,0,0,1,1],
# 	[0,0,0,0,1,0]
# 	]

# print(cykl4(G))

# def color(G):
#     T=[None for _ in range(len(G))]
#     return DFS(0,G,T,0,len(G))
# def DFS(v,G,T,last,n):
#     if T[v]==None:
#         T[v]=1-last
#     else:
#         if T[v]==last:
#             return False
#     for i in range(n):
#         if(G[v][i]==1):
#             G[v][i]=G[i][v]=0
#             if not DFS(i,G,T,1-last,n):
#                 return False
#     return True
# G=[[0,1,1],
#    [1,0,1],
#    [1,1,0]]
# print(color(G))
# G2=[[0,1,1,0],
#     [1,0,0,1],
#     [1,0,0,1],
#     [0,1,1,0]]
# print(color(G2))

# def uniwersalne_ujscie(G):
#     potencjalne = []
#     for u in range(len(G)):
#         findAllZeros = True
#         for v in range(len(G)):
#             if G[u][v] == 1:
#                 findAllZeros = False
#                 break

#         if findAllZeros == True:
#             potencjalne.append(u)

#     for u in potencjalne:
#         checkOnes =True
#         for v in range(len(G)):
#             if u != v:
#                 if G[v][u] == 0:
#                     checkOnes = False
#                     break

#         if checkOnes == True:
#             return u

#     return None

# G = [
#     [0,0,1,1,1],
#     [0,0,0,0,1],
#     [0,1,0,1,1],
#     [0,0,0,0,1],
#     [0,0,0,1,0]
# ]

# print(uniwersalne_ujscie(G))


# class Vertex:
#     def __init__(self, num):
#         self.num = num
#         self.color = 0
#         self.visited = False


# edges = [
#     [1, 2, 7], [0], [0], [5,9], [6], [3], [4, 8], [0, 9], [6], [3,7]
# ]


# def colorComponent(vertices, edges, s, c):
#     q = deque()
#     s.color = c
#     s.visited = True
#     q.append(s)
#     while len(q):
#         u = q.popleft()
#         for i in edges[u.num]:
#             v = vertices[i]
#             if not v.visited:
#                 v.visited = True
#                 v.color = c
#                 q.append(v)


# def countComponents(edges):
#     vertices = [Vertex(i) for i in range(len(edges))]
#     count = 0
#     for v in vertices:
#         if v.color == 0:
#             count += 1
#             colorComponent(vertices, edges, v, count)
#     r
e  # turn count

pri  # ### n(countComponents(edges))

d
#
de  # universal_estuary(graph):
#  i = j = 0
#  while i < len(graph) and j < len(graph):
#      if graph[i][j] == 1:
#          i += 1
#      else:
#          j += 1
#  for k in range(len(graph)):
#      if graph[i][k] != 0:
#          return False
#      if graph[k][i] != 1 and k != i:
#          return False
#  return i


gra  # ph = [[0, 1, 0, 1, 1],
#       [1, 0, 0, 0, 1],
#       [0, 1, 0, 0, 1],
#       [1, 0, 1, 0, 1],
#       [0, 0, 0, 1, 0]]
pri  # nt(universal_estuary(graph))ef unicversal_estuary(graph):
#  i = j = 0
#  while i < len(graph) and j < len(graph):
#      if graph[i][j] == 1:
#          i += 1
#      else:
#          j += 1
#  if i == len(graph):
:
# ro  #       return False
    for k in range(len(graph)):
#    if graph[i][k] != 0:
#        return False
#    if graph[k][i] != 1 and k != i:
#        return False
        return i

graph  # = [[0, 1, 0, 1, 1],
#     [1, 0, 0, 0, 1],
#     [0, 1, 0, 0, 1],
#     [1, 0, 1, 0, 1],
#     [0, 0, 0, 1, 0]]
print  # (unicversal_estuary(graph))


def zad_4(G, C, x, y):
    visited = [0] * len(G)

    q = Queue()
    q.put(x)

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if visited[v] == 0:
                visited[v] = C[u][v]
                q.put(v)
            elif visited[v] < C[u][v]:
                for p in G[v]:
                    if visited[p] == 0:
                        q.put(v)
                        visited[v] = C[u][v]
                        break
            if v == y and C[u][v] < visited[u]:
                return True


    return False




C = [[0,3,10,13,0,0],[0,0,0,0,0,5],[0,0,0,0,3,11],[0,0,12,0,0,0],[0,0,0,0,0,2],[0,0,0,0,0,0]]
print(zad_4(G,C,0,5))