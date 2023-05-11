
#  Arrange string characters such that lowercase letters should come first

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# Create two lists lower and upper
# Iterate a string using a for loop
# In each loop iteration, check if the current character is the lower or upper case using the islower() string function.
# If a character is the lower case, add it to the lower list, else add it to the upper list
# to join the lower and upper list using a join() function.
# convert list to string
# print the final string

str1 = "PYnativE"
print('Original String : ', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list 
        lower.append(char)
    else:
        # add uppercase characters to lower list 
        upper.append(char)

# Join both list 
sorted_str = ''.join(lower + upper)
print("Result : ", sorted_str)  