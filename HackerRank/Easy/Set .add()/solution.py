# HackerRank Problem: Set .add() 
# Link: https://www.hackerrank.com/challenges/py-set-add/problem
# Difficulty: Easy
# Language: python3

n=int(input())

countries=set()

for i in range(n):
    country=input()
    countries.add(country)
    
    
print(len(countries))    
    
