# List Declaration

# In my_list contains collection numeric items
my_list = [3, 9, 4, 5, 10, 6]

# Contains collection string items
mystring_list = ["a", "b" , "c"] 

# Contains collection mixed items
mixed_list = ["a", 6 , "c", True, 4, False]  

# start Index
# print(my_list[-3:]) 
# print("dwwe", my_list[-3:-1]) # the end index should be negative value if you use negative value in start index

# # End Index
# print(my_list[:-4]) 
# print(my_list[:1])

# print("ssdsdd",my_list[::3])  # Output: [10, 40, 70]

# print(my_list[::-1])  # Output: [80, 70, 60, 50, 40, 30, 20, 10]

# #########
# # Using step 
# print(my_list[0:5:2])
# print(my_list[-5:-2: 2])


# Functions
my_list.append(6)
# print(my_list.count(6))
my_list.insert(3,55)
my_list[3]=33 # update 3rd index is 33

my_list.remove(9)
my_list.pop()
my_list.sort()
# del my_list[2]
# print(my_list[:1])  

x = my_list.count(3)
# if(334 in my_list):
#     print("3334 is present in my list")
# else:
#     print("334 is not present in my list")

my_list2 = [5,6, 0, 44,88]

my_list2.extend(my_list)
my_list2.sort()
# print(my_list2)

#  List Comprehension
my_list3 = [2, 5, 9, 10, 22, 33]



new_list = [ x for x in my_list3 if 2 in my_list3]
print(new_list)