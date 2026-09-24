# HackerRank Problem: Collections.namedtuple()
# Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Difficulty: Easy
# Language: python3

n = int(input())

columns = input().split()

marks_index = columns.index("MARKS")

total = 0

for i in range(n):
    student = input().split()
    total += int(student[marks_index])

average = total / n

print(f"{average:.2f}")
