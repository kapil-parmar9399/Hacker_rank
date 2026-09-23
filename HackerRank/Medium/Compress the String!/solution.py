# HackerRank Problem: Compress the String! 
# Link: https://www.hackerrank.com/challenges/compress-the-string/problem
# Difficulty: Medium
# Language: python3

from itertools import groupby

S = input()

for key, group in groupby(S):
    print((len(list(group)), int(key)), end=" ")
