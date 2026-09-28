# LeetCode Problem: Find the Index of the First Occurrence in a String
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Difficulty: Easy
# Language: python3

class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1
            