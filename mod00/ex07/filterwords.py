import sys
import string

def filter_words(wordstr: str, num: int):
	wordlst = wordstr.split()
	condition = lambda ch : ch not in string.punctuation
	#filteredlst = [s for s in wordlst if sum(condition(ch) for ch in s) > num] #my eyes!!!!! :_(
	#retlst = [''.join(filter(lambda ch : ch not in string.punctuation, s)) for s in filteredlst] #This abomination is so horrifying it was banned by the subject
	retlst = [s.translate(str.maketrans('', '', string.punctuation)) for s in [s for s in wordlst if sum(condition(ch) for ch in s) > num]] #Shield your virgin eyes!!!!! Cthulu!!!! I've seen Cthulu!!!!!
	return retlst

def valid_args(args: list):
	if len(args) != 2 or len(args[0]) < 1 or not args[1].isdigit():
		return False
	return True

def main():
	args = sys.argv[1:]
	if not valid_args(args):
		print("\nBad arguments. Give me two (2) arguments.\n"
		"First argument must be a string of words separated by spaces (S).\n"
		"Second argument must a positive integer (N).\n"
		"I will print a list of all words in S with more than N characters that aren't punctuation marks.\nJust what you've always wanted, I know.\n")
		return
	print(filter_words(args[0], int(args[1])))

if __name__ == "__main__":
	main()
