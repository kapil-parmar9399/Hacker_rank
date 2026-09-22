# HackerRank Problem: Check Strict Superset
# Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Difficulty: Easy
# Language: python3

a = set(map(int, input().split()))

n = int(input())

result = True

for _ in range(n):
    b = set(map(int, input().split()))

    if not a > b:
        result = False

print(result)
