import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}

capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

def getCapitalByState(state):
	try:
		result = states[state]
		result = capital_cities[result]
		return result
	except KeyError:
		return None

if __name__ == '__main__':
	if (len(sys.argv) < 2):
		sys.exit(0)
	result = getCapitalByState(sys.argv[1])
	if not result:
		print("Unknow state")
	else:
		print(result)
