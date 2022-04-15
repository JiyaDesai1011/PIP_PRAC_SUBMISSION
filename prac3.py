#variable for input 
n = int(input())

#List to store the input
arr = map(int, input().split())

# Typecasted arr to set to remove repeated the entries, then again to list then sorted the list and printed last second element of the list
print(sorted(list(set(arr)))[-2])