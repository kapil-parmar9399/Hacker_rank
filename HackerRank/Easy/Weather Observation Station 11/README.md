# Weather Observation Station 11

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 11](https://www.hackerrank.com/challenges/weather-observation-station-11/problem)

## Problem Description

Query the list of *CITY* names from **STATION** that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

**Input Format**

The **STATION** table is described as follows:

*

where LAT_N* is the northern latitude and *LONG_W* is the western longitude.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Weather Observation Station 11
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
-- Difficulty: Easy
-- Language: mysql

SELECT DISTINCT CITY
FROM STATION
WHERE
    (CITY NOT LIKE 'A%'
     AND CITY NOT LIKE 'E%'
     AND CITY NOT LIKE 'I%'
     AND CITY NOT LIKE 'O%'
     AND CITY NOT LIKE 'U%')

OR
    (CITY NOT LIKE '%A'
     AND CITY NOT LIKE '%E'
     AND CITY NOT LIKE '%I'
     AND CITY NOT LIKE '%O'
     AND CITY NOT LIKE '%U');

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
