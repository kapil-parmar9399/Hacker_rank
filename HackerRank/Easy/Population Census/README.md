# Population Census 

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Population Census ](https://www.hackerrank.com/challenges/asian-population/problem)

## Problem Description

Given the **CITY** and **COUNTRY** tables, query the sum of the populations of all cities where the *CONTINENT* is *'Asia'*.

**Note:** *CITY.CountryCode* and *COUNTRY.Code* are matching key columns.

**Input Format**

The **CITY** and **COUNTRY** tables are described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

![](https://s3.amazonaws.com/hr-challenge-images/8342/1449769013-e54ce90480-Country.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Population Census 
-- Link: https://www.hackerrank.com/challenges/asian-population/problem
-- Difficulty: Easy
-- Language: mysql

SELECT sum(city.population)
from city 
join country
ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.CONTINENT = 'Asia';

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
