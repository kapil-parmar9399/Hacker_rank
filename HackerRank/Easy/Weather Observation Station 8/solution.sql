-- HackerRank Problem: Weather Observation Station 8
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-8/problem
-- Difficulty: Easy
-- Language: mysql

SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(CITY, 1, 1)) IN ('a', 'e', 'i', 'o', 'u')
AND LOWER(SUBSTRING(CITY, -1, 1)) IN ('a', 'e', 'i', 'o', 'u');
