# HackerRank Problem: Problem solving
# Link: https://www.hackerrank.com/challenges/problem-solving/problem
# Difficulty: Hard
# Language: python3

def dfs(u, graph, match, visited):
    for v in graph[u]:
        if visited[v]:
            continue

        visited[v] = True

        if match[v] == -1 or dfs(match[v], graph, match, visited):
            match[v] = u
            return True

    return False


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(N)]

    # i ke baad j ko same day me solve kar sakte hain?
    for i in range(N):
        for j in range(i + 1, N):
            if abs(arr[i] - arr[j]) >= K:
                graph[i].append(j)

    match = [-1] * N
    matching = 0

    for i in range(N):
        visited = [False] * N

        if dfs(i, graph, match, visited):
            matching += 1

    answer = N - matching

    print(answer)
