#Class : It is a user defined blueprint or prototype
#prototypes or methods : Sum, multiplication, division

#A class will have methods, class variables, instance variables, constructors
#Objects for your classes..
#new keyword is not required for creating the object
#the functions which are used inside the classes is called Methods

#constructor is a method which is automatically called when we create an object for class
#default constructor
#name :__init__()

#Class variables : which is created inside a call
#instance variables: Which is created inside a constructor

#self keyword is mandatory for calling variables names into method


class Calculator:
    num = 100
    def __init__(self):
        print("Constructor called")

    def getData(self):
        print("calculator")

    def add(self,a,b):
        print(a+b)

obj = Calculator() #it is a object created for class
obj.getData()
print(obj.num)
obj.add(2,5)









