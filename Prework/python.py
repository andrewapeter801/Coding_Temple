#Question 1:
#Write a function to print “hello_USERNAME!” USERNAME is the input of the function. 
#The first line of the code has been defined as below.
def first_odds():
    user = "USERNAME"
    print("hello_" + (user))

first_odds()

# Question 2:
# Write a Python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    odd_numbers = list(range(1, 100, 2))
    print(odd_numbers)

first_odds()

#"""Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list. 
#The first line of the code has been defined below."""
def max_num_in_list():
    l = list[3, 2, 10, 5, 6, 7]
    max_l = max(l)
    print(max_l)

max_num_in_list()

# """Question 4:
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false)."""
def is_leap_year():
    number = input("Is this a leap year?: ")
    number = int(2023)
    if number % 4  == 0:
        print("This is a leap year!")
    else:
        print("This is not a leap year.")

       

# """Question 5:
# Write a function to check to see if all numbers in the list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type"""

def is_consecutive(a_list):
    sorted(a_list)
    for index in range(len(a_list)-1):
        if a_list[index] > a_list[index+1]:
            print(False)
        elif a_list[index] + 1 != a_list[index+1]:
            print(True)
        
    print(True)
is_consecutive([1,2,4,5])



