# Far Vertices

**Difficulty:** Hard  
**Topics:** N/A  
**HackerRank URL:** [Far Vertices](https://www.hackerrank.com/challenges/far-vertices/problem)

## Problem Description

You are given a tree that has N vertices and N-1 edges. Your task is to mark as small number of vertices as possible, such that, the maximum distance between two unmarked vertices is less than or equal to K. Output this value.
Distance between two vertices i and j is defined as the minimum number of edges you have to pass in order to reach vertex i from vertex j.

**Input Format** **
The first line of input contains two integers N and K. The next N-1 lines contain two integers (ui,vi) each, where 1 <= ui,vi <= N. Each of these lines specifies an edge.

N is no more than 100. K is less than N.

Output Format** **
Print an integer that denotes the result of the test.

Sample Input:**

```
5 1
1 2
1 3
1 4
1 5

```

**Sample Output:**

```
3

```

**Sample Input:**

```
5 2
1 2
1 3
1 4
1 5

```

**Sample Output:**

```
0

```

**Explanation:**

In the first case you have to mark at least 3 vertices, and in the second case you don't need to mark any vertices.

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Far Vertices
# Link: https://www.hackerrank.com/challenges/far-vertices/problem
# Difficulty: Hard
# Language: python3

from collections import deque

n, k = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())

    u -= 1
    v -= 1

    graph[u].append(v)
    graph[v].append(u)


def distance_from(start):
    dist = [-1] * n
    dist[start] = 0

    q = deque([start])

    while q:
        node = q.popleft()

        for neighbour in graph[node]:
            if dist[neighbour] == -1:
                dist[neighbour] = dist[node] + 1
                q.append(neighbour)

    return dist


distances = []

for i in range(n):
    distances.append(distance_from(i))


maximum_unmarked = 0

if k % 2 == 0:

    radius = k // 2

    for center in range(n):
        count = 0

        for node in range(n):
            if distances[center][node] <= radius:
                count += 1

        maximum_unmarked = max(maximum_unmarked, count)

else:

    radius = k // 2

    for u in range(n):

        for v in graph[u]:

            if u < v:

                count = 0

                for node in range(n):
                    if min(distances[u][node],
                           distances[v][node]) <= radius:
                        count += 1

                maximum_unmarked = max(maximum_unmarked, count)


print(n - maximum_unmarked)

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
