# Subarray Sums Divisible by K

**Difficulty:** Medium  
**Topics:** Array, Hash Table, Prefix Sum  
**LeetCode URL:** [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

## Problem Description

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the number of non-empty <strong>subarrays</strong> that have a sum divisible by </em><code>k</code>.</p>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,5,0,-2,-3,1], k = 5
<strong>Output:</strong> 7
<strong>Explanation:</strong> There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5], k = 9
<strong>Output:</strong> 0
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>2 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution

```python3
# LeetCode Problem: Subarray Sums Divisible by K
# Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Difficulty: Medium
# Language: python3

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count=0
        prefix_sum=0
        rimender_count={0:1}

        for i in range (len(nums)):
            prefix_sum +=nums[i]

            rimender=prefix_sum % k

            if rimender in rimender_count:
                count+=rimender_count[rimender]
                rimender_count[rimender] += 1
            else:
                rimender_count[rimender] = 1

        return count

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
