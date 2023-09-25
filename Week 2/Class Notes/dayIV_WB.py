# SUM OF SMALLEST NUMBERS
# Given a 2D ( nested ) list/array of size m * n, your task is to find the sum of the minimum values in each row.
# For Example:
# INPUT: [[ 1, 2, 3, 4, 5 ],[ 5, 6, 7, 8, 9 ],[ 20, 21, 34, 56, 100 ]]
# OUTPUT:26
# [ [ 1, 2, 3, 4, 5 ] # minimum value of row is 1
# , [ 5, 6, 7, 8, 9 ] # minimum value of row is 5
# , [ 20, 21, 34, 56, 100 ] # minimum value of row is 20
# ]
# So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.
# Note: You will be always given non-empty list containing Positive values.
# INPUT: [[ 7, 9, 8, 6, 2 ], [ 6, 3, 5, 4, 3 ], [ 5, 8, 7, 4, 5 ]]
# OUTPUT: 9
# INPUT [[ 11, 12, 14, 54 ], [ 67, 89, 90, 56 ], [ 7, 9, 4, 3 ], [ 9, 8, 6, 7 ]]
# OUTPUT: 76

#UPER
#Understand
# Each list of the input is a column within the row, each value in the list is like a row.
# determine the min value in each row
# sum the min values
# sum of the min output = 26

# Plan
# use min function for each array
#min (input[0])
#for i in input min [i]
# Create a sum variable  s=0 add to s in loop

# Execute

def sum_of_min(INPUT):
    s = 0
    for i in INPUT:
        s += min(i)
    return s 

print(sum_of_min([ 1, 2, 3, 4, 5 ],[ 5, 6, 7, 8, 9 ],[ 20, 21, 34, 56, 100 ]))