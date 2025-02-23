import re


with open('example.txt.txt') as file:
    txt = file.read()

x = re.findall("[a-b]" , txt)

print(x)