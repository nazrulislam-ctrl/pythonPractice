x=10

def my_function():
    global x
    x= 4 #this will change the value of the global variable
    y=5
    print(y)

my_function()
print(x)
# print(y) #y will cause an error because y is not defined as a global variable