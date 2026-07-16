#tmp outline incase I need to do multiple things per chapter to keep it in one file

def funcOne():
	print("one")

def funcTwo():
	print("two")

#Build dictionary
options = {
	1: funcOne,
	2: funcTwo,
}

whichOne = int(input("What one to run?"))

#run the one selected
options[whichOne]()

#Doing stuff like this instead of multiple files, I have written too much go man
