class MusicalInstruments:
	numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
	typeOfWood = "ToneWood"

class Guitar(StringInstruments):
	def __init__(self):
		self.numberOfStrings = 6
		print("This guitar consits of {} strings. It is made up of {} & it can play {} keys".format(self.numberOfStrings, self.typeOfWood, self.numberOfMajorKeys))

guitar = Guitar()	