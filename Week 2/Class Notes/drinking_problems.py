
# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.

# Examples: (Input --> Output)
# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky"

# UPER
# Understand, Plan, Execute, Refactor

# Understand
# Input: An age object. This will be an integer!
# Output needs to be a String: The drink which the person is able to order/drink
# If they are age<14 or younger, they drink "toddy"
# If ther are 14-18, they drink "coke"
# If they are 18-21, they drink "beer"
# 21+: They drink "Whiskey"

# Plan
# Make sure the age is an integer
# Conditional statement:If age < 14: return 'drink toddy'
# Elifs to chain together my conditionals so we don't have to recheck elif < 18: return 'drink coke'

# Execute
def solution(age):
    age = int(age)
    if age < 14:
        return 'drink toddy'
    elif age < 18:
        return 'drink coke'
    elif age < 21:
        return 'drink beer'
    else:
        return 'drink whiskey'
    
print(solution(10))