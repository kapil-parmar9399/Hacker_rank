# LeetCode - Mock Assessment

**Difficulty:** Unknown  
**Topics:** N/A  
**LeetCode URL:** [LeetCode - Mock Assessment](https://leetcode.com/problems/1/)

## Problem Description



## Examples



## Constraints



## Solution

```python
# LeetCode Problem: LeetCode - Mock Assessment
# Link: https://leetcode.com/problems/1/
# Difficulty: Unknown
# Language: python

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = paragraph.lower()

        for ch in "!?',;.":
            words = words.replace(ch, " ")

        words = words.split()

        count = {}

        for word in words:
            if word not in banned:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1

        max_word = ""

        for word in count:
            if max_word == "" or count[word] > count[max_word]:
                max_word = word

        return max_word
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
