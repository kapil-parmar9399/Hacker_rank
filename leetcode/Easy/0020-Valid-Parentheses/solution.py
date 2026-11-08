# LeetCode Problem: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Language: python3

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)

            else:
                if len(stack) == 0:
                    return False

                if i == ')' and stack[-1] == '(':
                    stack.pop()

                elif i == '}' and stack[-1] == '{':
                    stack.pop()

                elif i == ']' and stack[-1] == '[':
                    stack.pop()

                else:
                    return False

        return len(stack) == 0