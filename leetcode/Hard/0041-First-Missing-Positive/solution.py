# LeetCode Problem: First Missing Positive
# Link: https://leetcode.com/problems/first-missing-positive/
# Difficulty: Hard
# Language: python3

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        seen = set(nums)

        for i in range(1, len(nums) + 2):
            if i not in seen:
                return i