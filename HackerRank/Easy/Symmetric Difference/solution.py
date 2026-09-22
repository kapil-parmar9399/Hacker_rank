# HackerRank Problem: Symmetric Difference
# Link: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Difficulty: Easy
# Language: python3

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

result = sorted(a.symmetric_difference(b))

for i in result:
    print(i)
