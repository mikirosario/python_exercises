import functools

def ft_map(func, iterable):
	'''Map the function to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function
	'''
	arr = []
	for elem in iterable:
		arr.append(func(elem))
	return iter(arr)

if __name__ == "__main__":
	add1 = lambda num: num + 1
	arr = [1, 2, 3, 4]
	print(list(map(add1, arr)))
	print(list(ft_map(add1, arr)))
