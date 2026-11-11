-- HackerRank Problem: Weather Observation Station 14
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-14/problem
-- Difficulty: Easy
-- Language: mysql

SELECT truncate (max(lat_n),4)
 from  station 
 where lat_n <137.2345;
