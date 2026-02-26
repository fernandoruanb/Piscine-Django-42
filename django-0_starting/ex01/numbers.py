def readAndOutput(target: str):
	try:
		with open(target, "r") as file:
			for line in file:
				listOfnumbers = line.strip().split(",")
				for num in listOfnumbers:
					print(num.strip())
	except FileNotFoundError:
		print("Error: File not found.")
		return
	except PermissionError:
		print("Error: permission denied.")
		return
	except UnicodeDecodeError:
		print("Error: file is not valid UTF-8 text.")
		return
	except OSError as error:
		print(f"Error: the system failed with {error}")
		return

if __name__ == '__main__':
    readAndOutput("numbers.txt")
