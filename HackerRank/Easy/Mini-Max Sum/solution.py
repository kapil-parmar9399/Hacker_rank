# HackerRank Problem: Mini-Max Sum
# Link: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Difficulty: Easy
# Language: python3

arr = list(map(int, input().split()))

total = sum(arr)

minimum = total - max(arr)
maximum = total - min(arr)

print(minimum, maximum)
