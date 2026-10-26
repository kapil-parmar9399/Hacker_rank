# LeetCode Problem: Running Sum of 1d Array
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
# Difficulty: Easy
# Language: python3

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix=[]
        total=0
        for i in range (len(nums)):
            total=total+nums[i]
            prefix.append(total)

        return prefix    