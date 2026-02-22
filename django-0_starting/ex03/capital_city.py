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

def getCapitalByState():
    '''
        That function tries to get the first argument the user typed in the shell as a state information.
        Using that data we get the sigla and use the sigla to discover the capital relationated to the state
        printing it on the screen. I cannot handle with lowercase
    '''

    if (len(sys.argv) < 2):
        sys.exit(0)
    try:
        state = sys.argv[1]
        sigla = states[state]
        result = capital_cities[sigla]
        print(result)
    except KeyError:
        print("Unknown state")

if __name__ == '__main__':
    getCapitalByState()
