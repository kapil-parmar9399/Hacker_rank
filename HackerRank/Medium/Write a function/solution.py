# HackerRank Problem: Write a function
# Link: https://www.hackerrank.com/challenges/write-a-function/problem
# Difficulty: Medium
# Language: python3

def is_leap(n):
    
    if n%400==0:
        return True
    if n%100==0:
        return False  
    if n%4==0:
        return True 
    return False     

