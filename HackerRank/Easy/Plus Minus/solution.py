# HackerRank Problem: Plus Minus
# Link: https://www.hackerrank.com/challenges/plus-minus/problem
# Difficulty: Easy
# Language: python3

n=int(input())
arr=list(map(int,input().split()))
positive=0
negative=0
zero=0

for i in arr:
    if i >0:
        positive+=1
        
    elif i<0:
        negative +=1
        
    elif i ==0:
        zero+=1
        
        
        
print(positive/n) 
print(negative/n)       
print(zero/n)    
            
