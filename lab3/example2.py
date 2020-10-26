num1 = int(input("Type first num: "))
num2 = int(input("Type second num: "))
num3 = int(input("Type third num: "))

if num1 < num2 and num1 < num3:
	print(num1)
elif num2 < num1 and num2 < num3:
	print(num2)
elif num3 < num1 and num3 < num2:
	print(num3)