thisset = {"apple", "banana", "cherry"}
print(thisset)

#Unordered means that the items in a set do not have a defined order
#Set items are unchangeable
#Duplicates Not Allowed


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


#True and 1 is considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


#False and 0 is considered the same value
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


#A set can contain different data types
set1 = {"abc", 34, True, 40, "male"}


#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))


#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
