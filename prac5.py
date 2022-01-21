str1 = input() #Takes input for the string
length = len(str1) #Stores length of entered string
str2="" #An empty string to store result

for i in range(length):
    if str1[i].islower()==True: #Condition to check if the entered letter is in upper case or lower
        str2+=str1[i].upper() #Converts into uppercase
    else:
        str2+=str1[i].lower() #Converts into lowercase

print(str2) #Prints the result