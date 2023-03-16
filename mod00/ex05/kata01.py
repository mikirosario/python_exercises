kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if __name__ == "__main__":
	keys = kata.keys()
	for key in keys:
		print(f'{key} was created by {kata.get(key)}')