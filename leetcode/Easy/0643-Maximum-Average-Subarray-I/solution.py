# LeetCode Problem: Maximum Average Subarray I
# Link: https://leetcode.com/problems/maximum-average-subarray-i/
# Difficulty: Easy
# Language: python3

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total=0
        
        for i in range(k):
            total+=nums[i]
        ans=total/k
            


        for i in range(k,len(nums)):
            total=total-nums[i-k]
            total=total+nums[i] 

            avg=total/k

            if avg> ans:
                ans=avg

        return ans            