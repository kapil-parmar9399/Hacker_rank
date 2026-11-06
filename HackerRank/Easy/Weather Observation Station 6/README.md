# Weather Observation Station 6

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 6](https://www.hackerrank.com/challenges/weather-observation-station-6/problem)

## Problem Description

Query the list of *CITY* names starting with vowels (i.e., `a`, `e`, `i`, `o`, or `u`) from **STATION**. Your result *cannot* contain duplicates.

**Input Format**

The **STATION** table is described as follows:

*

where LAT_N* is the northern latitude and *LONG_W* is the western longitude.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Weather Observation Station 6
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-6/problem
-- Difficulty: Easy
-- Language: mysql

/*
Enter your query here.
*/

select city from station 
where city like "a%"
       or city like "e%"
        or city like "i%"
         or city like "o%"
          or city like "u%"
          

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
