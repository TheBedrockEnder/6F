#it says programm not app so assuming I can just make cli
input = input("Enter username to search: ").strip()

with open("saveFile", "r") as file:
	for line in file:
			parts = line.strip().split(" ")
			if len(parts) >= 3 and parts[0] == input:
				print("username:   {parts[0]}")
				print("first name: {parts[1]}")
				print("surname:    {parts[2]}")
				break

#would probably be a lot better and cleaner to use a database but I seriously can not be asked, if it's stupid and it works, it's not stupid
