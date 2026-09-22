# HackerRank Problem: Grading Students
# Link: https://www.hackerrank.com/challenges/grading/problem
# Difficulty: Easy
# Language: python3

n=int(input())
for i in range(n):
    grade=int(input())
    
    if grade <38:
        print(grade)
        
    else:
        next=((grade//5)+1)*5
        diff=next-grade
        
        if diff < 3:
            print(next)
            
        else:
            print(grade)        
