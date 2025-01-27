#Sort List Alphanumerically


#Sort the list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


#Sort Descending

#Sort the list descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#For nums
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Customize Sort Function

#sort nums to clother to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#Case Insensitive Sort

# resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#use str.lower as a key function
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse function, regardless alphabet
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)





