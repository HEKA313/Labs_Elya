import math

E = math.e
A = 2.1
B = 6.7
x = float(input())

if x < -2:
	y = x * x * x + 2 * A
elif -2 <= x <= 5:
	y = math.exp(abs(math.cos(B * x)))
else:
	y = x * x * math.pow(E, x)

print(y)
