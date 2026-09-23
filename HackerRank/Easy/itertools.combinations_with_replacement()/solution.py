# HackerRank Problem: itertools.combinations_with_replacement()
# Link: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Difficulty: Easy
# Language: python3

from itertools import combinations_with_replacement

S, k = input().split()

for c in combinations_with_replacement(sorted(S), int(k)):
    print(''.join(c))
