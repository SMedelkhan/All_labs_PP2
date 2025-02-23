import re


with open('example.txt.txt') as file:
    txt = file.read()

pattern = re.compile(r'a.*b')

matches = pattern.finditer(txt)

for match in matches:
    print(match.group(0))  
