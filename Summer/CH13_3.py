#it says programm not app so assuming I can just make cli (again)

accepted = False
username = ""
password = ""

while accepted == False:
	username = input("Enter your username")
	password = input("Enter your password")
	if len(password) > 6:
		accepted = True
	else:
		print("Password must be at least 6 characters")
