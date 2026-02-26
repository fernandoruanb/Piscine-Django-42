def myBeautifulFunction():

	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]

	dictionary = {};

	if d is None:
		return

	if not isinstance(d, list) or not d:
		return

	for check in d:
		if not isinstance(check, tuple) or len(check) != 2:
			return

	for name, year in d:
		if not isinstance(name, str) or not isinstance(year, str) or not year.isdigit():
			continue
		dictionary[year] = name.strip()
		print(f"{year}: {name}")

if __name__ == "__main__":
    myBeautifulFunction()
