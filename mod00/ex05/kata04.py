kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
	module = 'module_' + str(kata[0]).zfill(2)
	exercise = 'ex_' + str(kata[1]).zfill(2)
	decimal1 = f'{kata[2]:.2f}'
	integer = f'{kata[3]:.2e}'
	decimal2 = f'{kata[4]:.2e}'
	print(module + ", " + exercise + " : " + decimal1 + ", " + integer + ", " + decimal2)