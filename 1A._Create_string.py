# Write a program to create a new string made of an input string’s first, middle, and last character.

# Use string indexing to get the character present at the given index.
# Use str1[0] to get the first character of a string and add it to the result variable
# Next, get the middle character’s index by dividing string length by 2. x = len(str1) /2. Use str1[x] to get the middle character and add it to the result variable
# Use str1[len(str1)-1] to get the last character of a string and add it to the result variable
# print result variable to display new string

str1 = input("Enter s String: ")
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)