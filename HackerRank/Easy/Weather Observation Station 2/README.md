# Weather Observation Station 2

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 2](https://www.hackerrank.com/challenges/weather-observation-station-2/problem)

## Problem Description

Query the following two values from the **STATION** table:

* The sum of all values in *LAT_N* rounded to a scale of  decimal places.

* The sum of all values in *LONG_W* rounded to a scale of  decimal places.

**Input Format**

The **STATION** table is described as follows:

*

where LAT_N* is the northern latitude and *LONG_W* is the western longitude.

**Output Format**

Your results must be in the form:

```
lat lon

```

where  is the sum of all values in *LAT_N* and  is the sum of all values in *LONG_W*. Both results must be rounded to a scale of  decimal places.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Weather Observation Station 2
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-2/problem
-- Difficulty: Easy
-- Language: mysql

SELECT round(sum(lat_n),2),
round (sum(long_w),2)  from station;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
