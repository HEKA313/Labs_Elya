# .Составить программу, которая по номеру семестра печатает курс, к которому
# относится введенный семестр (1 и 2 семестр - 1 курс, 3 и 4 семестр - 2 курс и т.
# д.).

a = int(input())
if a == 1 or a == 2:
	b = 1
elif a == 3 or a == 4:
	b = 2
elif a == 5 or a == 6:
	b = 3
elif a == 7 or a == 8:
	b = 4

print(b)
