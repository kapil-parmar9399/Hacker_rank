# Revising Aggregations - Averages

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Revising Aggregations - Averages](https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem)

## Problem Description

Query the average population of all cities in **CITY** where *District* is **California**.

**Input Format**

The **CITY** table is described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Revising Aggregations - Averages
-- Link: https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
-- Difficulty: Easy
-- Language: mysql

SELECT avg(population)
from city 
where district = 'california';

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
