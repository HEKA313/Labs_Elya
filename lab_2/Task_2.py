# Сумма младшего разряда целой и старшего разряда дробной частей x
# является четным числом или 1-й разряд целой части больше 1-го
# разряда дробной части.

a = float(input())
b = a % 10
c = (a * 10) % 10
isSpecial = False

if (a + b) % 2 == 0:
	isSpecial = True
elif b > c:
	isSpecial = True

print(isSpecial)
