# HackerRank Problem: DefaultDict Tutorial
# Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Difficulty: Easy
# Language: python3

from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

for i in range(n):
    word = input()
    d[word].append(i + 1)

for i in range(m):
    word = input()

    if word in d:
        print(*d[word])
    else:
        print(-1) 
