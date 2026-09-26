# HackerRank Problem: Word Order
# Link: https://www.hackerrank.com/challenges/word-order/problem
# Difficulty: Medium
# Language: python3

n=int(input())
words={}

for i in range (n):
    string=input().strip()
    
    if string in words:
        words[string]+=1
        
    else:
        words[string]=1
        
print(len(words))

print(*words.values())            
