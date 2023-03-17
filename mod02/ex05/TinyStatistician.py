import math
import numpy as np

class TinyStatistician:
	bad_arg = lambda x: x is None \
							or not ((isinstance(x, np.ndarray) and x.size > 0)\
							or isinstance(x, list) and ((all(isinstance(elem, int) or isinstance(elem, float) for elem in x) and len(x) > 0) \
								or (all(isinstance(elem, list) for elem in x) and all(all(isinstance(subelem, int) or isinstance(subelem, float) for subelem in elem) for elem in x) and any(len(elem) > 0 for elem in x))))\

	@staticmethod
	def __count(x):
		c = 0
		for elem in x:
			c += 1 if not isinstance(elem, list) else len(elem)
		return c
	
	@staticmethod
	def __matrix_to_sorted_lst(x):
		sorted_lst = []
		for elem in x:
			if not isinstance(elem, list):
				sorted_lst.append(elem)
			else:
				for subelem in elem:
					sorted_lst.append(subelem)
		sorted_lst.sort()
		return sorted_lst
	
	@staticmethod
	def __median(x):
		sorted_arr_len = len(x)
		last_pos = sorted_arr_len - 1
		return x[last_pos // 2] if sorted_arr_len % 2 != 0 else (x[last_pos // 2] + x[last_pos // 2 + 1]) / 2

	@staticmethod
	def mean(x):
		if TinyStatistician.bad_arg(x):
			return None
		m = 0
		elem_total = TinyStatistician.__count(x)
		for elem in x:
			m += elem if not isinstance(elem, list) else sum(num for num in elem)
		return m / elem_total

	@staticmethod
	def median(x):
		if TinyStatistician.bad_arg(x):
			return None
		sorted_arr = TinyStatistician.__matrix_to_sorted_lst(x)
		return TinyStatistician.__median(sorted_arr)
	
	@staticmethod
	def quartiles(x):
		if TinyStatistician.bad_arg(x):
			return None
		sorted_arr = TinyStatistician.__matrix_to_sorted_lst(x)
		sorted_arr_len = len(sorted_arr)
		lower_quartile = []
		upper_quartile = []
		if (sorted_arr_len % 2 != 0):
			for elem in sorted_arr[:sorted_arr_len // 2]:
				lower_quartile.append(elem)
			for elem in sorted_arr[sorted_arr_len // 2 + 1:]:
				upper_quartile.append(elem)
		else:
			for elem in sorted_arr[:sorted_arr_len // 2]:
				lower_quartile.append(elem)
			for elem in sorted_arr[sorted_arr_len // 2:]:
				upper_quartile.append(elem)
		quartiles = [TinyStatistician.__median(lower_quartile), TinyStatistician.__median(upper_quartile)]
		return quartiles

	def var(x):
		if TinyStatistician.bad_arg(x):
			return None
		square = lambda val: pow(val, 2)
		vals = TinyStatistician.__matrix_to_sorted_lst(x)
		mean = TinyStatistician.mean(x)
		deviations = [val - mean for val in vals]
		squared_deviations = list(map(square, deviations))
		sum_of_squares = sum(squared_deviations)
		return (sum_of_squares / len(vals))
	
	def std(x):
		if TinyStatistician.bad_arg(x):
			return None
		return math.sqrt(TinyStatistician.var(x))

if __name__ == "__main__":
	a = [1, 42, 300, 10, 59]
	b = [[1], [42], [300], [10], [59]]
	c = [1, 42, 300, 10, 59, 69]
	d = [[1, 42], [300, 10], [59, 69]]
	nd = np.array([1, 42, 300, 10, 59])
	print(TinyStatistician.mean(a))
	print(TinyStatistician.mean(b))
	print(TinyStatistician.mean(nd))
	print(TinyStatistician.mean(c))
	print(TinyStatistician.mean(d))
	print(TinyStatistician.median(a))
	print(TinyStatistician.median(b))
	print(TinyStatistician.median(nd))
	print(TinyStatistician.median(c))
	print(TinyStatistician.median(d))
	print(TinyStatistician.quartiles(a))
	print(TinyStatistician.quartiles(b))
	print(TinyStatistician.quartiles(nd))
	print(TinyStatistician.quartiles(c))
	print(TinyStatistician.quartiles(d))
	print(TinyStatistician.var(a))
	print(TinyStatistician.var(b))
	print(TinyStatistician.var(nd))
	print(TinyStatistician.var(c))
	print(TinyStatistician.var(d))
	print(TinyStatistician.std(a))
	print(TinyStatistician.std(b))
	print(TinyStatistician.std(nd))
	print(TinyStatistician.std(c))
	print(TinyStatistician.std(d))
