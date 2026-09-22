# Time Conversion

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Time Conversion](https://www.hackerrank.com/challenges/time-conversion/problem)

## Problem Description

Given a time in [-hour AM/PM format](https://en.wikipedia.org/wiki/12-hour_clock), convert it to military (24-hour) time.

Note:
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. **
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example**

*

Return '12:01:00'.

*

Return '00:01:00'.

**Function Description**

Complete the  function with the following parameter(s):

* : a time in  hour format

**Returns**

* : the time in  hour format

**Input Format**

A single string  that represents a time in -hour clock format (i.e.:  or ).

**Constraints**

* All input times are valid

**Sample Input 0**

```
07:05:45PM

```

**Sample Output 0**

```
19:05:45

```

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Time Conversion
# Link: https://www.hackerrank.com/challenges/time-conversion/problem
# Difficulty: Easy
# Language: python3

time = input()

hour = int(time[:2])
period = time[-2:]

if period == "AM":
    if hour == 12:
        hour = 0
else:
    if hour != 12:
        hour += 12

print(f"{hour:02d}{time[2:-2]}")


```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
