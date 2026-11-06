-- HackerRank Problem: Weather Observation Station 5
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-5/problem
-- Difficulty: Easy
-- Language: mysql

(SELECT CITY, LENGTH(CITY)
 FROM STATION
 ORDER BY LENGTH(CITY) ASC, CITY ASC
 LIMIT 1)

UNION ALL

(SELECT CITY, LENGTH(CITY)
 FROM STATION
 ORDER BY LENGTH(CITY) DESC, CITY ASC
 LIMIT 1);
