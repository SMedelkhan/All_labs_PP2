import re


with open('example.txt.txt' ) as file:
    txt = file.read()

pattern = re.compile(r'[a-z]+_[0-9]+')

matches = pattern.finditer(txt)

for match in matches:
    print(match)