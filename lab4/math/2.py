def area_of_trapezoi(h , a , b):
    return (a + b) / 2 * h


h = int (input("Height:"))

x = int (input("Base, first value:"))

y = int (input("Base, secnod value:"))
Area = area_of_trapezoi(h , x , y)


print(f"Area : {Area}")
