n = int(input("type a num:"))
fact = 1
zeroCount = 0
for i in range(n):
	if(n>0):
		fact*=n
		n-=1
print(fact)
fact_ = fact
while fact_%10 == 0:
		zeroCount+=1
		fact_ //= 10
		print("up!" ,)	
print("number", fact, " has ", zeroCount, " trailing zeros.")		