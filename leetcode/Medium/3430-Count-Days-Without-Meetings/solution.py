# LeetCode Problem: Count Days Without Meetings
# Link: https://leetcode.com/problems/count-days-without-meetings/
# Difficulty: Medium
# Language: python

class Solution:
    def countDays(self, days, meetings):
        if not meetings:
            return days

        # Step 1: Sort meetings by start time
        meetings.sort()

        # Step 2: Merge overlapping intervals
        merged = []
        for start, end in meetings:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        # Step 3: Calculate total days covered by meetings
        meeting_days = 0
        for start, end in merged:
            meeting_days += end - start + 1

        # Step 4: Available days = total - meeting_days
        return days - meeting_days
