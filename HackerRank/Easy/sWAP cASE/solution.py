# HackerRank Problem: sWAP cASE
# Link: https://www.hackerrank.com/challenges/swap-case/problem
# Difficulty: Easy
# Language: python3

def swap_case(s):
    result=""
    
    for ch in s:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch

    return result
