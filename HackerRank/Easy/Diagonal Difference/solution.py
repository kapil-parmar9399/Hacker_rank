# HackerRank Problem: Diagonal Difference
# Link: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Difficulty: Easy
# Language: python3

n=int(input())
arr=[]
for  i in range(n):
    row=list(map(int,input().split()))
    arr.append(row)
    
a=0
b=0

for i in range(n):
    a+=arr[i][i]
    b+=arr[i][n-1-i]    
    
print(abs(a-b))    
