-- HackerRank Problem: Weather Observation Station 2
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-2/problem
-- Difficulty: Easy
-- Language: mysql

SELECT round(sum(lat_n),2),
round (sum(long_w),2)  from station;
