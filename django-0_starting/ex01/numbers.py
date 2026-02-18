# Using with is more recommended because with guarantees we always close the file descriptor after that block

with open("numbers.txt", "r") as file:
	for line in file:
		listOfnumbers = line.strip().split(",")
		for num in listOfnumbers:
			print(num)

# In that example below, we do not use with and we need to close the file descriptor after it

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
