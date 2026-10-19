# LeetCode Problem: Maximum Count of Positive Integer and Negative Integer
# Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
# Difficulty: Easy
# Language: python3

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        positive=0
        negative=0

        for i in range(len(nums)):
            if nums[i]<0:
                negative+=1

            elif nums[i]>=1:
                positive+=1

        if positive >negative:
            return positive

        elif positive==negative:
            return positive

        else:
            return negative               
