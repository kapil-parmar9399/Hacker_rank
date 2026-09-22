# HackerRank Problem: Staircase
# Link: https://www.hackerrank.com/challenges/staircase/problem
# Difficulty: Easy
# Language: python3

n= int(input())
for i in range(n):
    print(" " * (n-i-1) + "#" *(i+1))
