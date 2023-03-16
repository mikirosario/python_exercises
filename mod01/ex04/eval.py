class Evaluator:
	validate = lambda word_lst, coef_lst: word_lst and coef_lst and isinstance(word_lst, list) and isinstance(coef_lst, list) and len(word_lst) == len(coef_lst) and all(isinstance(coef, float) and isinstance(word, str) for coef, word in zip(coef_lst, word_lst))
	@staticmethod
	def zip_evaluate(coefs: list, words: list):
		if not Evaluator.validate(words, coefs):
			return -1
		return sum([float(len(word)) * coef for word, coef in zip(words, coefs)])
	
	@staticmethod
	def enumerate_evaluate(coefs: list, words: list):
		if not Evaluator.validate(words, coefs):
			return -1
		coef_enum = enumerate(coefs)
		words_enum = enumerate(words)
		coef_enum.__next__
		i = 0
		# for coef in coef_enum:
		# 	coef * len(words_enum[i])
		# 	i += 1
		return sum([float(len(word)) * coef_enum.__next__()[1] for word in words])
