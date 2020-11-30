password = input("choose a password: ")
isValid = False
lowVal = False
upVal=False
digVal=False
requirementCount = 0
if len(password) >= 8: requirementCount += 1
for i in password:
	if i.islower() and not lowVal:
		requirementCount +=1
		lowVal = True
	elif i.isupper() and not upVal:
		requirementCount +=1
		upVal = True
	elif i.isdigit() and not digVal:
		requirementCount +=1
		digVal = True
if digVal and lowVal and upVal and requirementCount == 4:
	print("valid password!")
else:
	print("invalid password!")			