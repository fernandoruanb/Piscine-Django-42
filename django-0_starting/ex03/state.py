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

def getCapitalCity(capital):
	try:
		result = states[capital]
		result = capital_cities[result]
		return result
	except KeyError:
		return None

if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit(0)
	result = getCapitalCity(sys.argv[1])
	if not result:
		print("Unknow capital city")
	else:
		print(result)
