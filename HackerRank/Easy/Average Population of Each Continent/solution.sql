-- HackerRank Problem: Average Population of Each Continent
-- Link: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
-- Difficulty: Easy
-- Language: mysql

SELECT COUNTRY.CONTINENT,
       FLOOR(AVG(CITY.POPULATION))
FROM CITY
JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;
