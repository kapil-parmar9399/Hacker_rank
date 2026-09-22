# HackerRank Problem: Mutations
# Link: https://www.hackerrank.com/challenges/python-mutations/problem
# Difficulty: Easy
# Language: python3


def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

