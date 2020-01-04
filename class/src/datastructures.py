# list
l = [1,2,3,4]

# list as stack
print(l.pop())
print(l.pop())

# list as queue
# can be done but inefficient
# use queue
from collections import deque
queue = deque([1,2,4])
print(queue.popleft())

# list comprehension
squares = [x**2 for x in range(10)]
print(squares)

# A list comprehension consists of brackets containing an expression followed by a for clause, 
# then zero or more for or if clauses. 
# The result will be a new list resulting from evaluating the expression 
# in the context of the for and if clauses which follow it. 
# For example, this listcomp combines the elements of two lists if they are not equal:
val = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(val)

# del to remove from list and also to remove variable
z = 10
del z
# print(z)       no variable z as it has been deleted.

# Tuple
# list of heterozenious values
# immutable (where as lists are mutable)
x = (1,2,"val")
print(x)

y = ()      # empty tuple
y = (1,)    # tuple with one value

t = 1,2,6   # tuple packing
print(t)

x,y,z = t   # tuple unpacking
print(x,y,z)


# sets (unordered list, no duplicates)
fruits = {"orange", "banana","apple","apple"}
print(fruits)  # apple exists as only one 

a = set('abracadabra')
b = set('alacazam')
print("a-b", a-b)
print("a|b", a|b)
print("a&b", a&b)
print("a^b", a^b)       # letters in a or b but not both

# Dictionaries
testItems = {"one":1, "two":2, "three":3}
print(testItems)
print(list(testItems))
print("one" in testItems)
print("four" in testItems)

for k,v in testItems.items():
    print(k,v)

# zip to to combine to iterations in to one iterations
x = ["one","two","three"]
y = [1,2,3]

z = zip(x,y)
for a,b in z:
    print(a,b)