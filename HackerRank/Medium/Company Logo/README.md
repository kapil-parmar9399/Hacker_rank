# Company Logo

**Difficulty:** Medium  
**Topics:** N/A  
**HackerRank URL:** [Company Logo](https://www.hackerrank.com/challenges/most-commons/problem)

## Problem Description

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

* Print the three most common characters along with their occurrence count.

* Sort in descending order of occurrence count.

* If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above,

 would have it's logo with the letters .

**Input Format**

A single line of input containing the string .

**Constraints**

*

*  has at least  distinct characters

**Output Format**

Print the three most common characters along with their occurrence count each on a separate line. **
Sort output in descending order of occurrence count.

If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0**

```
aabbbccde

```

**Sample Output 0**

```
b 3
a 2
c 2

```

**Explanation 0**

Here, *b* occurs  times. It is printed first.**
Both *a* and *c* occur  times. So, *a* is printed in the second line and *c* in the third line because *a* comes before *c* in the alphabet.

Note**: The string  has at least  distinct characters.

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Company Logo
# Link: https://www.hackerrank.com/challenges/most-commons/problem
# Difficulty: Medium
# Language: python3

s = input()

count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

items = list(count.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] < items[j][1]:
            items[i], items[j] = items[j], items[i]

        elif items[i][1] == items[j][1] and items[i][0] > items[j][0]:
            items[i], items[j] = items[j], items[i]

for i in range(3):
    print(items[i][0], items[i][1])

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
