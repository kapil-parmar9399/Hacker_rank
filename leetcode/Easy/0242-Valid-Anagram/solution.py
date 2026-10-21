# LeetCode Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Language: python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s==t:
            return True

        else:
            return False
        
