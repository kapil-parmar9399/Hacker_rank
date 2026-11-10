-- HackerRank Problem: Japan Population
-- Link: https://www.hackerrank.com/challenges/japan-population/problem
-- Difficulty: Easy
-- Language: mysql

SELECT sum(population) 
from city 
where countrycode ='jpn';
