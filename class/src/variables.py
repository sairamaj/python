######################################
#       Variables
#           Numbers
#           Strings
#           Lists
######################################
a = 1
b = 2

print(a)
print(b)

# We can redefine the same variable
a = 1.1
print(a)

a = "this is string"
print(a)

# list of integers
a = [1,2,3,4,5]
print(a)

a = ["one", "two", "three", "four"]
print(a)
print(a[0])

# Slicing of the lists
# [<startindex>:<endindex not including>]
print(a[:])  # all

print(a[1:3])
print(a[-1])    # last one

print(len(a))
print("Length:" , "also part of print", "also another", len(a))

# List in lists
list1 = [1,3,5]
list2 = [2,4,6]

newList = [list1, list2]
print(newList)
