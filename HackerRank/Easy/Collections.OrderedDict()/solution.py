# HackerRank Problem: Collections.OrderedDict()
# Link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Difficulty: Easy
# Language: python3

n = int(input())

items = {}

for i in range(n):
    data = input().split()

    name = " ".join(data[:-1])
    price = int(data[-1])

    if name in items:
        items[name] += price
    else:
        items[name] = price

for name, price in items.items():
    print(name, price)
