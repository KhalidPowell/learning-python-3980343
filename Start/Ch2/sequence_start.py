# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values


# to access a member of a sequence type, use []
mylist = [1,"house", False, 3.8]

# add a list to another list

anotherlist = ["main"]

mylist = mylist + anotherlist

# use slices to get parts of a sequence

print(mylist[1:4])

print(mylist[-2])

# you can use slices to reverse a sequence


# Tuples are like lists, but they are immutable


# Sets are also sequences, but they contain unique values

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
