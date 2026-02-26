import sys

def isState(stateInput, states, capital_cities):
	if (stateInput is None or states is None or capital_cities is None
		or not isinstance(stateInput, str)
		or not isinstance(states, dict)
		or not isinstance(capital_cities, dict)):
			return None
	for state, sigla in states.items():
		if (state.strip().lower() == stateInput.strip().lower()):
			for sig, city in capital_cities.items():
				if (sig.strip().lower() == sigla.strip().lower()):
					return [city.strip(), state.strip()]
	return None

def isCapital(capitalInput, states, capital_cities):
	if (capitalInput is None or states is None
		or capital_cities is None
		or not isinstance(capitalInput, str)
		or not isinstance(states, dict)
		or not isinstance(capital_cities, dict)):
			return None
	for sigla, capital in capital_cities.items():
		if (capitalInput.strip().lower() == capital.strip().lower()):
			for state, sig in states.items():
				if (sigla.strip().lower() == sig.strip().lower()):
					return [capital.strip(), state.strip()]
	return None
	
def isValid():
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

	if len(sys.argv) != 2:
		sys.exit(0)
	try:
		listArgs = sys.argv[1].strip().split(",")
	except IndexError:
		print("Error: invalid index.")
		sys.exit(1)
	except OSError as error:
		print("Error: I/O {error}.")
		sys.exit(1)
 
	for arg in listArgs:
		test = arg.strip()
		if not test:
			continue
		else:
			isCap = isCapital(test, states, capital_cities)
			isSt = isState(test, states, capital_cities)
			if (isCap):
				print(f"{isCap[0]} is the capital of {isCap[1]}")
			elif (isSt):
				print(f"{isSt[0]} is the capital of {isSt[1]}")
			else:
				print(f"{test} is neither a capital city nor a state")

if __name__ == '__main__':
    isValid()
