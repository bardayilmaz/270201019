GPA = float(input("Type your GPA: "))
lecNum = int(input("Type your lecture number: "))

if lecNum < 47:
	if GPA < 2.0:
		print("Not enough number of lectures and GPA!")
	else:
		print("Not enough number of lectures!")
else:
	if GPA < 2.0:
		print("Not enough GPA!")
	else:
		print("GRADUATED!")		