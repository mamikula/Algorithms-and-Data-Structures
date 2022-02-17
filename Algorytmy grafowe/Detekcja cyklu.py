def DFS(G, s):
    visited = [False] * len(G) #liczba wezlow, sposob zapisania rozmiaru tej atblicy zalezy od reprezentacji grafu
    parent = [None] * len(G)
    visited[s] = True
    return DFS_aux(G, s, visited, parent)


def DFS_aux(G, v, visited, parent):

    for u in G[v].neighbours:
        result = False
        if visited[u] and parent[u] != v:
            return True
        if not visited[u]:
            visited[u] = True
            parent[u] = v
            DFS_aux(G, u, visited, parent)
            result = result or DFS_aux(G, u, visited, parent)
            return result