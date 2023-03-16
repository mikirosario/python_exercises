import string
import sys

def exit_fatal(str: string):
	print(str)
	sys.exit()

def main():
	args = sys.argv[1:]
	if len(args) != 1:
		exit_fatal("Pass a single argument or die")
	str = args[0]
	sign = 0
	index = 0
	for ch in str:
		if ch == '-':
			sign -= 1
			index += 1
		elif ch == '+':
			sign += 1
			index += 1
		else:
			break
	str = str[index:]
	if(not str.isdigit()):
		exit_fatal("Pass a numeric value only")
	num = int(str)
	if sign < 0: #ni me preguntes por qué hago esto, porque sí xD
		num *= -1
	if num == 0:
		print("I'm Zero")
	elif num % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")

if __name__ == "__main__":
	main()