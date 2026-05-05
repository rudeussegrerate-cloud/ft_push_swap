class GardenError(Exception):
	def __init__(self, message = "Erreur, Plante inconnue :("):
		super().__init__(message)


class PlantError(GardenError):
	pass


class WaterError(GardenError):
	pass


def raiseError(Errorexcept: GardenError, message)->None:
	if (message):
		raise Errorexcept(message)
	else:
		raise Errorexcept()


class Plant:
	def __init__(self, name:str, height:float, p_age:int)->None:
		if (not name or not height or not p_age):
			raiseError(GardenError, '')
		if (height < 0 or not self.is_aYear(p_age)):
			raiseError(PlantError, "Entrer une valeur correrct de la taille ou de l'age")
			self._name = "None"
			self._height = 0.0
			self._p_age = 0
		else:
			self._name = str(name)
			self._height = round(float(height), 1)
			self._p_age = p_age
		self._stat = Plant.stat()
		self._waterqty = 0

	def get_waterqty(self):
		return self._waterqty

	def set_waterqty(self, value):
		if (value < 25):
			raiseError(WaterError, "La plante manque d'eau et risque de fanner")
		self._waterqty = value

	class stat:
		def __init__(self):
			self._grow = 0
			self._age = 0
			self._show = 0

		def set_grow(self, grow:int)->None:
			self._grow = self._grow + grow

		def set_age(self, age:int)->None:
			self._age = self._age + age

		def set_show(self, show:int)->None:
			self._show = self._show + show

		def get_grow(self)->None:
			return (self._grow)

		def get_age(self)->None:
			return (self._age)

		def get_show(self)->None:
			return (self._show)


	@classmethod
	def anonymous(cls)->"Plant":
		return cls("None", 0.0, 0)

	@staticmethod
	def is_aYear(age:int)->bool:
		return (age > 364)
	
	def grow(self)->None:
		self._height = round(self._height + 0.8, 1)
		self._stat.set_grow(1)

	def	age(self)->None:
		self._p_age = self._p_age + 1
		self._stat.set_age(1)

	def	show(self)->None:
		print(f"{self._name}: {self._height}cm, {self._p_age} days old")
		self._stat.set_show(1)

	def	set_height(self, height:float)->None:
		if (height < 0):
			raiseError(PlantError, "Error, height value is wrong")
		else:
			self._height = height

	def	set_age(self, age:int)->None:
		if (self.is_aYear(age)):
			raiseError(PlantError, "Error, age value is wrong")
		else:
			self._p_age = age

	def	get_height(self)->float:
		return (self._height)

	def	get_age(self)->int:
		return (self._p_age)

	def stat_plant(self):
		print(f"show: {self._stat.get_show()}, grow: {self._stat.get_grow()}, age: {self._stat.get_age()}")

def test_operation(operation_number: int) -> None:
	if (operation_number == 0):
		plante = Plant("asf", 364, -2)
	elif (operation_number == 1):
		plante = Plant('Rose', 10, 366)
		plante.set_waterqty(operation_number)
	

if __name__ == "__main__":
	print("=== Custom Garden Errors Demo ===\n")
	i = 0
	a = ''
	except_list = (PlantError, WaterError, GardenError, GardenError)
	while i < 4:
		try:
			if (i < 3):
				print(f"Testing {except_list[i].__name__}...")
				a = '\n'
			if i > 1:
				a = ''
			test_operation(i%2)
		except except_list[i] as e:
			print(f"Caught {except_list[i].__name__}: {e}!{a}")
		i += 1
	print("\nAll custom error types work correctly!")