import math

n = int(input('Input number of sides:'))

x = int(input('Input the length of a side: '))

def Area( n , x ):
    perimeter = n * x

    alpha = 180 * (n-2) / n

    radians = math.radians(alpha / 2)

    apothema = math.tan(radians) * x / 2

    return 1 / 2 * perimeter * apothema

print(Area( n , x))