import beverages
import random

class CoffeeMachine():

	def __init__(self):
		self.counter = 0
		self.fail = False

	class EmptyCup(beverages.HotBeverage):
		def __init__(self):
			super().__init__()
			self.name = "empty cup"
			self.price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.counter = 0
		self.fail = False

	def serve(self, drink):
		if (self.counter >= 10):
			raise CoffeeMachine.BrokenMachineException()
		self.counter += 1 # I register the attempt to use the machine
		#print(self.counter)
		self.fail = random.random() >= 0.7
		if (self.fail):
			return CoffeeMachine.EmptyCup()
		#drink_to_serve = getattr(beverages, beverage) if the parameter is a string not a class
		try:
			drinkToServe = drink()
		except (TypeError, AttributeError) as warning:
			return CoffeeMachine.EmptyCup()	
		return drinkToServe

try:	
	hotBeverage = CoffeeMachine()
	drink = hotBeverage.serve(beverages.Coffee)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Chocolate)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Cappucino)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Tea)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.HotBeverage)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Coffee)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Chocolate)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Cappucino)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Tea)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.HotBeverage)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Coffee)
	print(f"{drink}\n")
	hotBeverage.repair() #Test to see the repair time
	print("\nMachine repaired\n")
	# That kind of error do not come in the serve method, Attribute Error
	#drink = hotBeverage.serve(beverages.notExist)
	#print(f"{drink}")

except Exception as message:
	print(message)

hotBeverage.repair() #Test to see the repair time
print("\nMachine repaired\n")

try:
	drink = hotBeverage.serve(beverages.Coffee)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Tea)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.HotBeverage)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Coffee)
	print(f"{drink}\n")
	drink = hotBeverage.serve(beverages.Tea)
	print(f"{drink}")
	#drink = hotBeverage.serve(beverages.notExist)
	#print(f"{drink}")

except Exception as message:
	print(message)
