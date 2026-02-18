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

def findTheKeyByValue(value):
	for key, target in capital_cities.items():
		if (value == target):
			return key
	return None

def findTheStateByCapital(capital):
	for key, target in states.items():
		if (target == capital):
			return key
	return None

def getCapitalByState(capital):
	result = findTheKeyByValue(capital)
	result = findTheStateByCapital(result)
	return result

if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit(0)
	result = getCapitalByState(sys.argv[1])
	if not result:
		print("Unknow capital city")
	else:
		print(result)
