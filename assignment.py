class Library:
	"""docstring for """
	def __init__(self, listOfBooks):
		self.availableBooks = listOfBooks
		
	def displayAvailableBooks(self):
		print("Avaialable Books: ")
		for book in self.availableBooks:
			print(book)

	def lendBook(self, requestedBook):
		if requestedBook in self.availableBooks:
			print("You have now borrowed book ", requestedBook)
			self.availableBooks.remove(requestedBook)

	def addBook(self, returnedBook):
		self.availableBooks.append(returnedBook)
		print("You have now returned book ", returnedBook)
		print("Thank you")

class Customer:
	
	def requestBook(self):
		print("Enter the book name you would like to borrow: ")
		self.book = input()
		return self.book

	def returnBook(self):
		print("Enter the name of book you would like to return: ")
		self.book = input()
		return self.book



library = Library(['Think & Grow Rich', 'Who Will Cry When You Will Die', 'For One More Day'])
customer = Customer()
while True:
	print("Enter 1 to display available books")
	print("Enter 2 to request for book")
	print("Enter 3 to return book")
	print("Enter 4 for exit")
	userChoice = int(input())
	if userChoice is 1:
		print("user choice is 1")
		library.displayAvailableBooks()
	elif userChoice == 2:
		print("user choice is 2")
		requestedBook = customer.requestBook()
		library.lendBook(requestedBook)
	elif userChoice == 3:
		print("user choice is 3")
		returnedBook = customer.returnBook()
		library.addBook(returnedBook)
	elif userChoice == 4:
		print("user choice is 4")
		quit()
	else:
		print("Invalid input")
		quit()

		