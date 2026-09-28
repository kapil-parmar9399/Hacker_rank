# Merge Two Sorted Lists

**Difficulty:** Easy  
**Topics:** Linked List, Recursion  
**LeetCode URL:** [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem Description

<p>You are given the heads of two sorted linked lists <code>list1</code> and <code>list2</code>.</p>

<p>Merge the two lists into one <strong>sorted</strong> list. The list should be made by splicing together the nodes of the first two lists.</p>

<p>Return <em>the head of the merged linked list</em>.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;" />
<pre>
<strong>Input:</strong> list1 = [1,2,4], list2 = [1,3,4]
<strong>Output:</strong> [1,1,2,3,4,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = [0]
<strong>Output:</strong> [0]
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in both lists is in the range <code>[0, 50]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>Both <code>list1</code> and <code>list2</code> are sorted in <strong>non-decreasing</strong> order.</li>
</ul>

## Solution

```python3
# LeetCode Problem: Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Language: python3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Node value
        self.next = next  # Pointer to next node

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Base cases: If any list is empty, return the other list
        if not list1:  # Agar list1 khatam ho gayi ho
            return list2
        if not list2:  # Agar list2 khatam ho gayi ho
            return list1

        # Compare first nodes of list1 and list2
        if list1.val < list2.val:  # Agar list1 ka value chhota ho list2 ke comparison me
            list1.next = self.mergeTwoLists(list1.next, list2)  # list1 ka next element merge karo
            return list1  # list1 ko return karo
        else:  # Agar list2 ka value chhota ho list1 se
            list2.next = self.mergeTwoLists(list1, list2.next)  # list2 ka next element merge karo
            return list2  # list2 ko return karo

# Function to print the linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")  # Correct syntax for Python 3.x
        head = head.next
    print("None")

# Creating linked lists:
# list1: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))

# list2: 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merging both lists
sol = Solution()
merged_head = sol.mergeTwoLists(list1, list2)

# Printing the merged linked list
print_list(merged_head)

        
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
