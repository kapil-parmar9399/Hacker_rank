# LeetCode Problem: Subsets
# Link: https://leetcode.com/problems/subsets/
# Difficulty: Medium
# Language: python3

class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(index, current):
            if index == len(nums):
                result.append(current.copy())
                return

            current.append(nums[index])
            backtrack(index + 1, current)

            current.pop()
            backtrack(index + 1, current)

        backtrack(0, [])
        return result