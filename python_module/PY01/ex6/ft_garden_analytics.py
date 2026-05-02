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


class Flower(Plant):
	def	__init__(self, name:str, height:float, p_age:int, color:str)->None:
		super().__init__(name, height, p_age)
		self._color = color

	def get_color(self)->None:
		return self._color

	def set_color(self, value):
		self._color = value


class Tree(Plant):
	def	__init__(self, name:str, height:float, p_age:int, trunk_diameter:int)->None:
		super().__init__(name, height, p_age)
		self._trunk_diameter = trunk_diameter
		self._stat = Tree.stat()

	class stat(Plant.stat):
		def __init__(self)->None:
			super().__init__()
			self._shade = 0
	
		def get_shade(self):
			return self._shade

		def set_shade(self, value):
			self._shade += value

	def produce_shader(self)->None:
		print(f"Tree {self._name} now produces a shade of {self._height} long and {self._trunk_diameter} wide.")
		self._stat.set_shade(1)

	def get_trunk_diameter(self)->int:
		return self._trunk_diameter

	def set_trunk_diameter(self, value:int)->None:
		self._trunk_diameter = value
	
	def show(self)->None:
		super().show()
		print(f"trunk diameter: {self._trunk_diameter}")

	def stat_plant(self)->None:
		super().stat_plant()
		print(f"shader: {self._stat.get_shade()}")

class Vegetable(Plant):
	def	__init__(self, name:str, height:float, p_age:int, harvest_season:str, nutritional_value:float):
		super().__init__(name, height, p_age)
		self._harvest_season = harvest_season
		self._nutritional_value = round(float(nutritional_value), 1)

	def get_harvest_season(self)->str:
		return self._harvest_season

	def set_harvest_season(self, value:str)->None:
		self._harvest_season = value

	def get_nutritional_value(self)->str:
		return self._nutritional_value

	def set_nutritional_value(self, value:float)->None:
		self._nutritional_value = value

class Seed(Flower):
	def __init__(self, name:str, height:float, p_age:int, color:str)->None:
		super().__init__(name, height, p_age, color)
		self._graine = 0

	def get_graine(self)->int:
		return self._graine

	def set_graine(self, value:int)->None:
		self._graine = value

	def	bloom(self)->None:
		print(f"The {self._name} is blooming successfully")
		self._graine = self._graine + 1
	
	def show(self)->None:
		super().show()
		print(f"Seed: {self._graine}")

def	global_stat(plante:Plant)->None:
	print(f"== {plante._name} Statistic ==")
	plante.stat_plant()


if __name__ == "__main__":
	plante = Tree("menth", 20, 20, 180)
	plante1 = Seed("Rose", 10, 10, "Red")
	plante.age()
	plante.produce_shader()
	plante.show()
	plante.stat_plant()
	plante1.bloom()
	plante1.bloom()
	plante1.show()
	print(plante.is_aYear(500))
	global_stat(plante)
	global_stat(plante1)
