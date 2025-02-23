import re


with open('example.txt.txt' ) as file:
    txt = file.read()

pattern = re.compile(r'[A-Z][a-z]+')

matches = pattern.finditer(txt)

for match in matches:
    print(match)