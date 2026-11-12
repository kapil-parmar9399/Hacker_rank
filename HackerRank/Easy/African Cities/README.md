# African Cities

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [African Cities](https://www.hackerrank.com/challenges/african-cities/problem)

## Problem Description

Given the **CITY** and **COUNTRY** tables, query the names of all cities where the *CONTINENT* is *'Africa'*.

**Note:** *CITY.CountryCode* and *COUNTRY.Code* are matching key columns.

**Input Format**

The **CITY** and **COUNTRY** tables are described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

![](https://s3.amazonaws.com/hr-challenge-images/8342/1449769013-e54ce90480-Country.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: African Cities
-- Link: https://www.hackerrank.com/challenges/african-cities/problem
-- Difficulty: Easy
-- Language: mysql

SELECT city. name from city
JOIN country
ON 
CITY.CountryCode = COUNTRY.Code
where continent ='africa';

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
