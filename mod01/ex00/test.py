from recipe import Recipe
from book import Book

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def recipe_name_tests():
	ret = True
	except_err = lambda test_num: print(f"{bcolors.FAIL}Test {test_num} threw but shouldn't have{bcolors.ENDC}")
	else_err = lambda test_num: print(f"{bcolors.FAIL}Test {test_num} didn't throw but should have{bcolors.ENDC}")
	success = lambda test_num: print(f"{bcolors.OKGREEN}Test {test_num} successful{bcolors.ENDC}")
	try:
		recipe1 = Recipe("Name", 1, 0, ["greeedies"], "Desc", Recipe.valid_recipe_types[0])
	except:
		except_err(1)
		ret = False
	else:
		success(1)
	try:
		recipe2 = Recipe("", 1, 0, [""], "Desc", Recipe.valid_recipe_types[0])
	except:
		success(2)
	else:
		else_err(2)
		ret = False
	try:
		recipe3 = Recipe(None, 1, 0, [""], "Desc", Recipe.valid_recipe_types[0])
	except:
		success(3)
	else:
		else_err(3)
		ret = False
	try:
		recipe4 = Recipe("Name!", 1, 0, [""], "Desc", Recipe.valid_recipe_types[0])
	except:
		success(4)
	else:
		else_err(4)
		ret = False
	try:
		recipe5 = Recipe("afdñlkjfadfsdafjdalkñsfjdsklfjkldsfdlñkfjlksaflkasfdjlkañsfjkldsñafjñlkajflkdsjalkfsjlñfkjdañ", 1, 0, [""], "Desc", Recipe.valid_recipe_types[0])
	except Exception as e:
		success(5)
	else:
		else_err(5)
		ret = False
	try:
		recipe6 = Recipe("Filete", 1, 8, ["aceite", "sal", "amor", "ternera"], "", "starter")
	except:
		except_err(6)
		ret = False
	else:
		success(6)
	return ret

def recipe_book_tests():
	recipe_book = Book("Arguiñano")
	print(f"{bcolors.HEADER}Created: {recipe_book.creation_time}{bcolors.ENDC}")
	
	recipe_book.add_recipe(Recipe("Filete", 1, 8, ["aceite", "sal", "amor", "ternera"], "ehh", "starter"))
	recipe_book.get_recipe_by_name("Filete")
	print(recipe_book.get_recipes_by_type("starter"))
	print(recipe_book.get_recipes_by_type(None))
	print(recipe_book.get_recipe_by_name(None))
	print(recipe_book.get_recipe_by_name("No sssssssisto"))
	print(recipe_book.get_recipes_by_type("nosssssisto"))

def recipe_tests():
	if not recipe_name_tests():
		print(f"{bcolors.FAIL}KO{bcolors.ENDC}")
	else:
		print(f"{bcolors.OKCYAN}OK{bcolors.ENDC}")

def main():
	recipe_tests()
	recipe_book_tests()


if __name__ == "__main__":
	main()