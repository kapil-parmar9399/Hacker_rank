# Simple Array Sum

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Simple Array Sum](https://www.hackerrank.com/challenges/simple-array-sum/problem)

## Problem Description

Given an array of integers, find the sum of its elements.

For example, if the array , , so return .

**Function Description**

Complete the  function with the following parameter(s):

* : an array of integers

**Returns**

* : the sum of the array elements

**Input Format**

The first line contains an integer, , denoting the size of the array. **
The second line contains  space-separated integers representing the array's elements.

Constraints**

**Sample Input**

```
STDIN           Function
-----           --------
6               ar[] size n = 6
1 2 3 4 10 11   ar = [1, 2, 3, 4, 10, 11]

```

**Sample Output**

```
31

```

**Explanation**

Print the sum of the array's elements: .

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Simple Array Sum
# Link: https://www.hackerrank.com/challenges/simple-array-sum/problem
# Difficulty: Easy
# Language: python3

n = int(input())
arr = list(map(int, input().split()))

total = 0

for i in arr:
    total += i

print(total)

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
