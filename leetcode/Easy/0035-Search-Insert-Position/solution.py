# LeetCode Problem: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy
# Language: python3

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)