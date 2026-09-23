# HackerRank Problem: itertools.combinations()
# Link: https://www.hackerrank.com/challenges/itertools-combinations/problem
# Difficulty: Easy
# Language: python3

from itertools import combinations

S, k = input().split()

S = sorted(S)
k = int(k)

for r in range(1, k + 1):
    for c in combinations(S, r):
        print(''.join(c))
