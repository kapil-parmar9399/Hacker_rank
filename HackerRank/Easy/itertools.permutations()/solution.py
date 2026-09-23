# HackerRank Problem: itertools.permutations()
# Link: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Difficulty: Easy
# Language: python3

from itertools import permutations

S, k = input().split()

for p in permutations(sorted(S), int(k)):
    print(''.join(p))
