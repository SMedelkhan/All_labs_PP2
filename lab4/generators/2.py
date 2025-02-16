size = int ( input())

list = []

for i in range(size):
    num = i+1

    if num % 2 == 0:
        list.append(num)

myit = iter(list)

string = '0'

for i in  range(len(list)):
    string = string + ',' + str(next(myit)) 


print(string)