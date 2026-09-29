# LeetCode Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Language: python3



class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev = ""

        for i in range(len(s) - 1, -1, -1):
            rev += s[i]

        if rev == s:
            return True
        else:
            return False
            if reverse==x:
                print("true")

            else:
                print("flase")    