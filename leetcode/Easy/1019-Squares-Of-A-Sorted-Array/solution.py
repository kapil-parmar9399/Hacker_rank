# LeetCode Problem: Squares of a Sorted Array
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Difficulty: Easy
# Language: python3

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        all_square=[]
        for i in range(len(nums)):
            sqr=nums[i]*nums[i]
            all_square.append(sqr)

        all_square.sort()
        return all_square    
