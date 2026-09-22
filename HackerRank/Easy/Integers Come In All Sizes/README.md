# Integers Come In All Sizes

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Integers Come In All Sizes](https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem)

## Problem Description

Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).

As we know, the result of  grows really fast with increasing .

Let's do some calculations on very large integers.

**Task** **
Read four numbers, , , , and , and print the result of .

Input Format** **
Integers , , , and  are given on four separate lines, respectively.

Constraints** **

Output Format** **
Print the result of  on one line.

Sample Input**

```
9
29
7
27

```

**Sample Output**

```
4710194409608608369201743232

```

**Note**: This result is bigger than . Hence, it won't fit in the long long int of C++ or a 64-bit integer.

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Integers Come In All Sizes
# Link: https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
# Difficulty: Easy
# Language: python3

# Enter your code here. Read input from STDIN. Print output to STDOUT-

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b + c**d)

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
