# HackerRank Problem: Apple and Orange
# Link: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Difficulty: Easy
# Language: python3

s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apple=list(map(int,input().split()))
orange=list(map(int,input().split()))

ac=0
oc=0
for i in apple:
    if s<=a+i<=t:
        ac+=1
        
for i in orange:
    if s<=b+i<=t:
        oc+=1
        
print(ac)
print(oc)                
