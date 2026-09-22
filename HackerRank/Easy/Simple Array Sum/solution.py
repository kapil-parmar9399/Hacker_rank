# HackerRank Problem: Simple Array Sum
# Link: https://www.hackerrank.com/challenges/simple-array-sum/problem
# Difficulty: Easy
# Language: python3

n = int(input())
arr = list(map(int, input().split()))

total = 0

for i in arr:
    total += i

print(total)
