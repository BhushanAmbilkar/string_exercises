# Write a program to find words with both alphabets and numbers from an input string.


# Show Hint
# Use the built-in function any() with the combination of string functions isalpha() and isdigit()


str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)
