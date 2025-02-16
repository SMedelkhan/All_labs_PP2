import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface status")
print("=" * 102)
print("DN", " " * 42, "Description "," "*15 , "speed", " " * 15, "MTU")
print("-" * 42, "-" * 28, "-" * 13, "\t", "-" * 12)


for imdata in data["imdata"]:

    for i in imdata:

        for j in imdata[i]: # every imdata[i] is dictionary

            print(imdata[i][j]["dn"],"\t", "\t\t\t"  , imdata[i][j]["speed"] ,"\t\t" , imdata[i][j]["mtu"])
