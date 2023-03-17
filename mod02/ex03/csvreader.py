class CsvReader:
	class CorruptCSVException(Exception):
		pass
	def __init__(self, filename=None, sep=',', header=True, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
	
	def __enter__(self):
		try:
			self.file = open(self.filename, 'r')
			self.__validate_file()
		except Exception as e:
			print(e)
			return None
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		if 'file' in self.__dict__:
			self.file.close()
	
	def __validate_file(self):
		self.linec = 0
		self.val_num_per_line = 0
		file = self.file
		line = file.readline()
		for word in self.__get_next_word(line):
			if (word):
				self.val_num_per_line += 1
			self.linec += 1
		for line in file:
			val_num_in_line = 0
			for word in self.__get_next_word(line):
				if (word):
					val_num_in_line += 1
				#print(val_num_in_line)
			if val_num_in_line != self.val_num_per_line:
				raise CsvReader.CorruptCSVException("Varying number of registered values")
			self.linec += 1
		file.seek(0)

	def __get_next_word(self, line):
		word = str()
		for ch in line:
			if ch != self.sep:
				if ch != '\n' and not ch.isspace():
					word += ch
			else:
				yield word
				word = str()
		yield word

	def getdata(self):
		retlst = []
		retln = []
		linec = sum(1 for line in self.file)
		if (self.header):
			retlst = self.getheader()
		line_index = 0
		lower_bound = self.skip_top if self.skip_top <= linec else linec
		upper_bound = linec - self.skip_bottom if self.skip_bottom <= linec and self.skip_bottom <= linec - self.skip_top else linec
		for line in self.file:
			if (lower_bound <= line_index < upper_bound):
				for word in self.__get_next_word(line):
					retln.append(word)
				retlst.append(retln) #muy "pythónico" xD
				retln = []
			line_index += 1
		return retlst
		
	def getheader(self):
		retlst = []
		retln = []
		self.file.seek(0)
		line = self.file.readline()
		for word in self.__get_next_word(line):
			retln.append(word)
		retlst.append(retln)
		return retlst

if __name__ == "__main__":
	with CsvReader(filename='good.csv', skip_top=0) as file:
		if file == None:
			print("File is corrupted")
		else:
			data = file.getdata()
			for item in data:
				print(item)
