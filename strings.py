#String operations in Python
#Declaring strings using all quotation types
str1 = 'Hello'
str2 = "This is a"
str3 = '''Python 
        program'''
print(str1)
print(str2) 
print(str3)

#Using indexing on the declared strings
print("Third letter of the first string: "+str1[2])
print("Last letter in the first string: "+str1[-1])

#Operations on Strings
print(str1+", World!") 
print(str1*3) 
print(str3[0:6]) #Slicing

#String formatting operators
print("Hey %s, I'm %s and my Roll number is %d"%("Emily","Jake",22)) 

#String memberships
str4 = "AEIOU"
if("I" in str4 ):
    print("I is a member")
else:
    print("I is not a member")
if("O" not in str4 ):
    print("O is not present in 'AEIOU'")
else:
    print("O is present in 'AEIOU'")

#Use of some built in string methods
print(str4.lower()) #Converts all the characters into lowercase
print(str4.count("U")) #Counts the number of times a characters is present in a string
print(str4.find("I")) #Returns the index position of seached character
