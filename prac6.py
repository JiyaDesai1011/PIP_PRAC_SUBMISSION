n = int(input()) #Takes input for number of inputs to be entered
mylist = [] #An empty list to store the inputs
cnt = 0 #A variable to store the counts

for i in range(n):
    str1 = input() #Takes an input for the string
    mylist.append(str1) #Stores the input string in a list

myset = list(set(mylist)) #Converts into set to avoid the repeated elements
print(myset)
print(len(myset)) #Prints the number of unique elements using the length of set

for j in range(len(myset)):
    cnt = mylist.count(myset[j]) #Counts the number of accourance of each element of the set 
    print(cnt, end = " ") #Prints the counts of each elements of the set