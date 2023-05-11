# Append new string in the middle of a given string

# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.


# First, get the middle index number of s1 by dividing s1’s length by 2
# Use string slicing to get the character from s1 starting from 0 to the middle index number and store it in x
# concatenate x and s2. x = x + s2
# concatenate x and remeaning character from s1
# print x

def append_middle(s1, s2):
    print("Original Strings are", s1, s2)

    # middle index number of s1
    mi = int(len(s1) / 2)

    # get character from 0 to the middle index number from s1
    x = s1[:mi:]
    # concatenate s2 to it
    x = x + s2
    # append remaining character from s1
    x = x + s1[mi:]
    print("After appending new string in middle:", x)

append_middle("Ault", "Kelly")


