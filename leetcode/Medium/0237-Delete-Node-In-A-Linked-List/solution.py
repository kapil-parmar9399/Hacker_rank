# LeetCode Problem: Delete Node in a Linked List
# Link: https://leetcode.com/problems/delete-node-in-a-linked-list/
# Difficulty: Medium
# Language: python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next