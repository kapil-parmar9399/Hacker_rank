# LeetCode Problem: Maximum Average Subarray I
# Link: https://leetcode.com/problems/maximum-average-subarray-i/
# Difficulty: Easy
# Language: python3

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = 0

        for i in range(k):
            total += nums[i]

        max_avg = total / k

        for i in range(k, len(nums)):
            total = total - nums[i-k] + nums[i]

            avg = total / k

            if avg > max_avg:
                max_avg = avg

        return max_avg