class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
	
	def transfer(self, amount):
		self.value += amount

class Bank:
	'''The Bank'''
	validator =	{
		'valid_attr_num': lambda attr_dict: len(attr_dict.keys()) % 2 != 0,
		'valid_attr_b': lambda attr_dict: not any(key[0] == 'b' for key in attr_dict.keys()),
		'valid_attr_zip_o_addr': lambda attr_dict: any(key.startswith("zip") or key.startswith("addr") for key in attr_dict.keys()),
		'valid_req_attrs': lambda attr_dict: "name" in attr_dict.keys() and "id" in attr_dict.keys() and "value" in attr_dict.keys(),
		'valid_name_attr': lambda attr_dict: isinstance(attr_dict["name"], str),
		'valid_id_attr': lambda attr_dict: isinstance(attr_dict["id"], int),
		'valid_value_attr': lambda attr_dict: not isinstance(attr_dict["value"], int) or isinstance(attr_dict["value"], float)
	}
	@staticmethod
	def is_corrupt_account(acct: Account):

		attrs = acct.__dict__
		# for test in Bank.validator:
		# 	print(Bank.validator[test](attrs))
		# print()
		if any(Bank.validator[test](attrs) == False for test in Bank.validator):
			return True
		return False

	def __init__(self):
		self.accounts = dict()
	
	def add(self, new_account: Account):
		""" Add new_account in the Bank
			@new_account: Account() new account to append
			@return True if success, False if an error occured
		"""
		result = False
		if isinstance(new_account, Account) and not new_account.name in self.accounts:
			try:
				self.accounts[new_account.name] = new_account
			except Exception as e:
				print(e)
			else:
				result = True
		return result

	def transfer(self, origin: str, dest: str, amount: float):
		if not isinstance(origin, str) or not isinstance(dest, str) or not origin in self.accounts or not dest in self.accounts:
			return False
		origin = self.accounts[origin]
		dest = self.accounts[dest]
		if Bank.is_corrupt_account(origin) or Bank.is_corrupt_account(dest) or amount < 0 or amount > origin.value:
			print("Cheque sin fondos")
			return False
		dest.transfer(amount)
		origin.value -= amount
	
	# def fix_account(self, name: str):
	# 	if (isinstance(name, str) and name in self.accounts):
	# 		corrupt_acct = self.accounts[name]


if __name__ == "__main__":
	acct = Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31')
	acct1 = Account(
		'Smith John',
        zip='911-745',
        value=1000.0,
        bref='1044618437ff2782f0bbece0abd05f31'
	)
	bank = Bank()
	bank.add(acct)
	bank.add(acct1)
	bank.transfer(acct, acct1, 500)
