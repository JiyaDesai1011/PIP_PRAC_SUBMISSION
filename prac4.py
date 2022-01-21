n = int(input()) #Takes input for number of elements to be entered

mylist = list(map(int, input().split(" "))) #Takes input for the elements

mylist.sort() #Sorts the list of elements entered

myset = list(set(mylist)) #Converts to a set to avoid repeated elements

print(myset[-2]) #Prints the second last element of sorted and unrepeated list