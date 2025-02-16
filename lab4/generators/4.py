start = int(input())

end = int(input())

list = []

num = start

for i in range(end - start + 1):
    
    list.append(num**2)

    num+=1

myit = iter(list)

for i in range(len(list)):
    print(next(myit))