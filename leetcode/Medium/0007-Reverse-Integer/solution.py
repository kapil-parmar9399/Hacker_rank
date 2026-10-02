# LeetCode Problem: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium
# Language: python3

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reverse = ""

        for i in str(abs(x)):
            reverse = i + reverse

        reverse = int(reverse) * sign

        if reverse < -(2**31) or reverse > 2**31 - 1:
            return 0

        return reverse