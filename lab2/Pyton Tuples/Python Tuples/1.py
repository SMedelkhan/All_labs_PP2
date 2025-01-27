#Create a Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuple items are ordered
#Allow duplicate values
#Order will not change
#add or remove items after the tuple has been created are imposible


#Length of Tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#A tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")


#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)