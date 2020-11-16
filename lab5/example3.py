num1 = int(input("type a positive num:"))
num2 = int(input("type a positive num:"))
common = 0

while num1>0 and num2>0:
	if num1%10 == num2%10:
		common+=1

	num1 = num1 // 10
	num2 = num2 // 10	

print(common)						