size = int ( input())

list = []

for i in range(size):
    num = i+1
    list.append(num**2)

myit = iter(list)

for i in  range(size):
    print(next(myit))
