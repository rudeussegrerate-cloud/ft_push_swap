class GardenError(Exception):
    def __init__(self, message = "Error Garden"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message = "Plante Error")
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message = "Water Error"):
        super().__init__(message)

class Plant:
	def __init__(self, name:str, height:float, p_age:int)->None:
		if (height < 0 or self.is_aYear(p_age)):
			print("Erreur init OBJ")
			self._name = "None"
			self._height = 0.0
			self._p_age = 0
		else:
			self._name = str(name)
			self._height = float(height)
			self._p_age = p_age
		self._stat = Plant.stat()

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
			print("Error, height value is wrong")
		else:
			self._height = height
			print(f"Height update: {self._height}")

	def	set_age(self, age:int)->None:
		if (self.is_aYear(age)):
			print("Error, age value is wrong")
		else:
			self._p_age = age
			print(f"Age update: {self._p_age}")

	def	get_height(self)->float:
		return (self._height)

	def	get_age(self)->int:
		return (self._p_age)

	def stat_plant(self):
		print(f"show: {self._stat.get_show()}, grow: {self._stat.get_grow()}, age: {self._stat.get_age()}")
