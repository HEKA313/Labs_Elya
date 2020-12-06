import math

E = math.e

z = float(input())
y = float(input())
x = float(input())

f = x + math.sqrt(abs(x) + math.pow(E, y)) - (math.pow(z, 3) * math.pow(math.sin(y), 2)) / (y + z * z * (y - x))

print(f)

