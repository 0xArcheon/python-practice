#Creating different types of tuples
intTuple = (32, 1024, 1600, 433) #Tuple with a integer values
print(intTuple)
mixTuple = ("Guwahati", "New Delhi", 26.5, False) #Tuple having mixed datatypes
print(mixTuple)
nestTuple = ((0,1,10,11),"BTC","ETH",[43000, 2800]) #Nested tuple
print(nestTuple)

#Creating tuples without parenthesis
ezTuple = "Mango", "Orange", 150
print(ezTuple)

#Tuple unpacking
fruit1, fruit2, price = ezTuple
print(fruit1)
print(price, "Rs")

#Insertion and deletion of tuple elements
#Python tuples are immutable so we can't directly add, delete or update items

#Delete entire tuple
del ezTuple

#Built in tuple methods
myTuple = ("Sergio Ramos", "Robert Lewandowsky", "Isco", "Toni Kroos","Isco")
print(myTuple.count("Isco")) #Returns the number of times the specified element appears in the tuple
print(myTuple.index("Sergio Ramos")) #returns the index of the specified element in the tuple

#Creating a dictionary
emptyDict = {} #Empty dictionary
sports = {1: 'Football', 2: 'Cricket'} #Dictionary with integer keys
mixDict = {'name': 'John', 1: [2, 4, 3]} #Dictionary with mixed keys

#Insertion and Deletion
sports[3] = "Hockey"
sports[4] = "Golf"
sports[5] = "Formula 1"
print(sports)

del sports[5] #del keyword is used to delete 
print(sports)

#Updating dictionary data
sports[4] = "Volleyball"
print(sports)

#Built in dictionary methods
print(sports.get(1)) #get() returns the value of the specified key
print(sports.items()) #Returns a list containing a tuple for each key value pair
print(sports.keys()) #Returns a list containing the dictionary's keys
sports.pop(4) #Removes the element with the specified key
#Error in line 51 - TypeError: pop expected at least 1 argument, got 0. Fixed by providing an argument inside pop()
print(sports)