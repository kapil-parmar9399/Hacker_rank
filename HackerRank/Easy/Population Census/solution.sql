-- HackerRank Problem: Population Census 
-- Link: https://www.hackerrank.com/challenges/asian-population/problem
-- Difficulty: Easy
-- Language: mysql

SELECT sum(city.population)
from city 
join country
ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.CONTINENT = 'Asia';
