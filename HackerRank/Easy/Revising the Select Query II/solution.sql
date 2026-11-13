-- HackerRank Problem: Revising the Select Query II
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
-- Difficulty: Easy
-- Language: mysql

SELECT name from city 
where countrycode = 'USA' and  population  > 120000;
