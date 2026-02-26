import sys

def findState(capitalInput, states, capitals):
	if (not capitalInput or not states or not capitals
		or not isinstance(capitalInput, str)
		or not isinstance(states, dict)
		or not isinstance(capitals, dict)
		or not states or not capitals):
		return None

	capitalInput = capitalInput.strip()
	for sig, city in capitals.items():
		if (capitalInput.lower() == city.lower()):
			for capital, si in states.items():
				if (sig.lower() == si.lower()):
					return capital
	return None
	

def getCapitalByState():
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
		sys.exit(1)

	if (states is None or capital_cities is None
		or not isinstance(states, dict) 
		or not isinstance(capital_cities, dict)
		or not states or not capital_cities):
			return None

	try:
		result = findState(sys.argv[1], states, capital_cities)

		if result is not None:
			if (isinstance(result, str)):
				result = result.strip()
				print (result)
		else:
			print("Unknown capital city.")
	except KeyError:
		print("Unknown capital city.")
		return None
	except IndexError:
		print("Error: Invalid index.")
		return None
	except UnicodeDecodeError:
		print("Error: Invalid format of text, it is not UTF-8.")
		return None
	except OSError as error:
		print("Error: system internal error {error}.")

if __name__ == '__main__':
	getCapitalByState()
