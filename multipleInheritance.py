class OperatingSystem:
	multitasking = True
	name = "Mac OS"

class Apple:
	website = "www.apple.com"
	name = "Apple"

class MacBook(Apple, OperatingSystem):
	def __init__(self):
		if self.multitasking is True:
			print("This is multi tasking system. Visit {} for more details".format(self.website))
			print("Name: ", self.name)

macBook = MacBook()

		
		