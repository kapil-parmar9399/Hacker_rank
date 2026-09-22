# HackerRank Problem: Triangle Quest
# Link: https://www.hackerrank.com/challenges/python-quest-1/problem
# Difficulty: Medium
# Language: python3

n = int(input())
for i in range(1, n): print(i * (10**i - 1) // 9)
