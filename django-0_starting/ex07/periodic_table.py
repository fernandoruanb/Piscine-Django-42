import sys

def getTheList():
    '''
    I made that function to read the file and get all the lines to be checked after thinking
    in to build my myJson dictionary organized per element where I can get easily the name of
    each element and extract the information of them
    '''
    with open("periodic_table.txt", "r") as periodicTable:
        myPeriodicTable = []
        for line in periodicTable:
            myPeriodicTable.append(line.strip()) #remove blank spaces and mess
        return (myPeriodicTable)

def getTheJson(myPeriodicTable):
    if not myPeriodicTable:
        return None
    myJson = {}
    for line in myPeriodicTable:
        if '=' not in line or ':' not in line:
            return None
        element = line.split("=", 1)[0].strip()
        myJsonUnit = line.split("=", 1)[1].strip()
        myJson[element] = myJsonUnit
    return (myJson)

def mountHTML():
	myJson = getTheJson(getTheList())
	if not myJson:
		return None

	rows = []

	# we need to split each , and inside it we need to get : to separate field and myJson if the : exists
	# we need to clean the None in the final of each line replacing the $ (final) to an empty string
	# Finally, we finish the dictionary and we can get each position to create our HTML file

	for element, value in myJson.items():
		fields = {}
		for nextData in value.split(","):
			captured = nextData.strip().replace("$", "")
			if not ':' in captured:
				continue
			key, val = captured.split(":", 1)
			fields[key.strip()] = val.strip()
		
		position = fields.get("position", "")
		number = fields.get("number", "")
		small = fields.get("small", "")
		molar = fields.get("molar", "")
		electron = fields.get("electron", "")

		rows.append(f"""
			<table>
				<tr>
					<td style="border: 1px solid black; padding: 10px">
						<h4>{element}</h4>
						<ul>
							<li>Atomic {number}</li>
							<li>No {position}</li>
							<li>{small}</li>
							<li>{molar}</li>
							<li>{electron} electron</li>
						</ul>
					</td>
				</tr>
			</table>
		""")

	doc = f"""<!DOCTYPE html>
		 <html lang="en">
			<head>
				<meta charset="utf-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>The ultimate periodic table</title>
			</head>
			<body>
				{''.join(rows)}
			</body>
		 </html>
		"""

	with open("periodic_table.html", "w", encoding="utf-8") as file:
		file.write(doc)

def seeMyJson():
    '''
    I made that function only to see the myJson dictionary all right
    '''
    for key, value in myJson.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
	mountHTML()
