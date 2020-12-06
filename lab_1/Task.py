import math

E = math.e

a = 6.32
b = 3.704
x = 7.15

y = (a * x) / math.sqrt(math.pow(b, 2) + 2 * math.pow(E, x) - b * x)

print(y)
