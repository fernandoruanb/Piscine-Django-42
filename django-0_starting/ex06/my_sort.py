d = {
'Hendrix' : '1942',
'Allman' : '1946',
'King' : '1925',
'Clapton' : '1945',
'Johnson' : '1911',
'Berry' : '1926',
'Vaughan' : '1954',
'Cooder' : '1947',
'Page' : '1944',
'Richards' : '1943',
'Hammett' : '1962',
'Cobain' : '1967',
'Garcia' : '1942',
'Beck' : '1944',
'Santana' : '1947',
'Ramone' : '1948',
'White' : '1975',
'Frusciante': '1970',
'Thompson' : '1949',
'Burton' : '1939',
}


# To explain the function, we can create one or put an anonymous one, using the lambda

"""
def getTheRule(item):
	name, year = item
	return (int(year), name)
"""

# the function sorted 
if __name__ == '__main__':
	# lambda is an anonymous function just to return the next item, the value to order by it
	ordered = dict(sorted(d.items(), key=lambda item: (int(item[1]), item[0])))
	for key in ordered: # We do not need to use ordered.items() because we want only the key
		print(f"{key}")
