import enum

class Vector:
	class VectorType(enum.Enum):
		COLUMN = 0
		ROW = 1

	validate_list = lambda values: values is not None and isinstance(values, list)
	def __init__(self, values: list):
		validate_column_element = lambda values: all(len(value) == 1 and isinstance(value[0], float) for value in values)
		validate_row_element = lambda values: len(values) == 1 and all(isinstance(num, float) for num in values[0])
		if (not Vector.validate_list(values)):
			raise Exception("What the hell was that?")
		elif (validate_row_element(values)):
			self.type = Vector.VectorType.ROW
			self.shape = {1, len(values[0])}
		elif (validate_column_element(values)):
			self.type = Vector.VectorType.COLUMN
			self.shape = {len(values), 1}
		else:
			raise Exception("Not a row or column")
		self.vec = values
	
	@staticmethod
	def vector_from_list(values: list, type: "Vector.VectorType"):
		validate_series = lambda values: len(values) > 0 and all(isinstance(num, float) for num in values)
		if not Vector.validate_list(values) or not validate_series(values) or not isinstance(type, Vector.VectorType):
			raise Exception("What the hell was that?")
		if type == Vector.VectorType.ROW:
			newvec = [values]
		else:
			newvec = [[val] for val in values]
		return Vector(newvec)
	
	def __validate_vector_operation(self, other: "Vector"):
		if (other is None or not isinstance(other, Vector)):
			print("Argument is not a vector")
		elif (self.shape != other.shape):
			print("The vectors are not the same shape.")
		else:
			return True
		return False

	def get_values(self):
		retlst = list()
		if (self.type == Vector.VectorType.COLUMN):
			for lst in self.vec:
				retlst.append(lst[0])
		else:
			for val in self.vec[0]:
				retlst.append(val)
		return retlst

	def T(self):
		if (self.type == Vector.VectorType.COLUMN):
			return Vector([self.get_values()])
		else:
			vals = self.get_values()
			ret = []
			for val in vals:
				ret.append([val])
			return Vector(ret)
		
	def dot(self, other: "Vector"):
		if not self.__validate_vector_operation(other):
			return None
		myvec = self.get_values()
		othervec = other.get_values()
		product = 0
		for myval, otherval in zip(myvec, othervec):
			product += myval * otherval
		return product
	
	def __add__(self, other: "Vector"): 
		if not self.__validate_vector_operation(other):
			return None
		myvec = self.get_values()
		othervec = other.get_values()
		results = [myval + otherval for myval, otherval in zip(myvec, othervec)]
		return Vector.vector_from_list(results, self.type)
	
	def __sub__(self, other: "Vector"):
		if not self.__validate_vector_operation(other):
			return None
		myvec = self.get_values()
		othervec = other.get_values()
		results = [myval - otherval for myval, otherval in zip(myvec, othervec)]
		return Vector.vector_from_list(results, self.type)
	
	def __mul__(self, rvalue):
		if not isinstance(rvalue, float) and not isinstance(rvalue, int):
			if isinstance(rvalue, Vector):
				raise NotImplementedError("We don't do that here")
			else:
				print("That is not a number")
			return None
		scalar = float(rvalue)
		myvec = self.get_values()
		results = [myval * scalar for myval in myvec]
		return Vector.vector_from_list(results, self.type)

	def __rmul__(self, lvalue):
		if not isinstance(lvalue, float) and not isinstance(lvalue, int):
			print("That is not a number")
			return None
		scalar = float(lvalue)
		myvec = self.get_values()
		results = [scalar * myval for myval in myvec]
		return Vector.vector_from_list(results, self.type)

	def __truediv__(self, rvalue):
		if not isinstance(rvalue, float) and not isinstance(rvalue, int):
			print("That is not a number")
			return None
		if rvalue == 0:
			print("Division by zero is undefined")
			return None
		scalar = float(rvalue)
		myvec = self.get_values()
		results = [myval / scalar for myval in myvec]
		return Vector.vector_from_list(results, self.type)

	def __rtruediv__(self, lvalue):
		raise NotImplementedError("Division of a scalar by a Vector is not defined here.")
