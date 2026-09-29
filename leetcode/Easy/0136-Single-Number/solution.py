# LeetCode Problem: Single Number
# Link: https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Language: python3

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result = result ^ num

        return result