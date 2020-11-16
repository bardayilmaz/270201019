password = "abc123xd"
passwInput = input("password: ")
while True:
	if passwInput == "help":
		print(password[0])
		passwInput = input("password: ")

	elif passwInput == password:
		print("welcome")
		break
	else: 
		print("wrong")
		passwInput = input("password: ")		