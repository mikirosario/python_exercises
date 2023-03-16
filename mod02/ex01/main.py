def what_are_the_vars(*args, **kwargs):
	return ObjectC(*args, **kwargs)

class ObjectC(object):
	def __init__(self, *args, **kwargs):
		var_num = 0
		for arg in args:
			self.__setattr__(f"var_{var_num}", arg)
			var_num += 1
		for key, value in kwargs.items():
			self.__setattr__(key, value)
	
	def __getattr__(self, name: str):
		if not isinstance(name, str) or not name in self.__dict__:
			return None

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars("c", b='20', a=10)
	print(obj.wtf)
	doom_printer(obj)
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	doom_printer(obj)
