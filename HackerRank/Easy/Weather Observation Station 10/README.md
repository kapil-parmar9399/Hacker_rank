# Weather Observation Station 10

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 10](https://www.hackerrank.com/challenges/weather-observation-station-10/problem)

## Problem Description

Query the list of *CITY* names from **STATION** that *do not end* with vowels. Your result cannot contain duplicates.

**Input Format**

The **STATION** table is described as follows:

*

where LAT_N* is the northern latitude and *LONG_W* is the western longitude.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Weather Observation Station 10
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-10/problem
-- Difficulty: Easy
-- Language: mysql

SELECT distinct city 
from station 
where city not like '%a'
      and city not like '%e' 
       and city not like '%i' 
        and city not like '%o' 
         and city not like '%u'; 

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
