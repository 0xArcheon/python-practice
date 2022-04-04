#Using continue statement to print even numbers from between 1 to 10
print("\ncontinue keyword in for loop")
for i in range(10):
    if(i%2 == 0):
        continue
    print(i+1)
else:
    print("Value of i is out of range") #else statement in for loop

#Using break statement to print the sum of integers till 5
print("\nBreak Statement")
num1 = 0
sum = 0
while(num1<=10):
    sum = sum+num1
    if(num1 == 5):
        break
    num1 = num1+1  
print("Sum:",sum)

#Using pass keyword to define a function that performs no action
print("\npass keyword")
def uselessFunction():
    pass
#using if elif and else statements
print("\nConditional statements")
uname = input("Enter your username:" )
if(uname == "Archeon"):
    print("Access Granted")
elif(uname == "imamlan03"):
    print("Access granted")
else:
    print("Access Denied")

#Some aritmetic operators
print("\nArithmetic operators")
num2 = 32
num3 = 512
sumOp = num2+num3 #Addition operator
print("Sum of %d and %d is %d"%(num2,num3,sumOp))
multi = num2*num3 #Multiplication operator
print("Product of %d and %d is %d"%(num2,num3,multi))
floorDiv = num2//5 #Floor division operator which rounds the result down to the nearest whole number
print("Floor division of %d by %d gives %d"%(num2,5,floorDiv))

#Some relational operators
print("\nRelational Operators")
if(num2 == num3):
    print("Equal")
else:
    print("Not Equal")

#Membership operators
print("\nMembership operators")
language = "Javascript"
if("Java" in language):
    print("Present")
else:
    print("Absent")

#Identity operators
if(num2 is not num3):
    print("They are different values")

#Logical operators
print("\nLogical Operators")
print(5>7 or 55!=432) #Prints true since one of the condition is true
print(not(5>7 or 55!=432)) #Prints False since the inside condition evaluates to true

#Bitwise Operators
print("\nBitwise operator")
a = 60 # 60 = 0011 1100 
b = 13 # 13 = 0000 1101 
c = 0
c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)
c = a | b;        # 61 = 0011 1101 
print ("Line 2 - Value of c is ", c)

#Assignment operators
print("\nAssignment operator")
x = 25
x+=5 #Same as x = x+5
print(x)

#Set operations
gpus ={"RTX 3060", "RTX 3070", "GTX 1080ti", "GT710"}
print("Graphics cards in stock: ",gpus)
gpus.add("RTX 3090") #adding elements
print("GPUs in stock (Updated): ",gpus)
gpus.remove("GT710") #deleting elements
#iterating through elements
for i in gpus:
    print(i)
oddNum = {1, 3,5, 7, 9}
evenNum = (2,4,6,8,10)
all= oddNum.union(evenNum) #Union operation
print("Integers: ",all)
diff = oddNum.difference(evenNum)
print(diff)