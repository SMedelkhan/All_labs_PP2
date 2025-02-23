import re


with open('example.txt.txt') as file:
    txt = file.read()

x = re.findall("a.{3}b" , txt)

print(x)