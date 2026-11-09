# Revising Aggregations - The Sum Function

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Revising Aggregations - The Sum Function](https://www.hackerrank.com/challenges/revising-aggregations-sum/problem)

## Problem Description

Query the total population of all cities in **CITY** where *District* is **California**.

**Input Format**

The **CITY** table is described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Revising Aggregations - The Sum Function
-- Link: https://www.hackerrank.com/challenges/revising-aggregations-sum/problem
-- Difficulty: Easy
-- Language: mysql

SELECT sum(population)
from city 
where district ='california';

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
