# LeetCode Problem: Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy
# Language: python3

class Solution:
    def merge(self, nums1, m, nums2, n):
        final = []

        for i in range(m):
            final.append(nums1[i])

        for i in range(n):
            final.append(nums2[i])

        final.sort()

        for i in range(m + n):
            nums1[i] = final[i]