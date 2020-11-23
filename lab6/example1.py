email = input("enter an email adress: ")
email = email.lower()
x = email.index("@")
for i in range(x):
	if(email[i] == "."):
		email = email[:i] + email[i+1:]
if email == "ceng113@example.com":
	print("true")