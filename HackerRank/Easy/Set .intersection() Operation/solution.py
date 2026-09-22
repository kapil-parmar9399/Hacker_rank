# HackerRank Problem: Set .intersection() Operation
# Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Difficulty: Easy
# Language: python3

m = int(input())
a = list(map(int, input().split()))

n = int(input())
b = list(map(int, input().split()))

total = []

for i in a:
    if i in b:
        total.append(i)

print(len(total))
