#20CE021
#https://github.com/JiyaDesai1011/PIP_PRAC_SUBMISSION



#a. Write a Python script to check whether a given key already exists in a dictionary.
dictionary = {
    "name" : "Chalsie",
    "age" : 19,
    "gender" : "female",
    "contact" : 7848378747
} #Created a dictionary

arr = list(dictionary.keys()) #Added all the keys in a list

key=input("Enter the key you are looking for: ") #Took input for the key

if key in arr: #Printed the result
    print("The key already exists in dictionary.") 
else:
    print("The key doesn't exist in dictionary.")



#b. Write a Python script to merge two Python dictionaries.
dic1 = {
    "name" : "Chalsie",
    "age" : 19,
} #Created 1st dictionary

dic2 = {
    "gender" : "female",
    "contact" : 7848378747
} #Created 2nd dictionary

dic1.update(dic2) #Updated 1st dictionary by adding the 2nd one in it

print(dic1) #Printed the result



#c. Write a Python program to sum all the items in a dictionary.
mydic = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5
} #Created a dictionary

l1 = list(mydic.values()) #Added all the values of dictionary in a list
n = len(mydic) #Calculated length of dictionary
ans = 0 #Took a varible to store the answer and initialized it with a 0
for i in range(n): #Took a loop that runs as many times as the length of dictionary
    ans = ans + l1[i] #Updation in answer for n times
print(ans) #Printed the result



#d. Write a Python script to add a key to a dictionary.

mydict = {
    0: 10, 
    1: 20
} #Created a dictionary

dictkey = int(input("Enter key: ")) #Took input for key
dictval = int(input("Enter value: ")) #Took input for value

mydict[dictkey] = dictval #Added the element to the dictionary using the key and value input

print(mydict) #Printed the result



#e. Write a Python script to concatenate following dictionaries to create a new one.

mydic1 = {
    1:10, 
    2:20
} #Created a dictionary

mydic2 = {
    3:30, 
    4:40
} #Created a dictionary

mydic3 = {
    5:50,
    6:60
} #Created a dictionary

mydic4 = mydic1|mydic2|mydic3 #Performed dictionary concatination

print(mydic4) #Printed the result