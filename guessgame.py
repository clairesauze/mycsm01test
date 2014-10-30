import sys

secret = 100
guess = "null"


while(guess != secret):
	print("Guess the number...")
	guess = int(sys.stdin.readline().strip())
	if(guess < secret):
		print("too low, guess again")
		guess = int(sys.stdin.readline().strip())
	elif(guess > secret):
		print("too high")
		guess = int(sys.stdin.readline().strip())
	elif(guess == secret):
		print("well done")