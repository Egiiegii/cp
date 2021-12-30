#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict as dd
import queue
# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    graph = dd(list)
    for f, t in zip(graph_from, graph_to):
        graph[f].append(t)
        graph[t].append(f)
    target_ids = []
    for idx, _id in enumerate(ids, 1):
        if _id == val:
            target_ids.append(idx)

    def dijkstra(source):
        q = queue.Queue()
        visited = set()

        dist = [float('inf')] * (graph_nodes + 1)
        prev = [-1] * (graph_nodes + 1)

        q.put(item=source)
        visited.add(source)
        dist[source] = 0

        while not q.empty():
            u = q.get()
            for v in graph[u]:
                if v in visited:
                    continue
                if ids[v-1] == val:
                    return dist[u] + 1
                else:
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    q.put(v)
                    visited.add(v)
        return -1

    costs = []
    for target_id in target_ids:
        costs.append(dijkstra(target_id))
    plus_costs = list(filter(lambda x: x>=0, costs))
    if len(plus_costs) > 0:
        return min(plus_costs)
    else:
        return -1

if __name__ == '__main__':

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    print(ans)

