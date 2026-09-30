-- LeetCode Problem: Delete Duplicate Emails
-- Link: https://leetcode.com/problems/delete-duplicate-emails/
-- Difficulty: Easy
-- Language: mysql

DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
WHERE p1.id > p2.id;