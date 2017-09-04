from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
	@abstractmethod
	def createNewAccount():
		return 0
	@abstractmethod
	def authenticate():
		return 0
	@abstractmethod
	def withdraw():
		return 0
	@abstractmethod
	def deposit():
		return 0
	@abstractmethod
	def displayBalance():
		return 0

class Bank(Account):

	def __init__(self):
		self.savingAccounts = {}

	def createNewAccount(self, name, initialDeposit):
		self.accountNumber = randint(10000, 99999)
		self.savingAccounts[self.accountNumber] = [name, initialDeposit]
		print("Your account creation has been successful. Your account number is ", self.accountNumber)

	def authenticate(self, name, accountNumber):
		if accountNumber in self.savingAccounts.keys():
			if self.savingAccounts[accountNumber][0] == name:
				print("Authentication Successfull")
				self.accountNumber = accountNumber
				return True
			else:
				print("Authentication Failed")
				return False
		else:
			print("Authentication Failed")
			return False
	def withdraw(self, withdrawAmount):
		if self.savingAccounts[self.accountNumber][1] < withdrawAmount:
			print("Insufficient Balance")
		else:
			self.savingAccounts[self.accountNumber][1] -= withdrawAmount
			print("Withdraw was successful. Available balance is: ")
			self.displayBalance()

	def deposit(self, depositAmount):
		self.savingAccounts[self.accountNumber][1] += depositAmount
		print("Deposit was successful. Available balance is: ")
		self.displayBalance()


	def displayBalance(self):
		print("Balance Amount is: ", self.savingAccounts[self.accountNumber][1])

bank = Bank()

while True:
	print("Press 1 to create new account: ")
	print("Press 2 to access existing account: ")
	print("Press 3 to exit")

	userChoice = int(input())

	if userChoice is 1:
		print("Please enter name: ")
		name = input()
		print("Please enter initial deposit")
		initialDeposit = int(input())
		bank.createNewAccount(name, initialDeposit)
	elif userChoice is 2:
		print("Please enter name: ")
		name = input()
		print("Please enter account number")
		accountNumber = int(input())
		authenticationStatus = bank.authenticate(name, accountNumber)
		if authenticationStatus is True:
			while True:
				print("Press 1 to deposit: ")
				print("Press 2 to withdraw: ")
				print("Press 3 to check balance: ")
				print("Press 4 to exit: ")
				userChoice = int(input())
				if userChoice is 1:
					print("Please enter amount to deposit: ")
					depositAmount = int(input())
					bank.deposit(depositAmount)
				elif userChoice is 2:
					print("Please enter amount to withdraw: ")
					withdrawAmount = int(input())
					bank.withdraw(withdrawAmount)
				elif userChoice is 3:
					print("Your account balance is: ")
					bank.displayBalance()
				else:
					break
	else:
		quit()