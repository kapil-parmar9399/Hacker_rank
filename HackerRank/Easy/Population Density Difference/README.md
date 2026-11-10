# Population Density Difference

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Population Density Difference](https://www.hackerrank.com/challenges/population-density-difference/problem)

## Problem Description

Query the difference between the maximum and minimum populations in **CITY**.

**Input Format**

The **CITY** table is described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Population Density Difference
-- Link: https://www.hackerrank.com/challenges/population-density-difference/problem
-- Difficulty: Easy
-- Language: mysql

SELECT max(population) - min(population)
from city;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
