# Diagonal Difference

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Diagonal Difference](https://www.hackerrank.com/challenges/diagonal-difference/problem)

## Problem Description

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

```
1 2 3
4 5 6
9 8 9

```

* The left-to-right diagonal = .

* The right-to-left diagonal = .

Their absolute difference is .

**Function description**

Complete the  function with the following parameter:

* : a 2-D array of integers

**Return**

* : the absolute difference in sums along the diagonals

**Input Format**

The first line contains a single integer, ,  the number of rows and columns in the square matrix . **
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints**

*

**Sample Input**

```
STDIN      Function
-----      --------
3           arr[][] sizes n = 3, m = 3
11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
4 5 6
10 8 -12

```

**Sample Output**

```
15

```

**Explanation**

The primary diagonal is:

```
11
   5
     -12

```

Sum across the primary diagonal: .

The secondary diagonal is:

```
     4
   5
10

```

Sum across the secondary diagonal:  **
Difference:

Note:** |x| is the [absolute value](https://www.mathsisfun.com/numbers/absolute-value.html) of x.

## Examples



## Constraints



## Solution

```python3
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

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
