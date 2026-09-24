# HackerRank Problem: collections.Counter()
# Link: https://www.hackerrank.com/challenges/collections-counter/problem
# Difficulty: Easy
# Language: python3

n = int(input())

shoes = list(map(int, input().split()))

customers = int(input())

total = 0

for i in range(customers):
    size, price = map(int, input().split())

    if size in shoes:
        total += price
        shoes.remove(size)

print(total)
