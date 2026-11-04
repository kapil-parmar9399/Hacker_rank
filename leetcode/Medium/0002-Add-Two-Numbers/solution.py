# LeetCode Problem: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium
# Language: python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy

        current1 = l1
        current2 = l2
        carry = 0

        while current1 is not None or current2 is not None:

            val1 = 0
            val2 = 0

            if current1 is not None:
                val1 = current1.val

            if current2 is not None:
                val2 = current2.val

            total = val1 + val2 + carry

            if total > 9:
                carry = total // 10
                total = total % 10
            else:
                carry = 0

            current.next = ListNode(total)
            current = current.next

            if current1 is not None:
                current1 = current1.next

            if current2 is not None:
                current2 = current2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next