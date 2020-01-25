import sys

def str2bool(v):
   return str(v).lower() in ("yes", "true", "t", "1")

isInteractive = True
if len(sys.argv) > 1:
    isInteractive = str2bool(sys.argv[1])

print(f'interactive {isInteractive}')

def checkAndWait():
    if isInteractive:
        input("press any key to continue...")

print('--------- get type of variable -------------')
# get type of varialbe
x = 1
print(type(x))
checkAndWait()

print('--------- different between lists and tuples -------------')
# Sequence data types that can store a collection of items
# list and tuples
### tuples and lists
# they look same
# item stored in a list or a tuple can be of any data type
# tuple are immutables

# list
x = [1,2,4]
print(type(x))
x[2] = 5
print(type(x))
# https://www.afternerd.com/blog/difference-between-list-tuple/
checkAndWait()

# tuple
x = (1,2,3)
print(type(x))

print('--------- location of object -------------')
# location of object
print(id(x))
checkAndWait()

print('--------- passing variable arguments -------------')
def variableArgs(*args):
    print(args)
variableArgs(1,2,3)
checkAndWait()

print('--------- passing variable arguments -------------')
def variableArgs2(a,b):
    print('a is',a)
    print('b is',b)

kwargs = {'a':'this is a', 'b': 'this is b'}
variableArgs2(**kwargs)

print('--------- list comprehentions -------------')
# they’re just for-loops over a collection expressed in a more terse and compact syntax



# values = [expression
#           for item in collection
#           if condition]

print([x*x for x in range(10)])
print([x*x for x in range(10) if x % 2 != 0])

# set comprehensions
print(set([x*x for x in range(10)]))
# dictionary comprehensions
print({x:x*x for x in range(10)})
#https://dbader.org/blog/list-dict-set-comprehensions-in-python

print('--------- set operations -------------')
# only immutable one will go in set
# unorder list
# duplicates removed
# union,interset
# https://snakify.org/en/lessons/sets/#section_4
x = {1,2,3,4,3,4}
print(x)
x = set('abcdef')
print(x)


# https://snakify.org/en/lessons/sets/