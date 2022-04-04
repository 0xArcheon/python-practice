class Student:
    name = "Joseph"
    def study(self):
        print(self.name + " is studying. Please do not disturb")
s = Student() # Creating a new object of Student type
s.study() #calling the study method inside Student class

## class using __init__() method
class Professor:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub
    def teach(self):
        print('Hello, students, I am ' + self.name + " and I will teach " + str(self.sub))
p = Professor("Dr. Nakamoto", "Algorithms")
p.teach()

# Using Inheritance and overriding
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hi, It's ",self.name)
class Employee(Person):
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title
    def greet(self): #Overriding greet() method from parent class
        print("Hi, It's ",self.name, " and I'm a ",self.job_title)

employee = Employee('Lucas', 'Python Developer')
employee.greet()

#method overloading
def multi(x, y):
    p = x * y
    print(p)
def product(x, y, z):
    p = x*y*z
    print(p)

# isinstance method
class Calculation1:
    def Summation(self,a,b):
        return a+b
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived (Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b
d = Derived()
print(isinstance(d, Derived)) 
print(isinstance(d, Calculation1)) 
print(isinstance(d, Calculation2)) 