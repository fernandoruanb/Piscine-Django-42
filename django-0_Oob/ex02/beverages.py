class HotBeverage:

	def __init__(self):
		self.price = 0.30
		self.name = "hot beverage"
	
	def description(self):
		return "Just some hot water in a cup."

	def __str__(self):
		return f"name: {self.name}\nprice: {self.price}\ndescription: {self.description()}"

class Coffee(HotBeverage):
	def __init__(self):
		super().__init__() # we can initialize all the attributes in the main class and edit them
		self.price = 0.40
		self.name = "coffee"

	def description(self): # If we need to override a method, we rewrite it in the derivated class
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "tea"

class Chocolate(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "chocolate"
		self.price = 0.50

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappucino(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "cappuccino"
		self.price = 0.45

	def description(self):
		return "Un po’ di Italia nella sua tazza!"

hotBeverage = HotBeverage()
print(f"{hotBeverage}\n")
desc = hotBeverage.description()
print(f"Test description: {desc}\n")
hotBeverage = Chocolate()
print(f"{hotBeverage}\n")
desc = hotBeverage.description()
print(f"Test description: {desc}\n")
hotBeverage = Coffee()
print(f"{hotBeverage}\n")
desc = hotBeverage.description()
print(f"Test description: {desc}\n")
hotBeverage = Tea()
print(f"{hotBeverage}\n")
desc = hotBeverage.description()
print(f"Test description: {desc}\n")
hotBeverage = Cappucino()
print(hotBeverage)
desc = hotBeverage.description()
print(f"\nTest description: {desc}")
