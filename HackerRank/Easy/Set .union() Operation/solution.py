# HackerRank Problem: Set .union() Operation
# Link: https://www.hackerrank.com/challenges/py-set-union/problem
# Difficulty: Easy
# Language: python3

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

result = []

for i in a:
    if i not in result:
        result.append(i)

for i in b:
    if i not in result:
        result.append(i)

print(len(result)) 
