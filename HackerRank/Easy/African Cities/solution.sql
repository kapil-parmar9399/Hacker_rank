-- HackerRank Problem: African Cities
-- Link: https://www.hackerrank.com/challenges/african-cities/problem
-- Difficulty: Easy
-- Language: mysql

SELECT city. name from city
JOIN country
ON 
CITY.CountryCode = COUNTRY.Code
where continent ='africa';
