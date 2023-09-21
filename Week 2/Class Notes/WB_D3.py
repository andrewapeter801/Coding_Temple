# Don't give me five!
# In this kata you get the start number and the end number of a region and should
# return the count of all numbers except numbers with a 5 in it. The start and the
# end number are both inclusive!
# Examples:
# 1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
# 4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
# The result may contain fives. ;-)
# The start number will always be smaller than the end number. Both numbers can be
# also negative!

#UPER

#Understand - 
    #Input: two integer values = lower and upper bounds of the range.
    #Output: Return count of numbers excluding the number '5'

#Plan - define function as num: str, if '5' not in number, add num to count, create count = +1 starnuting count = 0

def solution(num_1, num_2):
    num_count = 0
    for num in range(num_1, num_2 +1):
        if '5' not in str(num):
            num_count += 1
range_of_num = solution(1,12)

print(range_of_num)
