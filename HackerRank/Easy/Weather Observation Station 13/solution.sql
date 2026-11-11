-- HackerRank Problem: Weather Observation Station 13
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-13/problem
-- Difficulty: Easy
-- Language: mysql

SELECT truncate(sum(lat_n),4)
from station 
WHERE LAT_N > 38.7880
AND LAT_N < 137.2345
