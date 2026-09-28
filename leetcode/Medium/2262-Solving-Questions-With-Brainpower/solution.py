# LeetCode Problem: Solving Questions With Brainpower
# Link: https://leetcode.com/problems/solving-questions-with-brainpower/
# Difficulty: Medium
# Language: python3

class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * (n + 1)  # Initialize a dp array of size n+1

        # Process the questions from the end to the start
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]

            # Option 1: Skip the current question
            skip = dp[i + 1]

            # Option 2: Solve the current question
            solve = points + (dp[i + brainpower + 1] if i + brainpower + 1 < n else 0)

            # Take the maximum of skipping or solving
            dp[i] = max(skip, solve)

        return dp[0]  # The answer is the maximum points starting from question 0


# Example usage:
questions = [[3, 2], [4, 3], [4, 4], [2, 5]]  # Example input
sol = Solution()  # Creating an object of the Solution class
result = sol.mostPoints(questions)  # Getting the maximum points

print(result)  # Output the result
