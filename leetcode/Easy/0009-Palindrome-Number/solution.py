# LeetCode Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Language: python

class Solution():
    def isPalindrome(self, num):
        original = num  # ✅ Original number ko store kiya
        reverse = 0
        
        for i in range(len(str(num))):  
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10  # ✅ Num update karna zaroori hai
        
        # ✅ Final comparison using `original`
        return reverse == original  # ✅ True ya False return karega

sol = Solution()
num = 21  # ✅ Yeh palindrome nahi hai
print(sol.isPalindrome(num))  # ✅ Output: False

num = 121  # ✅ Yeh palindrome hai
print(sol.isPalindrome(num))  # ✅ Output: True
