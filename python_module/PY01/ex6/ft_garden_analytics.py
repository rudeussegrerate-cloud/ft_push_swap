class Plant:
	def __init__(self, name:str, height:float, p_age:int)->None:
		if (height < 0 or self.is_aYear(p_age)):
			print("Erreur init OBJ")
			self._name = "None"
			self._height = 0.0
			self._p_age = 0
			self.statistic = self.stat()
		else:
			self._name = str(name)
			self._height = float(height)
			self._p_age = p_age
			self.statistic = self.stat()

	class stat:
		def __init__(self):
			self._grow = 0
			self._age = 0
			self._show = 0

			def set_grow(self, grow:int)->None:
				self.grow = self.grow + grow

			def set_age(self, age:int)->None:
				self.age = self.age + age

			def set_show(self, show:int)->None:
				self.show = self.show + show

	#getter
			def get_grow(self)->None:
				return (self.grow)

			def get_age(self)->None:
				return (self.age)

			def get_show(self)->None:
				return (self.show)


	@classmethod
	def anonymous(cls)->"Plant":
		return cls("None", 0.0, 0)

	@staticmethod
	def is_aYear(age:int)->bool:
		return (age > 364)
	
	def grow(self)->None:
		self._height = round(self._height + 0.8, 1)
		self.statistic.set_grow(1)

	def	age(self)->None:
		self._p_age = self._p_age + 1
		self.statistic.set_age(1)

	def	show(self)->None:
		print(f"{self._name}: {self._height}cm, {self._p_age} days old")
		self.statistic.set_show(1)

	def	set_height(self, height:float)->None:
		if (height < 0):
			print("Error, height value is wrong")
		else:
			self._height = height
			print(f"Height update: {self._height}")

	def	set_age(self, age:int)->None:
		if (is_aYear(age)):
			print("Error, age value is wrong")
		else:
			self._p_age = age
			print(f"Age update: {self._p_age}")

	def	get_height(self)->float:
		return (self._height)

	def	get_age(self)->int:
		return (self._p_age)

	def stat_plant(self):
		pass

class Flower(Plant):
	def	__init__(self, name:str, height:float, p_age:int, color:str)->None:
		super().__init__(name, height, p_age)
		self._color = color

class Tree(Plant):
	def	__init__(self, name:str, height:float, p_age:int, trunk_diameter:int)->None:
		super().__init__(name, height, p_age)
		self._trunk_diameter = trunk_diameter

class Vegetable(Plant):
	def	__init__(self, name:str, height:float, p_age:int, harvest_season:str, nutritional_value:float):
		super().__init__(name, height, p_age)
		self._harvest_season = harvest_season
		self._nutritional_value = round(float(nutritional_value), 1)

class Seed(Flower):
	def __init__(self, name:str, height:float, p_age:int, color:str)->None:
		super().__init__(name, height, p_age, color)

	def	bloom(self)->None:
		print(f"The {self._name} is blooming successfully")


if __name__ == "__main__":
	plante = Plant.anonymous()
	plante1 = Plant.anonymous()
	plante.show()
	print(plante.is_aYear(361))
	