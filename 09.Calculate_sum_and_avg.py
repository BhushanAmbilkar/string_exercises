# Calculate the sum and average of the digits present in a string

# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

# Show Hint
# Iterate each character from a string s1 and check if the current character is digit using the isdigit() function

# Show Solution
# Solution 1: Use string functions

# Iterate each character from a string s1 using a loop
# In the body of a loop, check if the current character is digit using the isdigit() function
# If it is a digit, then add it to the sum variable
# In the end, calculate the average by dividing the total by the count of digits


input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)


# Solution 2: Use regular expression


import re

input_str = "PYnative29@#8496"
digit_list = [int(num) for num in re.findall(r'\d', input_str)]
print('Digits:', digit_list)

# use the built-in function sum
total = sum(digit_list)

# average = sum / count of digits
avg = total / len(digit_list)
print("Sum is:", total, "Average is ", avg)
