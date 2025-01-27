#Remove Item
thisset = {"apple", "banana", "cherry","banana"}

thisset.remove("banana")

print(thisset)


#Using the discard() method
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)



thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

print(x) #removed item
print(thisset) #the set after removal


#The clear() method empties the set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)



