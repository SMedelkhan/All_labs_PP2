import re


with open('example.txt.txt' ) as file:
    txt = file.read()

x=re.sub("[\s,.]" , ":" , txt)

print(x)