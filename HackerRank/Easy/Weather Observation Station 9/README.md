# Weather Observation Station 9

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 9](https://www.hackerrank.com/challenges/weather-observation-station-9/problem)

## Problem Description

Query the list of *CITY* names from **STATION** that *do not start* with vowels. Your result cannot contain duplicates.

**Input Format**

The **STATION** table is described as follows:

*

where LAT_N* is the northern latitude and *LONG_W* is the western longitude.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Weather Observation Station 9
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-9/problem
-- Difficulty: Easy
-- Language: mysql

SELECT distinct city 
from station 
where city NOT like 'A%'
      and city NOT like 'e%'
     and city NOT like 'i%'
     and city NOT like 'o%'
     and city NOT like 'u%' ;
     
     

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
