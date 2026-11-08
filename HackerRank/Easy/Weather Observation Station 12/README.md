# Weather Observation Station 12

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 12](https://www.hackerrank.com/challenges/weather-observation-station-12/problem)

## Problem Description

Query the list of *CITY* names from **STATION** that *do not start* with vowels and *do not end* with vowels. Your result cannot contain duplicates.

**Input Format**

The **STATION** table is described as follows:

*

where LAT_N* is the northern latitude and *LONG_W* is the western longitude.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Weather Observation Station 12
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-12/problem
-- Difficulty: Easy
-- Language: mysql

SELECT DISTINCT CITY
FROM STATION
WHERE CITY NOT LIKE 'A%'
  AND CITY NOT LIKE 'E%'
  AND CITY NOT LIKE 'I%'
  AND CITY NOT LIKE 'O%'
  AND CITY NOT LIKE 'U%'
  AND CITY NOT LIKE '%A'
  AND CITY NOT LIKE '%E'
  AND CITY NOT LIKE '%I'
  AND CITY NOT LIKE '%O'
  AND CITY NOT LIKE '%U';

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
