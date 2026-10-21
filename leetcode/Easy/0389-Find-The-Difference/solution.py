# LeetCode Problem: Find the Difference
# Link: https://leetcode.com/problems/find-the-difference/
# Difficulty: Easy
# Language: python3

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]

        return t[-1]

