# Weather Observation Station 14

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 14](https://www.hackerrank.com/challenges/weather-observation-station-14/problem)

## Problem Description

Query the greatest value of the *Northern Latitudes* (*LAT_N*) from **STATION** that is less than . Truncate your answer to  decimal places.

**Input Format**

The **STATION** table is described as follows:

*

where LAT_N* is the northern latitude and *LONG_W* is the western longitude.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Weather Observation Station 14
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-14/problem
-- Difficulty: Easy
-- Language: mysql

SELECT truncate (max(lat_n),4)
 from  station 
 where lat_n <137.2345;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
