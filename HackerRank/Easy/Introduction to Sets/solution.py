# HackerRank Problem: Introduction to Sets
# Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Difficulty: Easy
# Language: python3

def average(array):
    array = set(array)

    total = 0

    for i in array:
        total = total + i

    result = total / len(array)

    return result
