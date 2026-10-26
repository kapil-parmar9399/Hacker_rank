# LeetCode Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Language: python3


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        count = 0

        for i in range(len(s)):
            if s[i] not in longest:
                longest = longest + s[i]
            else:
                index = longest.index(s[i])
                longest = longest[index + 1:]
                longest = longest + s[i]

            count = max(count, len(longest))

        return count