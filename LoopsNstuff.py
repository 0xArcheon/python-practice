#Creating a list
groceryList = ["Eggs","Cooking Oil","Rice","Potatoes"]
stockList = [250, 128, 40, 0, 19]

#Creating a list with multiple datatypes
randomList = [24, "Paris", False, 3.14]

#Creating a list with multiple dimensions
multiList = [[0,1], [1,2], [99,21]]

#Printing all the created lists
print(groceryList)
print(stockList)
print(randomList)
print(multiList)

#Accessing list items
print(groceryList[3]) #Using +ve indexing
print(stockList[-3]) #Using -ve Indexing

#Removing list items
randomList.remove(3.14)
print("Removal Completed. Updated List: ")
print(randomList)
groceryList.pop()
print("Potatoes purchased. Updated Shopping List: ")
print(groceryList)

#While loop to iterate through list items
Extras = ["Pickle","Mayonnaise","Cake","Biscuits","Ketchup"]
num = 0
print("Optional Items: ")
while(num<len(Extras)):
    print(Extras[num])
    num = num+1 #exit condition
    
#For Loop to iterate through list elements
print("Items in the multi dimensional list: ")
for i in multiList: #i is initialized to 0
    print(i)

#For loop with range() function 
for j in range(5,10):
    print(j+1) 

    