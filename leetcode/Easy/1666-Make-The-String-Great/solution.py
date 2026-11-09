# LeetCode Problem: Make The String Great
# Link: https://leetcode.com/problems/make-the-string-great/
# Difficulty: Easy
# Language: python3

class Solution:

    def makeGood(self, s: str) -> str:
        stack = []

        for i in s:
            if len(stack) == 0:
                stack.append(i)

            elif stack[-1].lower() == i.lower() and stack[-1] != i:
                stack.pop()

            else:
                stack.append(i)

        return "".join(stack)