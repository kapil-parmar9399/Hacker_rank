# LeetCode Problem: Number of Steps to Reduce a Number to Zero
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Difficulty: Easy
# Language: python3

class Solution:
    def numberOfSteps(self, num: int, count: int = 0) -> int:

        if num == 0:
            return count

        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1

        count += 1

        return self.numberOfSteps(num, count)