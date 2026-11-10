-- HackerRank Problem: The Blunder
-- Link: https://www.hackerrank.com/challenges/the-blunder/problem
-- Difficulty: Easy
-- Language: mysql

select ceil(
avg(salary) - avg(replace(salary,'0',''))
)
from employees;
