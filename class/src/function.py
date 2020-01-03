######################################
#       functions
#       indentation
######################################


def feb(n):
    a, b = 0, 1
    result = []
    print(a, b)
    while a < n:
        result.append(a)
        c = a+b
        a = b
        b = c
        print(a, b)
    return result


print(feb(9))

# default arguments


def func(x, y=2, msg="this"):
    print(x, y, msg)


#   func()      - error as first parameter does not have default
func(10)
func(10, 5)
func(10, 6, "new message")

# using named arguments
func(x=4, msg="some message")

# Positional and Keyword

# Positional only
def myposFunc(num , /):
    print(num)
myposFunc(1)
# myposFunc(num=2)  # error cannot use keyword

# Keyword only
def mykeyWordFunc(*, num):
    print(num)

mykeyWordFunc(num=2)
# mykeyWordFunc(5)   # error cannot use positional

def normalFunc(num):
    print(num)

normalFunc(3)           # positional
normalFunc(num=10)      # keyword

def bothPosOnlyAndKeyWordOnlyFunc(num1, / , anything, * , num2):
    print(num1, anything, num2)

bothPosOnlyAndKeyWordOnlyFunc(10, "somval", num2=11)
# bothPosOnlyAndKeyWordOnlyFunc(10, "somval", 11)     # error num2 cannot be passed as positional
# bothPosOnlyAndKeyWordOnlyFunc(num1=5,"someval", num2=12) # num1 cannot be used as keyword

# variabe arguments
def concat(*args, sep = '/'):
    return sep.join(args)

print(concat('abc'))
print(concat('abc','123', sep='/'))

# Unpacking arguments
# from list or tuple to separate arguments
x = [2,5]
print(list(range(2,5)))
print(list(range(*x)))  # equivalent to the above. Here x has been unpacked.

# same way dictionaries can be unpacked with *
def myfunc3(x, y, z):
    print(x,y,z)

myfunc3(1,2,3)
args = { "x":1, "y":2, "z": 3}
myfunc3(**args) # same as calling myfunc3(1,2,3)

# Document strings
def func10():
    "document string"
    print("hello")

func10()

# Coding styles
# https://www.python.org/dev/peps/pep-0008/

