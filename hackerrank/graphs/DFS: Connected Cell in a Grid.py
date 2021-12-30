#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#
def maxRegion(grid):
    # Write your code here
    visited = set()

    def get_adjacent(t):
        x = t[0]
        y = t[1]
        adj = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
               (x - 1, y),                 (x + 1, y),
               (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
        return list(filter(lambda t: 0 <= t[0] < n and 0 <= t[1] < m, adj))

    def dfs(y, x):
        visited.add((y, x))
        summary = []
        for (i, j) in get_adjacent((y, x)):
            if (i, j) not in visited and grid[i][j] == 1:
                summary.append(dfs(i, j) + 1)
            else:
                summary.append(0)
        return sum(summary)

    ans = []
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and grid[i][j] == 1:
                ans.append(dfs(i, j) + 1)
            else:
                ans.append(0)
    return max(ans)


if __name__ == '__main__':

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    print(res)
