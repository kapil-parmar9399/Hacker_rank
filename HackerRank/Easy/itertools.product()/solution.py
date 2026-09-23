# HackerRank Problem: itertools.product()
# Link: https://www.hackerrank.com/challenges/itertools-product/problem
# Difficulty: Easy
# Language: python3

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*product(A, B))
