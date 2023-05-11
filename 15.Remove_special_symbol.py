# Remove special symbols / punctuation from a string

# Show Hint
# Use string functions translate() and maketrans()

# Use the translate() function to get a new string where specified characters are replaced with the character described in a dictionary or a mapping table.
# Use the maketrans() function to create a mapping table.
# Or Use the regex in Python. See Python regex replace.


# Solution 1: Use string functions translate() and maketrans().

# The string.punctuation constant contain all special symbols.

import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)


# Solution 2: Using regex replace pattern in a string

import re

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is ", res)



