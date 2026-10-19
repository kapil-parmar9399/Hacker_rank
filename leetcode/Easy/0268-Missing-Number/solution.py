# LeetCode Problem: Missing Number
# Link: https://leetcode.com/problems/missing-number/
# Difficulty: Easy
# Language: python3

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            if i not in nums:
                return i

          


