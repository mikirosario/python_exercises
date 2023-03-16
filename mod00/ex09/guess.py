import random

def welcome_msg():
	print("This is an interactive guessing game!\n"
			"You have to enter a number between 1 and 99 to find out the secret number.\n"
			"Type 'exit'to end the game.\n"
			"Good luck!\n")

def victory(guess: int, tries: int):
	if(guess == 42):
		print("42, the answer to the ultimate question. All your evaluation points are belong to us! Make your time!")
	if(tries == 1):
		print("Congratulations! You got it on your first try! You are a super player!")
	else:
		print("Congratulations, you've got it!\n"
		f"You won in {tries} attempts")
	exit(0)

def main():
	num = random.randint(1, 99)
	check_guess = lambda guess: num - guess
	welcome_msg()
	tries = 0
	while (True):
		tries += 1
		print("Guess a number between 1 and 99.")
		reply = input()
		if (reply.casefold() == str("exit").casefold()):
			print("Goodbye!")
			exit(0)
		elif (not reply.isdigit()):
			print("That is not a valid number. Try again.")
		else:
			guess = int(reply)
			result = check_guess(guess)
			if result == 0:
				victory(guess, tries)
			elif result < 0:
				print("Too high!")
			else:
				print("Too low!")

if __name__ == "__main__":
	main()
	