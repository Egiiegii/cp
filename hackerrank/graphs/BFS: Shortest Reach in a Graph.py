from collections import defaultdict as dd
import queue


class Graph:
    def __init__(self, n):
        self.G = dd(list)
        self.node_number = n

    def connect(self, x, y):
        self.G[x].append(y)
        self.G[y].append(x)

    def find_all_distances(self, source):
        # dijkstra
        prev = [-1] * self.node_number
        visited = set()
        dist = [-1] * self.node_number
        q = queue.Queue()
        visited.add(source)
        dist[source] = 0

        q.put(source)

        while not q.empty():
            u = q.get()
            for v in self.G[u]:
                if v in visited:
                    continue
                dist[v] = dist[u] + 6
                prev[v] = u
                visited.add(v)
                q.put(v)
        dist.pop(source)
        print(" ".join(map(str, dist)))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
