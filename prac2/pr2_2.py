#20CE021
#https://github.com/JiyaDesai1011/PIP_PRAC_SUBMISSION

#a. Write a Python program to create a tuple with different data types.
tup1 = (1,"two",3.00,False) #Created a tuple containing elements of different datatypes
print(tup1) #Printed the result



#b. Write a Python program to create a tuple with numbers and print one item.
tup2 = () #Created an empty tuple
n = int(input("Enter the number of elements you wanna add : ")) #Took input for number of elements to be added
for i in range(n): #Took a loop which runs as many times as the number of elements to be added
    x = int(input("Enter number : ")) #Took input for the element
    tup2 += (x,) #Added new element in tuple
ind = int(input("Enter the index you wanna access : ")) #Took input for the index of the element to be printed
if len(tup2)<ind : #Checked if the index exists in the tuple
    print("Enter valid input") #Printed the result
else:
    print(tup2[ind]) #Printed the result



#c. Write a Python program to add an item in a tuple.
tup3 = () #Created an empty tuple
n = int(input("Enter the number of elements you wanna add : ")) #Took input for number of elements to be added
for i in range(n):#Took a loop which runs as many times as the number of elements to be added
    x = input("Enter number : ") #Took input for the element
    tup3 += (x,) #Added new element in tuple
print(tup3) #Printed the result



#d. Write a Python program to convert a tuple to a string.
tup4 = ("a","p","p","l","e",5) #Created a tuple
ans = "" #Took an empty string to store the answer
for i in range(len(tup4)): #Took a loop which runs as many times as the length of the tuple
    ans = ans + str(tup4[i]) #Concatinated the ith element (string type) with the previous answer
print(ans) #Printed the result



#e. Write a Python program to find the length of a tuple.
tup5 = ("a","p","l","e",5) #Created a tuple
print("Length of tuple : "+str(len(tup5))) #Printed the length of tuple