# LeetCode Problem: Absolute Difference Between Maximum and Minimum K Elements
# Link: https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/
# Difficulty: Easy
# Language: python3

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        smallest=0
        largest=0
        for i in range(k):
            smallest+=nums[i]

        for j in range(len(nums)-k ,len(nums)) :
            largest+=nums[j]


        diff=abs(largest-smallest)

        return diff    
