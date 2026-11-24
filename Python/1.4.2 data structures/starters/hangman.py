# thought I could do this in 5 mins, I was wrong.

wordinput = input("How long is the word?")
wordarry = []
for i in range(len(wordinput)):
	wordarry.append(wordinput[i-1])

guessedLetters = []
numberofguessesleft = 6
def guess(guess):
	usrguess = input("what do you guess?")
	if usrguess in guessedLetters:
		print("stop tying to break it")
	elif usrguess in wordarry:
		print("You got one!")
