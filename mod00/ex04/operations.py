import sys
def print_operations(n1: int, n2: int):
	print("Sum: \t\t" + str(n1 + n2))
	print("Difference: \t" + str(n1 - n2))
	print("Product: \t" + str(n1 * n2))
	print("Quotient: \t" + str(n1 / n2) if n2 != 0 else "ERROR (division by zero)")
	print("Remainder: \t" + str(n1 % n2) if n2 != 0 else "ERROR (modulo by zero)")

def has_integers(args):
	if not isinstance(args, list) and not all(isinstance(arg, str) for arg in args):
		return False
	for arg in args:
		i = 0
		for ch in arg:
			if ch == '-' or ch == '+':
				i += 1
		if not arg[i:].isdigit():
			return False
	return True

def get_integer(arg: str):
	sign = 0
	i = 0
	for ch in arg:
		if ch == '-':
			sign -= 1
			i += 1
		elif ch == '+':
			sign += 1
			i += 1
		else:
			break
	return int(arg[i:]) * -1 if sign < 0 else int(arg[i:])

def main():
	args = sys.argv[1:]
	assert len(args) == 2, "must have two arguments"
	assert has_integers(args), "only integers"
	n1 = get_integer(args[0])
	n2 = get_integer(args[1])
	print_operations(n1, n2)

if __name__ == "__main__":
	main()
