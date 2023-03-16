import re
import random

UNIQUE = "unique"
ORDERED = "ordered"
SHUFFLE = "shuffle"
options_list = [UNIQUE, ORDERED, SHUFFLE]

def generator(text: str, sep: str=" ", option: str=None):
	'''generator.py $STRING $OPTION
	OPTIONS:
	shuffle: Randomize list of words
	unique: Eliminate duplicate words
	ordered: Ordena las palabras alfabéticamente
	Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
	Option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
	Si quieres más de una opción te jodes y haces un pipe porque no viene en el subject
	
	'''
	validate_option = lambda option: option is None or any([option == elem for elem in options_list])
	if not text.isprintable() or not validate_option(option):
		print("ERRORüna")
		return(-1)
	word_lst = re.sub(' +', ' ', text).split(sep)
	if option == UNIQUE:
		word_lst = list(dict.fromkeys(word_lst))
	elif option == ORDERED:
		word_lst = sorted(word_lst, key=str.lower)
		print(word_lst)
	elif option == SHUFFLE:
		for i in range(len(word_lst) - 1, -1, -1):
			j = random.randint(0, i+1)
			word_lst[i], word_lst[j] = word_lst[j], word_lst[i]
	for word in word_lst:
		yield word
print(generator.__doc__)
