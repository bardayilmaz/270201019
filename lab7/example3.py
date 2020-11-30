employees = dict()
name = ""
salary = 0
for i in range(3):
	name = input("Type name: ")
	salary = int(input("type salary: "))
	employees.update({name:salary})

print(sorted(employees.items(), key=lambda item: item[1], reverse=True))	
