# Average Population

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Average Population](https://www.hackerrank.com/challenges/average-population/problem)

## Problem Description

Query the average population for all cities in **CITY**, rounded *down* to the nearest integer.

**Input Format**

The **CITY** table is described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Average Population
-- Link: https://www.hackerrank.com/challenges/average-population/problem
-- Difficulty: Easy
-- Language: mysql

SELECT round(avg(population))
from city

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
