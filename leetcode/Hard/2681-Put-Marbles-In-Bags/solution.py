# LeetCode Problem: Put Marbles in Bags
# Link: https://leetcode.com/problems/put-marbles-in-bags/
# Difficulty: Hard
# Language: python

class Solution:
    def putMarbles(self, weights, k):
        n = len(weights)
        if k ==1:
            return 0
        pair_sum =[]
        for i in range(n-1):
            pair_sum.append(weights[i] +weights[i+1])
        pair_sum.sort()    
            
        min_score = sum(pair_sum[:k-1])
        max_score = sum(pair_sum[-(k-1):])

        return max_score - min_score
sol = Solution()
weights = [1, 3, 5, 5, 1]
k = 2
print(sol.putMarbles(weights, k))