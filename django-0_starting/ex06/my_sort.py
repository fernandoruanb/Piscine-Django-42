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

def sortTheDictionary():
    '''
    That function was necessary to order everything. To make the ordered dictionary I needed to use
    the native function sorted and specify the key by an anonymous function where it returns always
    the year. But, if we have the same year, we can get conflict, then, in this case, I return the name
    to order alphabetically. I have another example below

    def getTheRule(item):
    name, year = item
    return (int(year), name)

    We can get the same behaviour using this example.
    '''
    ordered = dict(sorted(d.items(), key=lambda item: (int(item[1]), item[0])))
    for key in ordered: # We do not need to use ordered.items() because we want only the key
        print(f"{key}")

if __name__ == '__main__':
    sortTheDictionary()
