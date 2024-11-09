# Today we will discuss Lists and see some examples in list

## What is List in Python

- A list is a built-in data structure that is used to store an ordered collection of items.
- List are Mutable means their contents can be changed after the list has been created
- List is mainly used data type in devops world

## Why Lists are Useful

- Lists are useful for grouping data together so it can be accessed and manipulated as a single unit.
- They are one of the most versatile and commonly used data structures in Python, allowing you to work with collections of data efficiently

## Common List Operations

- Accessing Items
- Adding Deleting or Updating Items
- Slicing ( means gets a some portion of list from start index to end index )

## List Declaration

`my_list1` = [3, 9, 4, 5, 10, 6]. # contains collection of numeric items

`my_list2` = ["a", "b" , "c"] # string items

#### Accessing Items in a List

- To Access a list we use [] brackets along with list name like this (mylist1[0])
- Point to remember list always starts from zeroth index

` my_list[0]` # 3 accessing zeroth item

`my_list[3]` # 5 item that is present in 3rd index

`my_list[-1]` # last item

#### Slicing

- Getting specific portion with in the list
- my_list[start:stop:step]
- start is an start index, default is 0
- end is an end index, default is length of the list
- step is the interval between elements in the list, default value is 1  
   Example:-

  ##### start Index

* `my_list[1:3] ` # [9, 4, 5] - it will print start index 1 to end index 3
* `my_list[3:]` # [5, 10, 6] - start is 3 end is length of list step 1
* `my_list[-3:]` # [5, 10, 6] - start is -3 end is length of list step 1

##### end Index

- `my_list[:3]` # [3, 9, 4] - beacause start is 1 end is 3 step 1
- `my_list[:-4]` # [9, 5] - start is 0 end -4 step 1

##### Using step

- ```my_list[0:5:2]``` # [3, 4, 10] start is 0 end is index 5 step is 2
- `my_list[::3]` # Output: [10, 40, 70] - getting every 3rd element start index 1 end length of list step 3

##### To print a list in reverse order

- `my_list[::-1]` # Output: [80, 70, 60, 50, 40, 30, 20, 10]

#### Built in Functions in Python
append() used to add item to the list
count(ele) used to count the number of time the ele is occoured
remove(ele) used to remove the ele in the list

pop() == used to remove at end index
sort() == used to sort in asc or desc order
extend(list2) to add list2 to list1 