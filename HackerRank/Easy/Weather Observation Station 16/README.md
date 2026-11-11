# Weather Observation Station 16

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 16](https://www.hackerrank.com/challenges/weather-observation-station-16/problem)

## Problem Description

Query the smallest *Northern Latitude* (*LAT_N*) from **STATION** that is greater than . Round your answer to  decimal places.

**Input Format**

The **STATION** table is described as follows:

*

where LAT_N* is the northern latitude and *LONG_W* is the western longitude.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Weather Observation Station 16
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-16/problem
-- Difficulty: Easy
-- Language: mysql

SELECT round(min(lat_n),4)
from station 
where lat_n > 38.7780;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
