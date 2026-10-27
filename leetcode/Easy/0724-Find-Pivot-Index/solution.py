# LeetCode Problem: Find Pivot Index
# Link: https://leetcode.com/problems/find-pivot-index/
# Difficulty: Easy
# Language: python3

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left=0
        right=0
        total=sum(nums)
        for i in range(len(nums)):
            right=total-left-nums[i]

            if left==right:
                return i

            left+=nums[i]

        return -1
                