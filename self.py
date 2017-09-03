class Employee:
	def employeeDetails(self):
		self.name = "Matthew"
		print("Name: ", self.name)
		age = 30
		print("Age: ", age)

	def printEmployeeDetails(self):
		print("printing in second method")
		print("Name: ", self.name)
		#print("Age: ", age)

employee = Employee()
employee.employeeDetails()

employee.printEmployeeDetails()
		