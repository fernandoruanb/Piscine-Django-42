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

def findSiglaCapital(data):
	if not data:
		return None
	for key, value in capital_cities.items():
		if (value.lower() == data.lower()):
			return key
	return None

def findSiglaState(data):
	if not data:
		return None
	for key, value in states.items():
		if (key.lower() == data.lower()):
			return value
	return None

def isCapitalCity(data):
	if not data:
		return None
	for key,value in capital_cities.items():
		if (value.lower() == data.lower()):
			return value
	return None

def isStateTarget(data):
	if not data:
		return None
	for key,value in states.items():
		if (key.lower() == data.lower()):
			return key
	return None

def findCapitalBySigla(data):
	if not data:
		return None
	for key, value in capital_cities.items():
		if (key == data):
			return value
	return None

def findStateBySigla(data):
	if not data:
		return None
	for key, value in states.items():
		if (value == data):
			return key
	return None

def isValid(data):
	isCapital = isCapitalCity(data)
	isState = isStateTarget(data)
	if (isCapital or isState):
		# Get the official name
		# Get the capital name by sigla
		# Print
		if (isState):
			sigla = findSiglaState(isState)
			capital = findCapitalBySigla(sigla)
			print(f"{capital} is the capital of {isState}")
		else:
			sigla = findSiglaCapital(isCapital)
			state = findStateBySigla(sigla)
			print(f"{isCapital} is the capital of {state}")
	else:
		print(f"{data} is neither a capital city nor a state")

if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit(0)

	listArgs = sys.argv[1].strip().split(",")

	for arg in listArgs:
		test = arg.strip()
		if not test:
			continue
		else:
			isValid(test)
