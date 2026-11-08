# Type of Triangle

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Type of Triangle](https://www.hackerrank.com/challenges/what-type-of-triangle/problem)

## Problem Description

Write a query identifying the *type* of each record in the **TRIANGLES** table using its three side lengths. Output one of the following statements for each record in the table:

* **Equilateral**: It's a triangle with  sides of equal length.

* **Isosceles**: It's a triangle with  sides of equal length.

* **Scalene**: It's a triangle with  sides of differing lengths.

* **Not A Triangle**: The given values of *A*, *B*, and *C* don't form a triangle.

**Input Format**

The **TRIANGLES** table is described as follows:

![](https://s3.amazonaws.com/hr-challenge-images/12887/1443815629-ac2a843fb7-1.png)

Each row in the table denotes the lengths of each of a triangle's three sides.

**Sample Input**

![](https://s3.amazonaws.com/hr-challenge-images/12887/1443815827-cbfc1ca12b-2.png)

**Sample Output**

```
Isosceles
Equilateral
Scalene
Not A Triangle

```

**Explanation**

Values in the tuple  form an Isosceles triangle, because .

Values in the tuple  form an Equilateral triangle, because .
Values in the tuple  form a Scalene triangle, because .

Values in the tuple  cannot form a triangle because the combined value of sides  and  is not larger than that of side .

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Type of Triangle
-- Link: https://www.hackerrank.com/challenges/what-type-of-triangle/problem
-- Difficulty: Easy
-- Language: mysql

SELECT
    CASE
        WHEN A + B <= C OR A + C <= B OR B + C <= A
            THEN 'Not A Triangle'

        WHEN A = B AND B = C
            THEN 'Equilateral'

        WHEN A = B OR B = C OR A = C
            THEN 'Isosceles'

        ELSE 'Scalene'
    END
FROM TRIANGLES;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
