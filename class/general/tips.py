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
