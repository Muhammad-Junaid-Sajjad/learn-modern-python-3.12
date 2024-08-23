
# using type-hinting " :str "
message = "Hello, Python World ! "
print (message)

#string (str)
#integer (int)
#float (float)
# boolean (bool)


fruit: list = ['apple','mango', 'cherry','date']
print (fruit)
# print(fruit[2])  # indexing examples 

# # slicing examples 
print (fruit[2:4])  # we can also use negative postive all indexing types  

# negative indexing example
print(fruit[-4:])               

#listing types
fruit.clear()
print(fruit)

# finding memory address of fruit 
print(id(fruit))
fruit.reverse()
print(fruit)

