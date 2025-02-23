import re

with open('example.txt.txt') as file:  
    txt = file.read()


splitting = re.split(r'(?=[A-Z])', txt)

print(splitting)