# LeetCode Problem: Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium
# Language: python3

class Solution:
    def removeNthFromEnd(self, head, n):
        count = 0
        current = head

        while current is not None:
            count += 1
            current = current.next

        dlt = count - n

        if dlt == 0:
            return head.next

        current = head

        for i in range(dlt - 1):
            current = current.next

        current.next = current.next.next

        return head