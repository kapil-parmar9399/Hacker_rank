# HackerRank Problem: Number Line Jumps
# Link: https://www.hackerrank.com/challenges/kangaroo/problem
# Difficulty: Easy
# Language: python3

x1, v1, x2, v2 = map(int, input().split())

for i in range(10000):
    if x1 == x2:
        print("YES")
        break

    x1 = x1 + v1
    x2 = x2 + v2
else:
    print("NO")
