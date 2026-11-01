# LeetCode Problem: Middle of the Linked List
# Link: https://leetcode.com/problems/middle-of-the-linked-list/
# Difficulty: Easy
# Language: python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count=0
        current =head
        while current  is not None:
            count+=1
            current = current.next
        mid=count//2
        current=head

        for i in range(mid):
            current=current.next

        return current     