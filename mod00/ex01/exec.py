import sys
import string
def invert(str: string):
	return str[::-1]

def main():
	args = sys.argv[1:]
	newstr = ""
	if (len(args) < 1):
		print("No strings provided")
		return
	for arg in args:
		newstr += invert(arg).swapcase() + ("" if arg is args[-1] else " ")
	print(newstr)
if __name__ == "__main__":
    main()