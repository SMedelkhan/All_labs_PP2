size = int ( input())

list = []

num = size
for i in range(size + 1):
    list.append(num)
    num-=1
    
myit = iter(list)

for i in  range(size):
    print(next(myit))
