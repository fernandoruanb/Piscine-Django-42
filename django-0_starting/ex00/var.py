def my_var():

    '''
    That function created a list of vars to make simple the visualization printing
    with just a loop for to see the variable and its type

    '''

    vars = [
		42,
		"42",
		"quarante-deux",
		42.0,
		True,
		[42],
		{42: 42},
		(42,),
		set()
	]

    for var in vars:
        print(f"{var} has a type {type(var)}")

if __name__ == '__main__':
	my_var()
