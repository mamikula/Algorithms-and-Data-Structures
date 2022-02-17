A = [(1, 2), (2, 5), (5, 7), (5, 6), (2, 3), (3, 7), (7, 9), (9, 11), (2, 9), (9, 10), (10, 69)]
A.sort(key = lambda A:A[0])
print(A)

def maciek(A):

    graph = [[0 for _ in range(len(A))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][1] == A[j][0] and i != j:
                graph[i][j] = 1


    for i in graph:
        print(i)
    return graph


def DFSmatrix(graph, a, b):
    n = len(graph)
    visited = [None]*n


    def DFSVisit(graph, u, visited, a, b ):
        visited[u] = True
        print(A[u])
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] == 1:
                visited[v] = True
                if A[u][1] == b:
                    print(A[u][1])
                    return True

                return DFSVisit(graph, v, visited, a, b)

        return False

    for u in range(n):
        if not visited[u]:
            if DFSVisit(graph, u, visited,a, b):
                return True

    return False


print(DFSmatrix(maciek(A), 1, 11))
