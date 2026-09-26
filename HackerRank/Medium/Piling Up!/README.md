# Piling Up!

**Difficulty:** Medium  
**Topics:** N/A  
**HackerRank URL:** [Piling Up!](https://www.hackerrank.com/challenges/piling-up/problem)

## Problem Description

There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print `Yes` if it is possible to stack the cubes. Otherwise, print `No`.

**Example** **

Result: `No`

After choosing the rightmost element, , choose the leftmost element, .  After than, the choices are  and .  These are both larger than the top block of size .

Result: `Yes`

Choose blocks from right to left in order to successfully stack the blocks.

Input Format**

The first line contains a single integer , the number of test cases. **
For each test case, there are  lines.

The first line of each test case contains , the number of cubes.

The second line contains  space separated integers, denoting the *sideLengths* of each cube in that order.

Constraints**

 **

Output Format**

For each test case, output a single line containing either `Yes` or `No`.

**Sample Input**

```
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]

```

**Sample Output**

```
Yes
No

```

**Explanation**

In the first test case, pick in this order: **left - , right - , left - , right - , left - , right - **.

 In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either  or .

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Piling Up!
# Link: https://www.hackerrank.com/challenges/piling-up/problem
# Difficulty: Medium
# Language: python3

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    a = deque(map(int, input().split()))

    last = float("inf")
    ok = True

    for i in range(n):
        if a[0] >= a[-1]:
            x = a[0]
        else:
            x = a[-1]

        if x > last:
            ok = False
            break

        if a[0] == x:
            a.popleft()
        else:
            a.pop()

        last = x

    print("Yes" if ok else "No")

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
