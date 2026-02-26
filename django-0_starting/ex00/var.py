def my_var():

	values = [
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

	for var in values:
		if var is None:
			continue
		if isinstance(var, str):
			var = var.strip()
		print(f"{var} has a type {type(var)}")

if __name__ == '__main__':
	my_var()
