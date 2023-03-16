import datetime
from recipe import Recipe

class Book:
	max_width = 10

	def __init__(self, name: str):
		valid_str_width = lambda s: 0 < len(s) <= Book.max_width
		validate_name = lambda name: name is not None and isinstance(name, str) and valid_str_width(name) and all(ch.isalnum() or ch.isspace() for ch in name)
		if validate_name(name) == False:
			raise Exception(str(f"{name} threw an exception. RTFM."))
		self.name = name
		self.last_update = self.creation_time = datetime.datetime.now()
		self.recipes_list = dict()
		for type in Recipe.valid_recipe_types:
			self.recipes_list[type] = dict()
	
	def get_recipe_by_name(self, name: str):
		if (name is not None and isinstance(name, str)):
			book_key_set = self.recipes_list.keys()
			for rlist in self.recipes_list:
				got_recipe = self.recipes_list[rlist][name] if name in self.recipes_list[rlist] else None
				if (got_recipe != None):
					break
			if (got_recipe == None):
				print(f"{name} does not exist in the recipe book {self.name}")
			else:
				print(f"{str(got_recipe)}")
			return got_recipe
		return None
	
	def get_recipes_by_type(self, type: str):
		if (type is not None and isinstance(type, str)):
			key_set = self.recipes_list.keys()
			if type in key_set:
				return self.recipes_list.get(type)
		return None
	
	def add_recipe(self, recipe: Recipe):
		if (recipe is None or not isinstance(recipe, Recipe)):
			print(f"Not a recipe")
		else:
			self.recipes_list[recipe.recipe_type][recipe.name] = recipe
			lastUpdate = datetime.datetime.now()


	


