-- HackerRank Problem: Revising Aggregations - Averages
-- Link: https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
-- Difficulty: Easy
-- Language: mysql

SELECT avg(population)
from city 
where district = 'california';
