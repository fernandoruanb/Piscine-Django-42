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

def findSiglaCapital(capitalInput):
    '''
    The objective here is to find the sigla by the capital name and returns it.
    If I do not have the sigla, I returns None.
    '''
    if not capitalInput:
	    return None
    for sigla, capital in capital_cities.items():
	    if (capital.lower() == capitalInput.lower()):
		    return sigla
    return None

def findSiglaState(state):
    '''
    The objective here is to find a sigla by the states dictionary, I return None if
    the sigla is not valid
    '''
    if not state:
        return None
    for stateName, sigla in states.items():
        if (stateName.lower() == state.lower()):
            return sigla
    return None

def isCapitalCity(capitalInput):
    '''
    That function is to detect if the user typed a valid capital or not
    I always return the official capital name to correct input problems
    '''
    if not capitalInput:
	    return None
    for sigla, capitalName in capital_cities.items():
        if (capitalName.lower() == capitalInput.lower()):
            return capitalName
    return None

def isStateTarget(stateInput):
    '''
    That function is to detect if the user typed a valid state or not
    '''
    if not stateInput:
	    return None
    for stateName, sigla in states.items():
        if (stateName.lower() == stateInput.lower()):
            return stateName
    return None

def findCapitalBySigla(siglaInput):
    '''
    I wrote that function to find a capital by a sigla and returns it easily or None
    if the capital does not exist
    '''
    if not siglaInput:
        return None
    for sigla, capitalName in capital_cities.items():
        if (sigla == siglaInput):
            return capitalName
    return None

def findStateBySigla(data):
    '''
    I wrote that function to find a state by a sigla and returns it easily or None
    if the state does not exist
    '''
    if not data:
        return None
    for key, value in states.items():
        if (value == data):
            return key
    return None

def isValid():
    '''
    My isValid function must need to validate the input, separate each one by commas and remove
    the unnecessary spaces, tabs by strip() and put to analyze only what I need to check, showing the
    appropriate output for state and also if you put a capital with the correct values.
    '''
    if len(sys.argv) != 2:
        sys.exit(0)
    listArgs = sys.argv[1].strip().split(",")
    for arg in listArgs:
        test = arg.strip()
        if not test:
            continue
        else:
            isCapital = isCapitalCity(test)
            isState = isStateTarget(test)
            if (isCapital or isState):
                if (isState):
                    print(f"{findCapitalBySigla(findSiglaState(isState))} is the capital of {isState}")
                else:
                    print(f"{isCapital} is the capital of {findStateBySigla(findSiglaCapital(isCapital))}")
            else:
                print(f"{test} is neither a capital city nor a state")

if __name__ == '__main__':
    isValid()
