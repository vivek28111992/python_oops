class Car:
	numberOfWheels = 4
	_color = "Black"
	__yearOfManufacture = 2017

class Bmw(Car):
	def __init__(self):
		print("Protected attribute color: ", self._color)

car = Car()
print("Public attribute numberOfWheels: ", car.numberOfWheels)
bmw = Bmw()
print("Public attribute yearOfManufacture: ", car._Car__yearOfManufacture)