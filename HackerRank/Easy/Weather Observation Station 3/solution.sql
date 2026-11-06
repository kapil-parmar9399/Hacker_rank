-- HackerRank Problem: Weather Observation Station 3
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-3/problem
-- Difficulty: Easy
-- Language: mysql

/*
Enter your query here.
*/

SELECT distinct city 
from station
where Id %2 =0;
