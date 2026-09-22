# HackerRank Problem: Find the Runner-Up Score!  
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Difficulty: Easy
# Language: python3

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = sorted(set(arr))[-2]
    print(result)
