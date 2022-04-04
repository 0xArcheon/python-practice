#Creating a function without parameter
def sayHi():
    print("Hi Stranger")
sayHi()

#Creating a function which takes a string as parameter and without return statement
def sayHello(fname): 
    print("Hello",fname) 
sayHello("Walter")

#Creating a function with a return statement
def getKelvin(temp):
    '''Simple function that converts degree celcius unit temperature into Kelvin'''
    return temp+273.15
print("Converted temperature: ",getKelvin(24), "kelvin")

#Functions with different argument types
#Function with Default arguments
def welcome(lastname, firstname="Mr."): 
    '''This function prints a welcome message to the user.
    If the user doesn't provide first name, then it's set to print "Mr." by default'''
    print("Welcome back,",firstname,"",lastname)
welcome("White", "Walter")
welcome("Pinkman")

#Function with keyword arguments
def easytolearn(lang1, lang2): 
    '''This function prints a statement'''
    print(lang1, "is easier to learn than",lang2)
easytolearn("Java", "Python") #Order of the arguments matter
easytolearn(lang2="Java",lang1="Python") #This way the order of the arguments do not matter

#Function with Arbritrary arguments
def add(*num):
    '''This function takes multiple input values and calculates their sum using a for loop'''
    sum=0
    for i in num:
        sum = sum+i
    return sum
print("Total:",add(74,67,91,64)) #Passing multiple integer values as arguments
print("Total:",add(10,5))

#Function without any arguments and a return statment
def area():
    '''This function returns multiplication of length and breadth'''
    length = 25
    breadth = 13
    return length*breadth
print("Area of rectangle:",area(),"units")
    










