# create a class
class Person:
    name = "sai"
    def someFunc(self):
        print("some func:", self.name)

# class itself is object
print(Person.name)
print(Person.someFunc)

# create new object
x = Person()
print(x.name)
x.name = "ram"
Person.someFunc(x)


# initialization (like constructors in other languages)
class Person2:
    name = "sai"
    def __init__(self):
        print("in Person2.init")

x1 = Person2()
x2 = Person2()

# init method with arguments
class Person3:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name: {self.name} age:{self.age}")

x3 = Person3("sai",16)
x4 = Person3("ram",18)
x3.display()
x4.display()

# creating data attributes on the fly
class Person4:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name: {self.name} age:{self.age} gender:{self.gender}")

x5 = Person4("krishna",19)
x5.gender = 'M'     # added new data attribute
x5.display()

# Calling method thorugh class
Person4.display(x5)

## Class variables (ex: static in C)
class Person5:
    name = "name shared by all objects of Person5"  
    def __init__(self):
        self.name = "objectlevel"  # object level

    def display(self):
        print(f"name: {Person5.name} name of instance:{self.name}")
x6 = Person5()
x6.name = "namespecifictoinstance"
x6.display()

# printing class of the object
print(x6.__class__)

# Inheritance
class Person6(Person5):
    pass

x7 = Person6()
x7.display()

## working with iterations
l = [1,2,3]
x = iter(l)
print(next(x))
print(next(x))
print(next(x))
#print(next(x))  # Stop iteration exception


# implementing iterator
class Test:
    def __init__(self):
        self.val = 10
        self.done = False

    def __iter__(self):     # this will make the Test as iterator
        return self
    
    def __next__(self):     # this will be called for each in for loop 
        if(self.done):
            raise StopIteration     # end of the iterations.
        self.done = True 
        return self.val
for x in Test():
    print(x)        

# implementing iterator using generator


