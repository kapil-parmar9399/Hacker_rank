# HackerRank Problem: Set Mutations
# Link: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Difficulty: Easy
# Language: python3

n = int(input())
a = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    operation, length = input().split()
    other = set(map(int, input().split()))

    if operation == "update":
        a.update(other)

    elif operation == "intersection_update":
        a.intersection_update(other)

    elif operation == "difference_update":
        a.difference_update(other)

    elif operation == "symmetric_difference_update":
        a.symmetric_difference_update(other)

print(sum(a))
