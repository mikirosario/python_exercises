import string
import sys

def text_analyzer(msg: str = None):
	'''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
	assert msg is None or isinstance(msg, str) and len(msg) > 0, "text_analyzer expects a string biiish"
	if msg is None:
		msg = input("You must have forgotten to write something in your string. ¬¬\n")
	total_chars = len(msg)
	upper_case_letters = 0
	lower_case_letters = 0
	punctuation_marks = 0
	spaces = 0
	for c in msg:
		if c.isupper():
			upper_case_letters += 1
		elif c.islower():
			lower_case_letters += 1
		elif c in string.punctuation:
			punctuation_marks += 1
		elif c.isspace():
			spaces += 1
	print("This text contains " + str(total_chars) + " character(s)\n"
	"- " + str(upper_case_letters) + " upper letter(s)\n"
	"- " + str(lower_case_letters) + " lower letter(s)\n"
	"- " + str(punctuation_marks) + " punctuation mark(s)\n"
	"- " + str(spaces) + " space(s)"
	)
print(text_analyzer.__doc__)
if __name__ == "__main__":
	argc = len(sys.argv[1:])
	if (argc > 1):
		print("text_analyzer only wants ONE == 1 argument")
	else:
		text_analyzer(sys.argv[1] if argc > 0 else None)

