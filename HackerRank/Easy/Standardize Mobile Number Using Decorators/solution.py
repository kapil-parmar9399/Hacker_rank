# HackerRank Problem: Standardize Mobile Number Using Decorators
# Link: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
# Difficulty: Easy
# Language: python3

def wrapper(f):
    def fun(l):
        # mobile numbers ko +91 XXXXX XXXXX format mein convert karo
        l = ["+91 " + x[-10:-5] + " " + x[-5:] for x in l]
        return f(l)
    return fun

