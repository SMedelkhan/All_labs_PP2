#Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


#There is also a method called get() that will give you the same result
x = thisdict.get("model")
print(x)


#Get Keys
x = thisdict.keys()
print(x)


#Get Values
x = thisdict.values()
print(x)


#Get Items
x = thisdict.items()
print(x)
