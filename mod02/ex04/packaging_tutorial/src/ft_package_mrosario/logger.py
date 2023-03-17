import time
from random import randint
import os

# [1]: def outer_function():
#    ...:     print "1. This is outer function!"
#    ...:     def inner_function():
#    ...:         print "2. This is inner function, inside outer function!"
#    ...:     print "3. This is outside inner function, inside outer function!"
#    ...:     return inner_function()
# [2]: func_assign = outer_function()
# 1. This is outer function!
# 3. This is outside inner function, inside outer function!
# 2. This is inner function, inside outer function!

def log(func):
	def wrapper(instance, *args, **kwargs):
		start = time.time()
		result = func(instance, *args, **kwargs)
		end = time.time()
		diff = end - start
		units = 's'
		if diff < 1.:
			diff *= 1000
			units = 'ms'
		logfile = open("machine.log", 'a')
		logfile.write(f"{str(func.__name__ + ':').ljust(20)}[ exec-time = {diff:.3f} {units} ]\n".rjust(20))
		logfile.close()
		return result
	return wrapper

class CoffeeMachine():
	water_level = 100
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)
