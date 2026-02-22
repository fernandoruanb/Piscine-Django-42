def readAndOutput(target: str):
    '''
    We need to open the target file "numbers.txt" and read it line by line to print on the screen without the commas.
    Then, to solve that task we only need to open the file by a safe way, using the "with" where the file descriptor
    continues only opened while we are in the "with" scope. I also put a second example where we can see how to solve the
    same task without the "with" and yes using the open function directly, needing to close after the use
    '''

    with open(target, "r") as file:
	    for line in file:
		    listOfnumbers = line.strip().split(",")
		    for num in listOfnumbers:
			    print(num)

    '''
    file = open("numbers.txt", "r")
    try:
        for line in file:
            listOfnumbers = line.strip().split(",")
            for num in listOfnumbers:
                print(num)
    finally:
        file.close()
    '''

if __name__ == '__main__':
    readAndOutput("numbers.txt")
