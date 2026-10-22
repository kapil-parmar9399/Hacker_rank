# LeetCode Problem: Maximum Product Subarray
# Link: https://leetcode.com/problems/maximum-product-subarray/
# Difficulty: Medium
# Language: python3

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product=nums[0]

        for i in range(len(nums)):
            product=1

            for j in range(i,len(nums)):
                product*=nums[j]


                if product> max_product:
                    max_product=product

        return max_product            
