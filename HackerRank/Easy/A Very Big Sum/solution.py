# HackerRank Problem: A Very Big Sum
# Link: https://www.hackerrank.com/challenges/a-very-big-sum/problem
# Difficulty: Easy
# Language: python3

n=int(input())
num=list(map(int,input().split()))
sum=0
for i in num:
    sum+=i
    
print(sum)    
