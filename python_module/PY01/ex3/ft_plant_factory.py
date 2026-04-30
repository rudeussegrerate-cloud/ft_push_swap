class Plant:
	def	__init__(self, name:str, height:float, p_age:int):
		self.name = name
		self.height = float(height)
		self.p_age = p_age
		print("Created: ",end="")
		self.show()

	def	grow(self)->None:
		self.height = round(self.height + 0.8, 1)

	def	age(self)->None:
		self.p_age = self.p_age + 1 

	def	show(self)->None:
		print(f"{self.name}: {self.height}cm, {self.p_age} days old")

if	__name__ == "__main__":
	print("=== Plant Factory Output ===")
	plante = [Plant] * 5
	plante[0] = Plant("Rose", 25, 30)
	plante[1] = Plant("Oak", 200, 365)
	plante[2] = Plant("Cactus", 5, 90)
	plante[3] = Plant("Sunflower", 200, 365)
	plante[4] = Plant("Fern", 15, 120)
