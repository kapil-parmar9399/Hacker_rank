# LeetCode Problem: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Language: python3

class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_price

            if profit > max_profit:
                max_profit = profit

            if prices[i] < min_price:
                min_price = prices[i]

        return max_profit