# 3Sum Closest

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Sorting  
**LeetCode URL:** [3Sum Closest](https://leetcode.com/problems/3sum-closest/)

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>target</code>.</p>

<p>Find three integers at <strong>distinct indices</strong> in <code>nums</code> such that the sum is <strong>closest</strong> to <code>target</code>.</p>

<p>Return the sum of the three integers.</p>

<p>You may assume that each input would have <strong>exactly</strong> one solution.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,2,1,-4], target = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0], target = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 500</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution

```python3
# LeetCode Problem: 3Sum Closest
# Link: https://leetcode.com/problems/3sum-closest/
# Difficulty: Medium
# Language: python3


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum

                if current_sum == target:
                    return current_sum

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

        return closest

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
