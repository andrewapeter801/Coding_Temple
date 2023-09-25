#UPER

#understand
# Wanting to test an array the variable for sum of negative numbers and count positive int.

#plan
# Step 1 - set up variables
# Step 2 - write a for loop for positive numbers that checks the count
# Step 3 - write if variable to check if number is positive or negative
# Step 4 - return an array

def count_positives_sum_negatives(arr):
    positive_numbers = 0
    negative_numbers = 0
    if len(arr) <= 0: 
        return []
    
    for num in arr:
        if num > 0:
            positive_numbers += 1
        elif num < 0:
            negative_numbers += num
    return[positive_numbers, negative_numbers]
        
