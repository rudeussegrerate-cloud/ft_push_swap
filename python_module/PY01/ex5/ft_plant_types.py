class Plant:
	def __init__(self, name:str, height:float, p_age:int)->None:
		if (height < 0 or p_age < 0):
			print("Erreur init OBJ")
			self._name = "None"
			self._height = float(0)
			self._p_age = 0
		else:
			self._name = str(name)
			self._height = float(height)
			self._p_age = p_age
			print("Created: ",end="")
			self.show()

	def grow(self)->None:
		self._height = round(self._height + 0.8, 1)

	def	age(self)->None:
		self._p_age = self.p_age + 1

	def	show(self)->None:
		print(f"{self._name}: {self._height}cm, {self._p_age} days old")

	def	set_height(self, height:float)->None:
		if (height < 0):
			print("Error, height value is wrong")
		else:
			self._height = height
			print(f"Height update: {self._height}")

	def	set_age(self, age:int)->None:
		if (age < 0):
			print("Error, age value is wrong")
		else:
			self._p_age = age
			print(f"Age update: {self._p_age}")

	def	get_height(self)->float:
		return (self._height)

	def	get_age(self)->int:
		return (self._p_age)


class Flower(Plant):
	def	__init__(self, name:str, height:float, p_age:int, color:str)->None:
		self._color = color
		super().__init__(name, height, p_age)

	def grow(self)->None:
		super().grow()

	def age(self)->None:
		super().age()
	
	def	set_age(self, age:int)->None:
		super().set_age()

	def	get_height(self)->float:
		return super().get_height()

	def	get_age(self)->int:
		return super().get_age()

	def set_color(self, color:str)->None:
		 self._color = color

	def get_color(self)->str:
		return self._color
		
	def	bloom(self)->None:
		print(f"The {self._name} is blooming successfully")

	def	show(self)->None:
		print(f"color :{self._color}, ", end = "")
		super().show()




class Tree(Plant):
	def	__init__(self, name:str, height:float, p_age:int, trunk_diameter:int)->None:
		self._trunk_diameter = trunk_diameter
		super().__init__(name, height, p_age)
		
	def grow(self)->None:
		super().grow()

	def age(self)->None:
		super().age()
	
	def	set_age(self, age:int)->None:
		super().set_age()

	def	get_height(self)->float:
		return super().get_height()

	def	get_age(self)->int:
		return super().get_age()

	def	set_trunk_diameter(self, trunk_diameter:int)->None:
		self._trunk_diameter = trunk_diameter
	
	def	get_trunk_diameter(self)->int:
		return(self._trunk_diameter)

	def	produce_shade(self)->None:
		print("+++ Ombre is produced +++")

	def	show(self)->None:
		super().show()
		print(f", trunk diameter: {self._trunk_diameter}")



class Vegetable(Plant):
	def	__init__(self, name:str, height:float, p_age:int, harvest_season:str, nutritional_value:float):
		self._harvest_season = harvest_season
		self._nutritional_value = float(nutritional_value)
		super().__init__(name, height, p_age)

	def grow(self)->None:
		super().grow()

	def age(self)->None:
		super().age()
	
	def	set_age(self, age:int)->None:
		super().set_age()

	def	get_height(self)->float:
		return super().get_height()

	def	get_age(self)->int:
		return super().get_age()

	def	set_harvest_season(self, harvest_season:str)->None:
		self._harvest_season = harvest_season

	def	set_nutritional_value(self, nutritional_value:float)->None:
		self._nutritional_value = nutritional_value
	
	def	get_harvest_season(self)->str:
		return self._harvest_season

	def	get_nutritional_value(self)->float:
		return self._nutritional_value

	def	show(self)->None:
		super().show()
		print(f"harvest season: {self._harvest_season}, nutritional value: {self._nutritional_value}")


if	__name__ == "__main__":
	print ("=== Garden Plant Types ===")
	print("=== Vegetable")
	tomate = Vegetable("Tomato", 10, 10, "April", 0)
	tomate.set_nutritional_value(20)
	tomate.set_harvest_season("Avril")
	tomate.set_nutritional_value(20)
	tomate.show()
	
	Rose = Flower("Rose", 15, 10, "red")
	Rose.bloom()

	print("=== Tree")

	Oak = Tree("Oak", 200, 365, 5)
	Oak.produce_shade()
	
	
	
