size = int ( input())

list = []

for i in range(size):
    num = i+1

    if num % 3 == 0 or num % 4 == 0:
        list.append(num)



myit = iter(list)

for i in range(len(list)):
    print(next(myit))