# Maximum Product of Three Numbers

**Difficulty:** Easy  
**Topics:** Array, Math, Sorting  
**LeetCode URL:** [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>Find three numbers whose product is <strong>maximum</strong> and return the <strong>maximum</strong> product.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,-3]</span></p>

<p><strong>Output:</strong> <span class="example-io">-6</span></p>

<p><strong>Explanation:</strong></p>

<p>The only three numbers are 1, 2, and -3, so the maximum product is <code>1 * 2 * -3 = -6</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">24</span></p>

<p><strong>Explanation:</strong></p>

<p>The largest product comes from the three greatest numbers: <code>2 * 3 * 4 = 24</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-1,-2,-3]</span></p>

<p><strong>Output:</strong> <span class="example-io">-6</span></p>

<p><strong>Explanation:</strong></p>

<p>The only three numbers are -1, -2, and -3, so the maximum product is <code>(-1) * (-2) * (-3) = -6</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;=&nbsp;10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

## Constraints



## Solution

```python3
# LeetCode Problem: Maximum Product of Three Numbers
# Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
# Difficulty: Easy
# Language: python3

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]

        return max(a, b)   
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
