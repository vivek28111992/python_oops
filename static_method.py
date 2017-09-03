class Employee():
	def employeeDetails(self):
		self.name = "Ben"

	@staticmethod	
	def welcomeMessage():
		print("Welcome to our organisation")

employee = Employee()
employee.employeeDetails()

print(employee.name)
print(employee.welcomeMessage())
		