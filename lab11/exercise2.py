class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def get_name(self):
		return self.name
	def set_name(self, name):
		self.name = name

	def get_salary(self):
		return self.salary
	def set_salary(self, salary):
		self.salary = salary	

	def display_information(self):
		print(f"Employee {self.name}'s salary: {self.salary}")

class Company:
	def __init__(self, employee_list):
		self.employee_list = employee_list

	def get_employee_list(self):
		return self.employee_list
	def set_employee_list(self, employee_list):
		self.employee_list = employee_list		

	def add_employee(self, new_employee):
		if isinstance(new_employee, Employee):
			self.employee_list.append(new_employee)
		else:
			print("What are you trying to add?")	

	def average_salary(self):
		sum = 0
		for i in self.employee_list:
			sum += i.salary
		return sum/len(self.employee_list)

	def display_all(self):
		for i in self.employee_list:
			print(i.name,"|", i.salary)		

emp1 = Employee("Bülent Yılmaz", 1)
emp2 = Employee("Arda Yılmaz" , 2)
emp3 = Employee("Bülent Arda Yılmaz", 3)

comp = Company(list())
comp.add_employee(emp1)
comp.add_employee(emp2)
comp.add_employee(emp3)
print(comp.average_salary())
comp.display_all()

