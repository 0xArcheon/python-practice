name= input("Enter your name: ") #taking a string value as user name
roll= int(input("Enter your Roll No: ")) #taking roll no as integer input
print("Name of the student: "+name, type(name)) #using type() method to get the datatype of user input
print("Roll No. of the student: "+str(roll), type(roll)) #using str() for concatenation of int 
if(roll<=15 and roll>0):
    print(name+", You are selected in group A")
elif(roll>30 or roll==0):
    print(name+ ", You have entered an invalid Roll No")
else:
    print(name+", You are selected in group B")