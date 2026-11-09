# LeetCode Problem: Build an Array With Stack Operations
# Link: https://leetcode.com/problems/build-an-array-with-stack-operations/
# Difficulty: Medium
# Language: python3

class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack=[]
        count=0
        for i in range(1,n+1):
            if i in target :
                stack.append("Push")
                count+=1

            else:
                stack.append("Push")
                stack.append("Pop")

            if count ==len(target):
                break    

        return stack             