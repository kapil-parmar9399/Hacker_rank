# Remove Duplicates from Sorted List II

**Difficulty:** Medium  
**Topics:** Linked List, Two Pointers  
**LeetCode URL:** [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem Description

<p>You are given the <code>head</code> of a <strong>sorted</strong> linked list.</p>

<p>Delete all nodes that have <strong>duplicate</strong> numbers, leaving only <strong>distinct</strong> numbers from the original list.</p>

<p>Return the linked list <strong>sorted</strong> as well.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,3,4,4,5]
<strong>Output:</strong> [1,2,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg" style="width: 500px; height: 205px;" />
<pre>
<strong>Input:</strong> head = [1,1,1,2,3]
<strong>Output:</strong> [2,3]
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 300]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>The list is guaranteed to be <strong>sorted</strong> in ascending order.</li>
</ul>

## Solution

```python3
# LeetCode Problem: Remove Duplicates from Sorted List II
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Difficulty: Medium
# Language: python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        freq={}
        current=head
        while current is not None :
            if current.val in freq:
                freq[current.val]+=1

            else:
                freq[current.val]=1 
            current=current.next           


        arr=[]
        for value in freq:
            if freq[value] == 1:
                arr.append(value)

        dummy=ListNode(0)
        current=dummy

        for value in arr:
            current.next=ListNode(value) 
            current=current.next
        return dummy.next       
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
