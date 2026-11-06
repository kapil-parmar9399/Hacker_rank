-- HackerRank Problem: Revising the Select Query I
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem
-- Difficulty: Easy
-- Language: mysql

SELECT * from city 
where ( CountryCode = "USA" and population > 100000); 
