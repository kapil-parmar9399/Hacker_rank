# Capitalize!

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Capitalize!](https://www.hackerrank.com/challenges/capitalize/problem)

## Problem Description

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, `alison heck` should be capitalised correctly as `Alison Heck`.

Given a full name, your task is to *capitalize* the name appropriately.

**Input Format**

A single line of input containing the full name, .

**Constraints**

*

* The string consists of alphanumeric characters and spaces.

**Note:** in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

**Output Format**

Print the capitalized string, .

**Sample Input**

```
chris alan

```

**Sample Output**

```
Chris Alan

```

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Capitalize!
# Link: https://www.hackerrank.com/challenges/capitalize/problem
# Difficulty: Easy
# Language: python3



# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    result = []

    for word in words:
        if word:
            result.append(word[0].upper() + word[1:])
        else:
            result.append("")

    return " ".join(result)


```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
