-- HackerRank Problem: Weather Observation Station 16
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-16/problem
-- Difficulty: Easy
-- Language: mysql

SELECT round(min(lat_n),4)
from station 
where lat_n > 38.7780;
