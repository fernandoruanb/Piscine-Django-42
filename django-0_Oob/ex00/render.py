import settings
import sys

if (len(sys.argv) != 2 or '.' not in sys.argv[1].strip()):
	sys.exit(0)

file = sys.argv[1].strip().split('.', 1)

fileName = file[0]
extension = file[1]

if extension != "template":
	sys.exit(0)

output = None

with open(f"{sys.argv[1]}", "r") as inputFile:
	output = inputFile.read()

# vars returns a dictionary of all variables in our target file imported, items to keep the format key and value
# and we avoid the internal variables excluding any variable starting with "_"

# I desire the format key:value for each k and v in vars(settings).items, it is a dictionary, if not k.startswith _
# because "_" means internal variables, everything inside {} to make a new dictionary

insertValues = {k:v for k, v in vars(settings).items() if not k.startswith("_")}

try:
	# format_map = it is the function we need to use to change each {name}, for example, for the correspondet value
	temp = output.format_map(insertValues)
	output = temp
except KeyError:
	sys.exit(1)

with open(f"{fileName}.html", "w") as outputFile:
	outputFile.write(output)

print("Success")
