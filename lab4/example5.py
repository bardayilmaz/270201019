n = int(input("type a num:"))
fact = 1
for i in range(n):
	if(n>0):
		fact*=n
		n-=1
print(fact)			