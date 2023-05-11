#  Reverse a given string

# Show Hint
# Use negative slicing
# Or use the built-in function reversed().

# Solution 1: Negative String slicing

str1 = "PYnative"
print("Original String is:", str1)

str1 = str1[::-1]
print("Reversed String is:", str1)


# Solution 2: Using the reversed() function

str1 = "PYnative"
print("Original String is:", str1)

str1 = ''.join(reversed(str1))
print("Reversed String is:", str1)