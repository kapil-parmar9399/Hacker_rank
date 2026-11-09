# Revising Aggregations - The Count Function

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Revising Aggregations - The Count Function](https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem)

## Problem Description

Query a *count* of the number of cities in **CITY** having a *Population* larger than .

**Input Format**

The **CITY** table is described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Revising Aggregations - The Count Function
-- Link: https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem
-- Difficulty: Easy
-- Language: mysql

SELECT count(name ) from city 
where population >100000;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
