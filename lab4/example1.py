num = input("type a number: ")
if len(num) >= 2:
	digit1 = int(num[len(num)-1])
	digit2 = int(num[len(num)-2])
	print(digit1+digit2)
elif len(num) == 1:
	digit = int(num)
	print(digit)
#######################
num2 = input("type a num:")	
if len(num) >=2:
	digitt1 = int(num2)%100//10
	digitt2 = int(num2)%10
	print(digitt1+digitt2)
elif len(num) == 1:
	print(num)	