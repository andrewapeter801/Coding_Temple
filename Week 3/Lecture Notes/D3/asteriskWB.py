# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
# Example
# For
# picture = ["abc",
#            "ded"]
# the output should be
# solution(picture) = ["*****",
#                      "*abc*",
#                      "*ded*",
#                      "*****"]
# Input/Output
# [execution time limit] 4 seconds (py3)
# [memory limit] 1 GB
# [input] array.string picture
# A non-empty array of non-empty equal-length strings.
# Guaranteed constraints:
# 1 ≤ picture.length ≤ 100,
# 1 ≤ picture[i].length ≤ 100.
# [output] array.string
# The same matrix of characters, framed with a border of asterisks of width 1.

#UPER

# Understand
# - putting  ****** before and after the strings
# - x = []

def solution(picture):
    x = ["*"]*(len(max(picture))+2)
    x = ''.join(x)
    l = [x]
    print(x)
    for i in picture:
        l.append('*' +i+ '*')

        l.append(x)
        return l


print(solution(['abc', 'ded']))


