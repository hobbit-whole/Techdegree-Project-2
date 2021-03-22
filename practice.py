import random
def user_guess():
	while True:
	
		try:
			guess = int(input("Please pick a number between 1 and 10.  "))
		except ValueError:
			print("Please enter an integer not letters.")
		else:
			return guess
def start_game():
	print("*****Welcome to the Numbers Guessing Game!*****")
	solution = random.randint(1,10)
	guess = 0
	attempts = 0
	
	while guess != solution:
		attempts += 1
		
		guess = user_guess()
		
		if guess < solution:
			print("Try guessing higher")
		elif guess > solution:
			print("Try guessing lower")
	print("You got it! It only took you {} attempts! Thanks for playing!".format(attempts))		
start_game()