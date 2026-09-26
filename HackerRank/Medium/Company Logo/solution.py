# HackerRank Problem: Company Logo
# Link: https://www.hackerrank.com/challenges/most-commons/problem
# Difficulty: Medium
# Language: python3

s = input()

count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

items = list(count.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] < items[j][1]:
            items[i], items[j] = items[j], items[i]

        elif items[i][1] == items[j][1] and items[i][0] > items[j][0]:
            items[i], items[j] = items[j], items[i]

for i in range(3):
    print(items[i][0], items[i][1])
