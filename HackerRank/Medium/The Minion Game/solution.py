# HackerRank Problem: The Minion Game
# Link: https://www.hackerrank.com/challenges/the-minion-game/problem
# Difficulty: Medium
# Language: python3

def minion_game(s):
    
    stuart=0
    kevin=0
    
    for i in range(len(s)):
        if s[i] in "AEIOU":
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw") 
