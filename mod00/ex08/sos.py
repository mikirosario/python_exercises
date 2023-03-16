import sys

morse_cipher = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
				"F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
				"K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
				"P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
				"U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
				"Z": "--..", "Á": ".--.-", "Ä": ".-.-", "É": ".._..", "Ñ": "--.--",
				"Ö": "---.", "Ü": "..--", "0": "-----", "1": ".----", "2": "..---",
				"3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
				"8": "---..", "9": "----."}

def convert_to_morse(msg: str):
	msg = msg.upper()
	msg = msg.replace(" ", "/")
	msg = ' '.join(msg)
	retmsg = msg.upper().translate(str.maketrans(morse_cipher))
	retmsg = retmsg.replace(chr(26), " ")
	return retmsg

def valid_args(args: list):
	if len(args) < 1 or not all(all(ch.isalnum() or ch.isspace() for ch in s) for s in args):
		return False
	return True

def main():
	args = sys.argv[1:]
	if not valid_args(args):
		print("Write a normal message in alphanumeric characters with spaces.")
		return
	msg = str()
	for arg in args:
		msg += arg + (" " if arg is not args[-1] else "")
	print(convert_to_morse(msg))

if __name__ == "__main__":
	main()
