# HackerRank Problem: Time Conversion
# Link: https://www.hackerrank.com/challenges/time-conversion/problem
# Difficulty: Easy
# Language: python3

time = input()

hour = int(time[:2])
period = time[-2:]

if period == "AM":
    if hour == 12:
        hour = 0
else:
    if hour != 12:
        hour += 12

print(f"{hour:02d}{time[2:-2]}")

