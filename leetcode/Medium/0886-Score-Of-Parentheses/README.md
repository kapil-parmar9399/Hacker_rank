# Score of Parentheses

**Difficulty:** Medium  
**Topics:** String, Stack, Bracket Sequences  
**LeetCode URL:** [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)

## Problem Description

<p>Given a balanced parentheses string <code>s</code>, return <em>the <strong>score</strong> of the string</em>.</p>

<p>The <strong>score</strong> of a balanced parentheses string is based on the following rule:</p>

<ul>
	<li><code>&quot;()&quot;</code> has score <code>1</code>.</li>
	<li><code>AB</code> has score <code>A + B</code>, where <code>A</code> and <code>B</code> are balanced parentheses strings.</li>
	<li><code>(A)</code> has score <code>2 * A</code>, where <code>A</code> is a balanced parentheses string.</li>
</ul>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()&quot;
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(())&quot;
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()()&quot;
<strong>Output:</strong> 2
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 50</code></li>
	<li><code>s</code> consists of only <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>.</li>
	<li><code>s</code> is a balanced parentheses string.</li>
</ul>

## Solution

```python3
# LeetCode Problem: Score of Parentheses
# Link: https://leetcode.com/problems/score-of-parentheses/
# Difficulty: Medium
# Language: python3

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                x = stack.pop()

                if x == 0:
                    x = 1
                else:
                    x = 2 * x

                stack[-1] += x

        return stack[0]
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
