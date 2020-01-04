name = "sai"
age = 16

# using expressions
print(f"my name is: {name} and age {age}")
print(f"my name is: {name:10} and age {age:10d}")

# str() , repr()
t = (1,"test")
print(str(t))

# 
x = 65
# !a ascii !s str()   !r  repr()
print(f"my name is: {x!a} and age {age}")
# using format
print("{0} and {1}".format(name,age))

# create math table
table = 5
for x in range(1,11):
    print("{0:3d} X {1:3d} = {2:3d}".format(table, x, table*x))

#writing to file
with open('c:\\temp\\test.txt','w') as f:
    f.writelines(["first line","second line"])

# read to file
with open('c:\\temp\\test.txt','r') as f:
    for l in f.readlines():
        print(l)

# JSON
l = ["one", "two", "three"]
import json
print(json.dumps(l))
with open('c:\\temp\\test.txt','w') as f:
    f.write(json.dumps(l))


