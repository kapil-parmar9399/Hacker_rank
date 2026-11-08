# Higher Than 75 Marks

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Higher Than 75 Marks](https://www.hackerrank.com/challenges/more-than-75-marks/problem)

## Problem Description

Query the *Name* of any student in **STUDENTS** who scored higher than  *Marks*. Order your output by the *last three characters* of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending *ID*.

**Input Format**

The **STUDENTS** table is described as follows:
*
The Name* column only contains uppercase (`A`-`Z`) and lowercase (`a`-`z`) letters.

**Sample Input**

*

**Sample Output**

```
Ashley
Julia
Belvet

```

**Explanation**

Only Ashley, Julia, and Belvet have Marks* > . If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Higher Than 75 Marks
-- Link: https://www.hackerrank.com/challenges/more-than-75-marks/problem
-- Difficulty: Easy
-- Language: mysql

SELECT name  
from students
where marks >75
order by right(name,3) ASC ,id ASC;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
