import math

PI = math.pi

a = float(input())

z1 = math.pow(math.cos((3 / 8) * PI - a / 4), 2) - math.pow(math.cos(11 * PI / 8 + a / 4), 2)
z2 = (math.sqrt(2) / 2 * math.sin(a / 2))

print(z1)
print(z2)
