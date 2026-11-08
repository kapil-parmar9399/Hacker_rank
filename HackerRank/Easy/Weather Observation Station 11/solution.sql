-- HackerRank Problem: Weather Observation Station 11
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
-- Difficulty: Easy
-- Language: mysql

SELECT DISTINCT CITY
FROM STATION
WHERE
    (CITY NOT LIKE 'A%'
     AND CITY NOT LIKE 'E%'
     AND CITY NOT LIKE 'I%'
     AND CITY NOT LIKE 'O%'
     AND CITY NOT LIKE 'U%')

OR
    (CITY NOT LIKE '%A'
     AND CITY NOT LIKE '%E'
     AND CITY NOT LIKE '%I'
     AND CITY NOT LIKE '%O'
     AND CITY NOT LIKE '%U');
