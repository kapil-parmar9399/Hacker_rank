# Employee Names

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Employee Names](https://www.hackerrank.com/challenges/name-of-employees/problem)

## Problem Description

Write a query that prints a list of employee names (i.e.: the *name* attribute) from the **Employee** table in alphabetical order.

**Input Format**

The **Employee** table containing employee data for a company is described as follows:

*

where employee_id* is an employee's ID number, *name* is their name, *months* is the total number of months they've been working for the company, and *salary* is their monthly salary.

**Sample Input**

![](https://s3.amazonaws.com/hr-challenge-images/19629/1458558202-9a8721e44b-ScreenShot2016-03-21at4.32.59PM.png)

**Sample Output**

```
Angela
Bonnie
Frank
Joe
Kimberly
Lisa
Michael
Patrick
Rose
Todd

```

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Employee Names
-- Link: https://www.hackerrank.com/challenges/name-of-employees/problem
-- Difficulty: Easy
-- Language: mysql

SELECT name from employee
order by  name asc;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
