from collections import defaultdict


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return c_lib*n

    visited = set()
    graph = defaultdict(list)
    component = []
    for f, t in cities:
        graph[f].append(t)
        graph[t].append(f)

    def dfs(visited, graph, i):
        visited.add(i)
        for j in graph[i]:
            if j not in visited:
                dfs(visited, graph, j)
        return True
    for i in range(1, n+1):
        if i not in visited:
            component.append(dfs(visited, graph, i))
    return len(component)*c_lib + c_road*(n-len(component))
