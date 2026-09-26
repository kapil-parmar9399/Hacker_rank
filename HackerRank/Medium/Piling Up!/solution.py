# HackerRank Problem: Piling Up!
# Link: https://www.hackerrank.com/challenges/piling-up/problem
# Difficulty: Medium
# Language: python3

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    a = deque(map(int, input().split()))

    last = float("inf")
    ok = True

    for i in range(n):
        if a[0] >= a[-1]:
            x = a[0]
        else:
            x = a[-1]

        if x > last:
            ok = False
            break

        if a[0] == x:
            a.popleft()
        else:
            a.pop()

        last = x

    print("Yes" if ok else "No")
