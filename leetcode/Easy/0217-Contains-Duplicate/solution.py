# LeetCode Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Language: python3

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set()

        for i in nums:
            if i in result:
                return True

            result.add(i)

        return False