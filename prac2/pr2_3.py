#20CE021
#https://github.com/JiyaDesai1011/PIP_PRAC_SUBMISSION



#a. Write a Python program to add member(s) in a set and clear a set.
set1 = {1,2,3,4,5} #Created a set

inp = int(input("Enter 1 to add elements and enter 2 to clear the set: \n")) #Took input for choosing which operation to perform

if inp==1: #For adding element
    n = int(input("How many elements you want to add?\n")) #Took input for the number of elements to be added
    for i in range(n): #Took a loop which runs as many times as the number of elements that are to be added
        x = int(input("Enter the element :")) #Took input for the element to be added
        if x in set1: #Checked if the element already exists in the set or not
            continue 
        else: 
            set1.add(x) #Added the element to the set only if it doesn't already exists in the set
    print(set1) #Printed the resultant set
else: #For clearing the set
    set1.clear() #Cleared the set
    print(set1) #Printed the resultant set



#b. Write a Python program to remove an item from a set if it is present in the set.
set2 = {1,2,3,4,5,6,7,8,9,10} #Created a set

ele = int(input("Enter the element you wanna remove : ")) #Took input for the element to be removed
if ele in set2: #Checked if the element already exists in the set or not
    set2.remove(ele) #removed the element from the set only if it already exists in the set
    print(str(ele)+" removed.") #Printed the result
else:
    print("No such element exists in the set.") #Printed the result
print(set2) #Printed the resultant set



#c. Write a Python program to create an intersection, Union, difference of sets.
set3 = {1,2,3,4,5,6,7} #Created a set
set4 = {4,5,6,7,8,9,10} #Created a set

print("Union of sets : ")
print(set3.union(set4)) #Printed the result of union
print("Intersection of sets : ")
print(set3.intersection(set4)) #Printed the result of intersection
print("Difference of sets (set3 - set4) : ")
print(set3.difference(set4)) #Printed the result of set3 - set4
print("Difference of sets (set4 - set3) : ")
print(set4.difference(set3)) #Printed the result of set4 - set3



#d. Write a Python program to find maximum and the minimum value in a set.
set5 = {5,8,20,92,85,21,19,83} #Created a set
mylist = list(set5) #Converted into a list
mylist.sort() #Sorted the list
print("Max element: ")
print(mylist[-1]) #Printed the last element of the sorted list as max element
print("Min element: ")
print(mylist[0]) #Printed the 1st element of the sorted list as min element



#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#1 For lists:
list1 = [1,2,1,2,1,3,5,8] #Created a list
list2 = list(set(list1)) #Converted into a set to avoid repeated elements

countMax = 0 #Took a variable to get the max count and initialized it with a 0
maxList = [] #Created an empty list to store the elements with max count

for i in range(len(list2)): #Took a loop which runs as many times as the length of set
    if list1.count(list2[i])>countMax: #Checked if the count of an element from the 1st list is greater than the max count or not to find out the max count
        countMax = list1.count(list2[i]) #Updated the max count

for i in range(len(list2)): #Took a loop which runs as many times as the length of set
    if list1.count(list2[i])==countMax: #Checked if the count of an element from the 1st list is equal to max count or not
        maxList.append(list2[i]) #Added the elements in a new list which are having counts equal to max count

for i in range(len(maxList)): 
    print(maxList[i]) #Printed the result using a loop


#2 For tuples:
tup1 = (1,2,1,2,1,3,5,8) #Created a tuple
list1 = list(tup1) #Converted the tuple into a list
list2 = list(set(list1)) #Converted into a set to avoid repeated elements

countMax = 0 #Took a variable to get the max count and initialized it with a 0
maxList = [] #Created an empty list to store the elements with max count

for i in range(len(list2)): #Took a loop which runs as many times as the length of set
    if list1.count(list2[i])>countMax: #Checked if the count of an element from the 1st list is greater than the max count or not to find out the max count
        countMax = list1.count(list2[i]) #Updated the max count

for i in range(len(list2)): #Took a loop which runs as many times as the length of set
    if list1.count(list2[i])==countMax: #Checked if the count of an element from the 1st list is equal to max count or not
        maxList.append(list2[i]) #Added the elements in a new list which are having counts equal to max count

for i in range(len(maxList)): 
    print(maxList[i]) #Printed the result using a loop

#3 For dictionaries:
dict1 = {
    1 : 1,
    2 : 2,
    3 : 1,
    4 : 2,
    5 : 1,
    6 : 3,
    7 : 5,
    8 : 8
} #Created a dictionary
list1 = list(dict1.values()) #Stored all the values of the dictionary into a list
list2 = list(set(list1)) #Converted into a set to avoid repeated elements

countMax = 0 #Took a variable to get the max count and initialized it with a 0
maxList = [] #Created an empty list to store the elements with max count

for i in range(len(list2)): #Took a loop which runs as many times as the length of set
    if list1.count(list2[i])>countMax: #Checked if the count of an element from the 1st list is greater than the max count or not to find out the max count
        countMax = list1.count(list2[i]) #Updated the max count

for i in range(len(list2)): #Took a loop which runs as many times as the length of set
    if list1.count(list2[i])==countMax: #Checked if the count of an element from the 1st list is equal to max count or not
        maxList.append(list2[i]) #Added the elements in a new list which are having counts equal to max count

for i in range(len(maxList)): 
    print(maxList[i]) #Printed the result using a loop