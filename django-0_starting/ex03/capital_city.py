import sys

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

	if (len(sys.argv) != 2):
		sys.exit(0)

	if (states is None or capital_cities is None 
		or not isinstance(states, dict) 
		or not isinstance(capital_cities, dict)
		or not states or not capital_cities):
			return
	try:
		state = sys.argv[1]
		sigla = states[state]
		result = capital_cities[sigla]
		if (isinstance(result, str)):
			result = result.strip()
		print(result)
	except KeyError:
		print("Unknown state")
	except IndexError:
		print ("Error: invalid index")
	except OSError as error:
		print("Error: system error {error}")

if __name__ == '__main__':
	getCapitalByState()
