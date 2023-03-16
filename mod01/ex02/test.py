
from vector import Vector
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

except_err = lambda test_num: print(f"{bcolors.FAIL}Test {test_num} threw but shouldn't have{bcolors.ENDC}") is not None
else_err = lambda test_num: print(f"{bcolors.FAIL}Test {test_num} didn't throw but should have{bcolors.ENDC}") is not None
success = lambda test_num: print(f"{bcolors.OKGREEN}Test {test_num} successful{bcolors.ENDC}")
print_result = lambda test_result_bool: print(f"{bcolors.OKGREEN}OK{bcolors.ENDC}") if test_result_bool == True else print(f"{bcolors.FAIL}KO{bcolors.ENDC}")
result = lambda test_result_bool: f"{bcolors.OKCYAN}OK{bcolors.ENDC}" if test_result_bool == True else f"{bcolors.FAIL}KO{bcolors.ENDC}"
expects = lambda val, expected_val: val == expected_val
def test_vec_validation():
	ret = True
	try:
		print("Test 1: Accept Valid Row")
		vector1 = Vector([[2., 1.]])
	except Exception as e:
		print(e)
		ret = except_err(1)
	else:
		success(1)
	try:
		print("Test 2: Accept Valid Column")
		vector2 = Vector([[1.], [2.]])
	except Exception as e:
		print(e)
		ret = except_err(1)
	else:
		success(2)
	try:
		print("Test 3: Accept Valid Single Point")
		vector3 = Vector([[1.]])
	except Exception as e:
		print(e)
		ret = except_err(3)
	else:
		success(3)
	try:
		print("Test 4: Reject Bad Value")
		vector4 = Vector([[2.], [1., 2.]])
	except Exception as e:
		print(e)
		success(4)
	else:
		print(vector4.type)
		ret = else_err(4)
	try:
		print("Test 5: Reject Bad Value")
		vector5 = Vector([[2., 1., 2.], [1.]])
	except Exception as e:
		print(e)
		success(5)
	else:
		print(vector5.type)
		ret = else_err(5)
	print(f"Validation Check Result: {result(ret)}")
	return ret
	
def test_vec_operations():
	ret = True
	print("Test 6: Identify Valid Row Shape")
	vector6 = Vector([[2., 1.]])
	ret = expects(vector6.shape, {1, 2})
	print(vector6.type)
	print(vector6.shape)
	print_result(ret)
	print("Test 7: Identify Valid Column Shape")
	vector7 = Vector([[1.], [2.], [3.]])
	ret = expects(vector7.shape, {3, 1})
	print(vector7.type)
	print(vector7.shape)
	print_result(ret)
	print("Test 8: Get Column Values as List")
	vector8 = Vector([[1.], [2.], [3.]])
	ret = expects(vector8.get_values(), [1, 2, 3])
	print_result(ret)
	print("Test 9: Get Row as List")
	vector9 = Vector([[2., 1., 8., 6.]])
	ret = expects(vector9.get_values(), [2, 1, 8, 6])
	print_result(ret)
	print("Test 10: Column Inversion")
	vector10 = Vector([[1.], [2.], [3.]])
	ret = expects(vector10.T().vec, [[1., 2., 3.]])
	print(vector10.T().vec)
	print_result(ret)
	print("Test 11: Row Inversion")
	vector11 = Vector([[2., 1., 8., 6.]])
	ret = expects(vector11.T().vec, [[2.], [1.], [8.], [6.]])
	print(vector11.T().vec)
	print_result(ret)
	print("Test 12: Dot Product")
	vector12a = Vector([[2.], [7.], [1.]])
	vector12b = Vector([[8., 2., 8.]])
	ret = expects(vector12a.dot(vector12b), 38)
	print(vector12a.dot(vector12b))
	print_result(ret)
	print("Test 13: Dot with Bad Argument")
	vector13a = Vector([[2.], [7.], [1.], [9.]])
	vector13b = Vector([[8., 2., 8.]])
	ret = expects(vector13a.dot(vector13b), None)
	print_result(ret)
	print("Test 14: Dot with Null Argument")
	vector14 = Vector([[2.], [7.], [1.], [9.]])
	ret = expects(vector14.dot(None), None)
	print_result(ret)
	print("Test 15: Dot with Non-Vector Argument")
	vector15 = Vector([[2.], [7.], [1.], [9.]])
	ret = expects(vector15.dot(42), None)
	print_result(ret)
	print("Test 16: Vector Addition")
	vector16a = Vector([[2., 4.]])
	vector16b = Vector([[1., 5.]])
	ret = expects((vector16a + vector16b).vec, Vector([[3., 9.]]).vec)
	print_result(ret)
	print("Test 17: Vector Subtraction")
	vector17a = Vector([[9., 2., 16., 1., -7.]])
	vector17b = Vector([[-9., 17., 42., -42., -3.]])
	ret = expects((vector17a - vector17b).vec, Vector([[18., -15., -26., 43., -4.]]).vec)
	print((vector17a - vector17b).vec)
	print_result(ret)
	print("Test 18: Vector Multiplication by Scalar")
	vector18 = Vector([[2., 3., 1.]])
	ret = expects((vector18 * 2).vec, Vector([[4., 6., 2.]]).vec)
	print_result(ret)
	print("Test 19: Scalar Multiplication by Vector (RValue)")
	vector19 = Vector([[2., 3., 1.]])
	ret = expects((2 * vector19).vec, Vector([[4., 6., 2.]]).vec)
	print_result(ret)
	print("Test 20: Vector Division by Scalar")
	vector20 = Vector([[8., 6., 7.]])
	ret = expects((vector20 / 2).vec, Vector([[4., 3., 3.5]]).vec)
	print_result(ret)
	print("Test 21: Vector Division by Zero")
	vector21 = Vector([[8., 6., 7.]])
	ret = expects((vector21 / 0), None)
	print_result(ret)
	print("Test 22: Scalar Division by Vector (RValue)")
	try:
		vector22 = Vector([[8., 6., 7.]])
		2 / vector22
	except Exception as e:
		print(e)
		success(22)
	else:
		ret = else_err(22)
	print(f"Operations Check Result: {result(ret)}")
	return ret


def main():
	test_vec_validation() and test_vec_operations()

if __name__ == "__main__":
	main()
