import functools

def ft_reduce(func, iterable):
	'''Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.'''
	res = iterable[0]
	for elem in iterable[1:]:
		res = func(res, elem)
	return res

if __name__ == "__main__":
	mult = lambda x, y: x * y
	add = lambda x, y: x + y
	lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
	arr = [1, 2, 3, 4]
	print(functools.reduce(mult, arr))
	print(ft_reduce(mult, arr))
	print(functools.reduce(add, lst))
	print(ft_reduce(add, lst))
