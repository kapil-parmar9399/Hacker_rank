# HackerRank Problem: Capitalize!
# Link: https://www.hackerrank.com/challenges/capitalize/problem
# Difficulty: Easy
# Language: python3



# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    result = []

    for word in words:
        if word:
            result.append(word[0].upper() + word[1:])
        else:
            result.append("")

    return " ".join(result)

