mylist = ["apple", "banana", "cherry", "banana"]

print(mylist)

# Indexes starts with 0
# Orders cannot change
# We can change, add, and remove items in a list after it has been created
# Dublicates are allowed


# List length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


#List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


#A list can contain different data types
list4 = ["abc", 34, True, 40, "male"]


# lists are defined as objects with the data type 'list'
print(type(list1))


#It is also possible to use the list() constructor when creating a new list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


