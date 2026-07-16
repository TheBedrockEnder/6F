#tmp outline incase I need to do multiple things per chapter to keep it in one file
import tkinter as tk #CBA to deal with warnings from langserver when importing all

#Write a program to place a button saynig "Click here" in a window, when clicked hi there appears underneath. named "placing a button"

def funcOne():
	root = tk.Tk()
	def hiThere():
		tk.Label(root, text = "hi there").pack()
	root.title("Placing a button.")
	button = tk.Button(root, text = "Click here!", command=hiThere)
	button.pack()
	root.mainloop()


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
