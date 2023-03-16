
def ft_filter(func, iterable):
	'''Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.'''
	arr = []
	for elem in iterable:
		if func(elem) == True:
			arr.append(elem)
	return iter(arr)

if __name__ == "__main__":
	iseven = lambda num: num % 2 == 0
	arr = [1, 2, 3, 4]
	print(list(filter(iseven, arr)))
	print(list(ft_filter(iseven, arr)))
