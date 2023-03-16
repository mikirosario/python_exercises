import math

cookbook = dict()
options = ["Add a recipe", "Delete a recipe", "Print a recipe", "Print the cookbook", "Quit"]
max_name_length = 20

def add_recipe(name: str, ingredients: list, type: str, prep_time: int):
	if name is None or len(name) == 0 or ingredients is None or type is None or prep_time < 0:
		print("ERROR: Bad user. Please contact user administrator and request user replacement.")
		return
	recipe = {"ingredients": ingredients, "meal": type, "prep_time": prep_time}
	cookbook[name.casefold()] = recipe
	
def print_recipe_names():
	recipenames = cookbook.keys()
	for name in recipenames:
		print(name)

def print_recipe_details(recipe_name: str):
	if recipe_name is None or cookbook.get(recipe_name.casefold()) is None:
		print("HOW DARE YOU pass me an invalid argument! I demand to speak to the manager!")
		return
	recipe = cookbook.get(recipe_name.casefold())
	print(f"\nRecipe for {recipe_name}:")
	recipekeys = list(recipe.keys())
	print(f"Ingredients list: {recipe[recipekeys[0]]}")
	print(f"To be eaten for {recipe[recipekeys[1]]}")
	print(f"Takes {recipe[recipekeys[2]]} minute(s) of cooking")

def remove_recipe(recipe_name: str):
	if recipe_name is None or cookbook.get(recipe_name.casefold()) is None:
		print("Yeah... it doesn't exist... so I just ran rm -rf on your root directory.")
		return
	cookbook.pop(recipe_name.casefold())
	print("Okay! Recipe deleted.")

def print_option_list():
	print("List of available options:")
	i = 0
	for option in options:
		print(str((i + 1)) + ": " + option)
		i += 1

def invalid_option(option: str):
	digit_count = lambda num: int(math.log10(num)) + 1
	if (len(option) != digit_count(len(options)) or not option.isdigit()):
		print("\nLook. It's REALLY simple. All you have to do is write the number of the option you want. That's it!")
	elif int(option) > len(options) or int(option) < 1:
		print(f"\nReread that list of options. There are {len(options)} options. Do you see {option} anywhere? Well? DO YOU!?")
	else:
		return False
	return True

def get_recipe_name_from_user():
	valid_recipe_name = lambda s: s is not None and not len(s) > max_name_length and s.isprintable()
	print("Please name your recipe:")
	name = input()
	while(not valid_recipe_name(name)):
		print(f"It's a recipe, not Elon's next child. Choose a normal name, and make sure it isn't longer than {max_name_length} characters:")
		name = input()
	return name

def get_ingredients_list_from_user():
	valid_ingredient = lambda s: s is not None and not len(s) > max_name_length and s.isprintable()
	valid_continue = lambda s: s is not None and not len(s) > 3 and s.casefold() == str('yes').casefold() or s.casefold() == str('y').casefold() or s.casefold() == str('si').casefold() or s.casefold() == str('sí').casefold()
	print("Please provide an ingredient:")
	ingredients = list()
	ingredient = input()
	done = False
	while(not valid_ingredient(ingredient) or not done and len(ingredients) < 50):
		is_valid_ingredient = valid_ingredient(ingredient)
		if is_valid_ingredient:
			ingredients.append(ingredient)
			print("Mmmm hmmm, got it. Any more ingredients? [yes/no]")
			cont = input()
			if not valid_continue(cont):
				if(cont.casefold() == str('oui').casefold()):
					print("Desolé, je ne parle pas le français.")
				else:
					print("I'll take that as a no.")
				done = True
				continue
		if not is_valid_ingredient:
			print(f"I need an ingredient. Normally these consist of one or more words with printable letters. Words not longer than {max_name_length} characters.")
		else:
			print("Please provide another ingredient")
		ingredient = input()	
	if len(ingredients) == 50:
		print("I'm starting to suspect you are trying to flood my RAM with garbage. You wouldn't do something like that, would you?\n50 ingredients is more than enough for any normal recipe.")
	return ingredients

def get_meal_type_from_user():
	valid_meal_type = lambda s: s is not None and not len(s) > max_name_length and s.isprintable()
	print("Now please state the type of meal ('lunch', 'desert', etc.)")
	meal = input()
	while (not valid_meal_type(meal)):
		print(f"Much like recipe names, meal names generally consist of words with printable letters not more than {max_name_length} characters long, and not whatever that abomination was.")
		meal = input()
	return meal

def get_preparation_time_from_user():
	valid_prep_time = lambda s: s is not None and not len(s) > 6 and s.isdigit()
	print("Finally, how long does it take to prepare this meal in whole Earth minutes? No decimals please, we don't do that here.\nAnd don't go into the millions of minutes.")
	prep_time = input()
	while (not valid_prep_time(prep_time)):
		print(f"What a way to spend your time! Just write a positive integer that is less than 1000000. I can wait all day.")
		prep_time = input()
	return prep_time

def add_recipe_option():
	name = get_recipe_name_from_user()
	ingredients = get_ingredients_list_from_user()
	meal = get_meal_type_from_user()
	prep_time = int(get_preparation_time_from_user())
	add_recipe(name, ingredients, meal, prep_time)
	print(f"Okay! {name} has been added to the cookbook.")

def delete_recipe_option():
	print("What is the name of the recipe you would like to delete?")
	recipe_name = input()
	remove_recipe(recipe_name)

def print_recipe_option():
	print("What is the name of the recipe you would like to print?")
	recipe_name = input()
	print_recipe_details(recipe_name)
	
def handle_option(option: int):
	if options[option] == "Add a recipe":
		print()
		add_recipe_option()
		print()
	if options[option] == "Delete a recipe":
		print()
		delete_recipe_option()
		print()
	if options[option] == "Print a recipe":
		print()
		print_recipe_option()
		print()
	if options[option] == "Print the cookbook":
		print()
		print_recipe_names()
		print()
	if options[option] == "Quit":
		print("Cookbook closed. Goodbye!")
		exit(0)

def main():
	add_recipe("bocadillo", ["jamón", "pan", "queso", "tomate"], "almuerzo", 10)
	add_recipe("tarta", ["harina", "azúcar", "huevos"], "postre", 60)
	add_recipe("ensalada", ["aguacate", "rúcula", "tomates", "espinacas"], "almuerzo", 15)
	while (True):
		print_option_list()
		print("Please select an option")
		option = input()
		if (not invalid_option(option)):
			handle_option(int(option) - 1)

if __name__ == "__main__":
	main()
