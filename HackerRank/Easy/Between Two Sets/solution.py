# HackerRank Problem: Between Two Sets
# Link: https://www.hackerrank.com/challenges/between-two-sets/problem
# Difficulty: Easy
# Language: python3

m,n=list(map(int,input().split()))

a=list(map(int,input().split()))
b=list(map(int,input().split()))

count=0
for i in range(1,101):
    valid=True
    
    for x in a:
        if i%x!=0:
            valid=False
            break
            
    for j in b:
        if j%i!=0:
            valid=False
            
    if valid:
        count+=1
        
print(count)             
    
