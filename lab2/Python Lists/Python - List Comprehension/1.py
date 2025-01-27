#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) #only the fruits with the letter "a" in the name


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # Same as previous code


#The Syntax
newlist1 = [x.upper() for x in fruits] #Set the values in the new list to upper case
print(newlist1)

newlist2 = ['hello' for x in fruits] #Set all values in the new list to 'hello'
print(newlist2)

newlist3 = [x if x != "banana" else "orange" for x in fruits]
print(newlist3) #Return orange instead of banana