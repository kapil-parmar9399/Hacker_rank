-- HackerRank Problem: Top Earners
-- Link: https://www.hackerrank.com/challenges/earnings-of-employees/problem
-- Difficulty: Easy
-- Language: mysql

SELECT max(salary * months) , count(*)
from employee
where salary * months =(
    SELECT max(salary * months )
    from employee
);
