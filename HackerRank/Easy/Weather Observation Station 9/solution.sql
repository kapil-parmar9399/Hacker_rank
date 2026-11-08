-- HackerRank Problem: Weather Observation Station 9
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-9/problem
-- Difficulty: Easy
-- Language: mysql

SELECT distinct city 
from station 
where city NOT like 'A%'
      and city NOT like 'e%'
     and city NOT like 'i%'
     and city NOT like 'o%'
     and city NOT like 'u%' ;
     
     
