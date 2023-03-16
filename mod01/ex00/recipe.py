class Recipe:
	max_width = 20
	valid_recipe_types = ["starter", "lunch", "dessert"]
	def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: str, recipe_type: str):
		valid_str_width = lambda s: 0 < len(s) <= Recipe.max_width
		validator = dict()
		validator["name"] = (lambda name: name is not None and isinstance(name, str) and valid_str_width(name) and all(ch.isalnum() or ch.isspace() for ch in name))(name)
		validator["cooking_lvl"] = (lambda lvl: lvl is not None and isinstance(lvl, int) and valid_str_width(str(lvl)) and 1 <= lvl <= 5)(cooking_lvl)
		validator["cooking_time"] = (lambda time: time is not None and isinstance(time, int) and valid_str_width(str(time)) and time >= 0)(cooking_time)
		validator["ingredients"] = (lambda ingredients: ingredients is not None and isinstance(ingredients, list) and all(isinstance(ingredient, str) and valid_str_width(ingredient) for ingredient in ingredients))(ingredients)
		validator["description"] = (lambda desc: desc is None or (isinstance(desc, str)) and (len(desc) == 0 or valid_str_width(desc)))(description)
		validator["recipe_type"] = (lambda type: type is not None and isinstance(type, str) and any(type == valid_type for valid_type in Recipe.valid_recipe_types))(recipe_type)
		args = list(validator.keys())
		for arg in args:
			if validator[arg] == False:
				raise Exception(str(f"{arg} threw an exception. RTFM."))
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = str('') if description == None else description
		self.recipe_type = recipe_type

	def __str__(self):
		return str(f"Recipe: {self.name}\nCooking Level: {str(self.cooking_lvl)}\n"
					f"Cooking Time: {str(self.cooking_time)}\nIngredients: {self.ingredients}\n"
					f"Description: {self.description}\nRecipe Type: {self.recipe_type}")
