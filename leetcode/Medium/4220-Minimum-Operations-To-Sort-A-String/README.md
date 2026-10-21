# Minimum Operations to Sort a String

**Difficulty:** Medium  
**Topics:** String  
**LeetCode URL:** [Minimum Operations to Sort a String](https://leetcode.com/problems/minimum-operations-to-sort-a-string/)

## Problem Description

<p data-end="244" data-start="156">You are given a string <code>s</code> consisting of lowercase English letters.</p>

<p>In one operation, you can select any <strong><span data-keyword="substring-nonempty">substring</span></strong> of <code>s</code> that is <strong>not</strong> the entire string and <strong>sort</strong> it in <strong>non-descending alphabetical</strong> order.</p>

<p>Return the <strong>minimum</strong> number of operations required to make <code>s</code> sorted in <strong>non-descending</strong> order. If it is not possible, return -1.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;dog&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>Sort substring <code>&quot;og&quot;</code> to <code>&quot;go&quot;</code>.</li>
	<li>Now, <code>s = &quot;dgo&quot;</code>, which is sorted in ascending order. Thus, the answer is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;card&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Sort substring <code>&quot;car&quot;</code> to <code>&quot;acr&quot;</code>, so <code>s = &quot;acrd&quot;</code>.</li>
	<li>Sort substring <code>&quot;rd&quot;</code> to <code>&quot;dr&quot;</code>, making <code>s = &quot;acdr&quot;</code>, which is sorted in ascending order. Thus, the answer is 2.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;gf&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>It is impossible to sort <code>s</code> under the given constraints. Thus, the answer is -1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>

## Constraints



## Solution

```python3
# LeetCode Problem: Minimum Operations to Sort a String
# Link: https://leetcode.com/problems/minimum-operations-to-sort-a-string/
# Difficulty: Medium
# Language: python3

class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0

        if len(s) == 2:
            return -1

        mn = min(s)
        mx = max(s)

        if s[0] == mn or s[-1] == mx:
            return 1

        for i in range(1, len(s) - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        return 3
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
