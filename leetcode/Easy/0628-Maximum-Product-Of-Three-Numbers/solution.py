# LeetCode Problem: Maximum Product of Three Numbers
# Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
# Difficulty: Easy
# Language: python3

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]

        return max(a, b)   