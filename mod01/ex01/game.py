class GotCharacter:
	'''This character class is amazing'''
	def __init__(self, first_name: str, is_alive: bool=True):
		self.first_name = first_name
		self.is_alive = is_alive
	
class Stark(GotCharacter):
	'''Who are these people? I regret not watching the series now'''
	def __init__(self, first_name: str=None, is_alive: bool=True):
		super().__init__(first_name, is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is coming"
	
	def print_house_words(self):
		print(self.house_words)
	
	def die(self):
		self.is_alive = False

print(GotCharacter.__doc__)
print(Stark.__doc__)
