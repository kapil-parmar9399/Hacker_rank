# LeetCode - Mock Assessment

**Difficulty:** Unknown  
**Topics:** N/A  
**LeetCode URL:** [LeetCode - Mock Assessment](https://leetcode.com/problems/2/)

## Problem Description



## Examples



## Constraints



## Solution

```python
# LeetCode Problem: LeetCode - Mock Assessment
# Link: https://leetcode.com/problems/2/
# Difficulty: Unknown
# Language: python

from collections import deque

class Solution:
    def cutOffTree(self, forest):

        trees = []

        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))

        trees.sort()

        def bfs(sr, sc, tr, tc):
            queue = deque([(sr, sc, 0)])
            visited = {(sr, sc)}

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            while queue:
                r, c, steps = queue.popleft()

                if r == tr and c == tc:
                    return steps

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < len(forest) and
                        0 <= nc < len(forest[0]) and
                        forest[nr][nc] != 0 and
                        (nr, nc) not in visited):

                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))

            return -1

        current_r = 0
        current_c = 0
        total_steps = 0

        for height, r, c in trees:

            steps = bfs(current_r, current_c, r, c)

            if steps == -1:
                return -1

            total_steps += steps

            current_r = r
            current_c = c

            forest[r][c] = 1

        return total_steps
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
