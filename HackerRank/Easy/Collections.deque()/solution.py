# HackerRank Problem: Collections.deque()
# Link: https://www.hackerrank.com/challenges/py-collections-deque/problem
# Difficulty: Easy
# Language: python3

from collections import deque
n=int(input())
d=deque()

for i in range(n):
    data=input().split()
    
    if data[0]=="append":
        d.append(int(data[1]))
        
    elif data[0]=="appendleft":
        d.appendleft(int(data[1]))
    elif data[0]=="pop":
        d.pop()
        
    elif data[0]=="popleft":
        d.popleft() 
        
        
        
        
print(*d)        
               
