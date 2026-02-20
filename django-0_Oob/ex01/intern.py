class Coffee:

	# the constructor
	def __init__(self):
		pass

	def __str__(self):
		return "This is the worst coffee you ever tasted."

class Intern:
	# the constructor
	def __init__(self, name=None):
		if not name:
			self.internName = "My name? I’m nobody, an intern, I have no name."
		else:
			self.internName = name.strip()

	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")

	def make_coffee(self):
		coffee = Coffee()
		return (coffee)

	def __str__(self):
		return (self.internName)

A = Intern()
B = Intern("Mark")
coffee = A.make_coffee()
coffee_B = B.make_coffee()

print(f"{A}\n{B}\n{coffee}\n{coffee_B}")

try:
	A.work()
except Exception as message:
	print(message)
