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

def findTheCapitalSigla(capital):
    '''
    That function is useful to get the sigla of the target capital.
    It is important to get the name of the related state.
    '''
    for key, target in capital_cities.items():
        if (capital == target):
            return key
    return None

def findTheStateByCapital(targetSigla):
    '''
    After getting the sigla, we can find easily the state information to show to the user.
    '''
    for key, sigla in states.items():
        if (sigla == targetSigla):
            return key
    return None

def getCapitalByState():
    '''
    I made that function thinking about the communication between the dictionaries.
    To solve it, I needed two functions, one to get the sigla by capital and another to find the correct state.
    If I do not find the state, it does not exist. Then, I print "Unknown capital city", solving the problem.
    '''
    if len(sys.argv) < 2:
        sys.exit(0)
    result = findTheStateByCapital(findTheCapitalSigla(sys.argv[1]))
    if result is not None:
        print (result)
    else:
        print("Unknown capital city")

if __name__ == '__main__':
	getCapitalByState()
