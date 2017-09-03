class Employee:
	def setNumberOfWorkingHours(self):
		self.numberOfWorkingHours = 40

	def displayNumberOfWorkingHours(self):
		print(self.numberOfWorkingHours)

class Trainee(Employee):
	def setNumberOfWorkingHours(self):
		self.numberOfWorkingHours = 45

	def resetNumberOfWorkingHours(self):
		super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
employee.displayNumberOfWorkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
trainee.displayNumberOfWorkingHours()

trainee.resetNumberOfWorkingHours()
trainee.displayNumberOfWorkingHours()