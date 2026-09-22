# HackerRank Problem: Merge the Tools!
# Link: https://www.hackerrank.com/challenges/merge-the-tools/problem
# Difficulty: Medium
# Language: python3

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        part=string[i:i+k]
        result=""
        
        for ch in part:
            if ch not in result:
                result+=ch
                
        print(result)        

