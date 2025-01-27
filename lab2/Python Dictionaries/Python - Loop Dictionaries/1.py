#Loop Through a Dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)


#Print all values
for x in thisdict:
  print(thisdict[x])


#You can also use the values() method
for x in thisdict.values():
  print(x)

#You can use the keys() method
for x in thisdict.keys():
  print(x)


#Loop through both keys and values
for x, y in thisdict.items():
  print(x, y)

