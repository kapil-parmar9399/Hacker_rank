# Japan Population

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Japan Population](https://www.hackerrank.com/challenges/japan-population/problem)

## Problem Description

Query the sum of the populations for all Japanese cities in **CITY**. The *COUNTRYCODE* for Japan is **JPN**.

**Input Format**

The **CITY** table is described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Japan Population
-- Link: https://www.hackerrank.com/challenges/japan-population/problem
-- Difficulty: Easy
-- Language: mysql

SELECT sum(population) 
from city 
where countrycode ='jpn';

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
