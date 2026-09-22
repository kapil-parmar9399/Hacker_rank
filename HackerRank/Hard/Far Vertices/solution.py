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
