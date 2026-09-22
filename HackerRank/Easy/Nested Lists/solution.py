# HackerRank Problem: Nested Lists
# Link: https://www.hackerrank.com/challenges/nested-list/problem
# Difficulty: Easy
# Language: python3

if __name__ == '__main__':
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
    findScore =[x[1] for x in lst]
    sortScore= sorted(set(findScore))
    findName = sorted([y[0] for y in lst if(sortScore[1] == y[1])]) 
    for z in findName:
        print(z)     
