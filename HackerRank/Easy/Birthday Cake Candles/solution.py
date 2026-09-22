# HackerRank Problem: Birthday Cake Candles
# Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Difficulty: Easy
# Language: python3

n=int(input())
arr=list(map(int,input().split()))

tallest=0
for i in arr:
    if i>tallest:
        tallest=i
        
count=0
for i in arr:
    if i==tallest:
        count+=1
        
print(count)                
    
