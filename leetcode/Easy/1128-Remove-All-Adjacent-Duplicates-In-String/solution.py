# LeetCode Problem: Remove All Adjacent Duplicates In String
# Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Difficulty: Easy
# Language: python3

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in s :
            if len(stack)==0 :
                stack.append(i)

            elif stack[-1] == i:
                stack.pop()


            else:
                stack.append(i)


        return "".join(stack)     
