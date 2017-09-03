class A:
	def method(self):
		print("This method belongs to class A")
	pass

class B:
	def method(self):
		print("This method belongs to class B")
	pass

class C:
	def method(self):
		print("This method belongs to class C")
	pass

class D(B, C):
	pass

d = D()
d.method()
