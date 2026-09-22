# Mini-Max Sum

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Mini-Max Sum](https://www.hackerrank.com/challenges/mini-max-sum/problem)

## Problem Description

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

**Example** **

The minimum sum is  and the maximum sum is .  The function prints

```
16 24

```

Function Description**

Complete the  function with the following parameter(s):

* : an array of  integers

**Print**

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.No value should be returned.

**Note** For some languages, like C, C++, and Java, the sums may require that you use a long integer due to their size.

**Input Format**

A single line of five space-separated integers.

**Constraints**

**Sample Input**

```
1 2 3 4 5

```

**Sample Output**

```
10 14

```

**Explanation**

The numbers are , , , , and . Calculate the following sums using four of the five integers:

* Sum everything except , the sum is .

* Sum everything except , the sum is .

* Sum everything except , the sum is .

* Sum everything except , the sum is .

* Sum everything except , the sum is .

**Hints:** Beware of integer overflow! Use a 64-bit integer to store the sums.

Need help to get started? Try the [Solve Me First](https://www.hackerrank.com/challenges/solve-me-first) problem.

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Mini-Max Sum
# Link: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Difficulty: Easy
# Language: python3

arr = list(map(int, input().split()))

total = sum(arr)

minimum = total - max(arr)
maximum = total - min(arr)

print(minimum, maximum)

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
