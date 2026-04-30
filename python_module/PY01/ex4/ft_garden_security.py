class Plant:
	def __init__(self, name:str, height:float, p_age:int)->None:
		if (height < 0 or p_age < 0):
			print("Erreur init OBJ")
			self._name = "None"
			self._height = float(0)
			self._p_age = 0
		else:
			self._name = str(name)
			self._height = round(height, 1)
			self._p_age = int(p_age)
			print("Created: ",end="")
			self.show()

	def grow(self)->None:
			self._height = round(self._height + 0.8, 1)

	def age(self)->None:
			self._p_age = self.p_age + 1

	def show(self)->None:
		print(f"{self._name}: {self._height}cm, {self._p_age} days old")

	def set_height(self, height)->None:
		if (height < 0):
			print("Error, height value is wrong")
		else:
			self._height = round(height, 1)
			print(f"Height update: {self._height}")

	def set_age(self, age)->None:
		if (age < 0):
			print("Error, age value is wrong")
		else:
			self._p_age = int(age)
			print(f"Age update: {self._p_age}")

	def get_height(self)->float:
		return (self._height)

	def get_age(self)->int:
		return (self_p_age)

if __name__ == "__main__":
	print("=== Garden Security System ===")
	plante = Plant("Rose", 2, 20)
	plante.set_age(10)
	plante.show()
