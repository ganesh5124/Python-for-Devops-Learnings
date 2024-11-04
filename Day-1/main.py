# List Declaration

# In my_list contains collection numeric items
my_list = [3, 9, 4, 5, 10, 6]

# Contains collection string items
mystring_list = ["a", "b" , "c"] 

# Contains collection mixed items
mixed_list = ["a", 6 , "c", True, 4, False]  

# start Index
print(my_list[-3:]) 
print("dwwe", my_list[-3:-1]) # the end index should be negative value if you use negative value in start index

# End Index
print(my_list[:-4]) 
print(my_list[:1])

print("ssdsdd",my_list[::3])  # Output: [10, 40, 70]

print(my_list[::-1])  # Output: [80, 70, 60, 50, 40, 30, 20, 10]

#########
# Using step 
print(my_list[0:5:2])
print(my_list[-5:-2: 2])


# Functions
my_list.append(6)
print(my_list.count(6))

print(my_list)