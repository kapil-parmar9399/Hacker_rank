# Average Population of Each Continent

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Average Population of Each Continent](https://www.hackerrank.com/challenges/average-population-of-each-continent/problem)

## Problem Description

Given the **CITY** and **COUNTRY** tables, query the names of all the continents (*COUNTRY.Continent*) and their respective average city populations (*CITY.Population*) rounded *down* to the nearest integer.

**Note:** *CITY.CountryCode* and *COUNTRY.Code* are matching key columns.

**Input Format**

The **CITY** and **COUNTRY** tables are described as follows:
![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

![](https://s3.amazonaws.com/hr-challenge-images/8342/1449769013-e54ce90480-Country.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Average Population of Each Continent
-- Link: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
-- Difficulty: Easy
-- Language: mysql

SELECT COUNTRY.CONTINENT,
       FLOOR(AVG(CITY.POPULATION))
FROM CITY
JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
