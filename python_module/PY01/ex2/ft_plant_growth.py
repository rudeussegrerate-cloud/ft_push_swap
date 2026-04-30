class	Plant:
	def	__init__(self, name:str, height:float, p_age:int)->None:
		self.name = name
		self.height = float(height)
		self.p_age = p_age
	
	def	grow(self)->None:
		self.height = round(self.height + 0.8, 1)
	def	age(self)->None:
		self.p_age = self.p_age + 1 
	def	show(self)->None:
		print(f"{self.name}: {self.height}cm, {self.p_age} days old")

if	__name__ == "__main__":
	print("=== Garden Plant Growth ===")
	plante = Plant("Rose", 25, 30)
	plante.show()
	prev_grow = plante.height
	i = 1
	for i in range(i, 8):
		print(f"=== Day {i} ===")
		plante.grow()
		plante.age()
		plante.show()
	print(f"Growth this week: {round((plante.height - prev_grow), 1)}cm")
