# LeetCode Problem: Find Target Indices After Sorting Array
# Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Difficulty: Easy
# Language: python3

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:    
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)

        return result        