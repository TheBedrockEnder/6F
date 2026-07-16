#tmp outline incase I need to do multiple things per chapter to keep it in one file
import tkinter as tk #CBA to deal with warnings from langserver when importing all

def funcOne():
	root = tk.Tk()
	def hiThere():
		tk.Label(root, text = "hi there").pack()
	root.title("Placing a button.")
	button = tk.Button(root, text = "Click here!", command=hiThere)
	button.pack()
	root.mainloop()

def funcTwoA():
	root = tk.Tk()
	root.geometry("200x120")
	root.configure(background="Light green")
	def Left():
		label.config (text = "Left")
	def Right():
		label.config (text = "Right")
	label = tk.Label(root, text = "press one")
	label.grid(row = 0, column = 0, columnspan=2, padx=20, pady=20)
	buttonleft = tk.Button(root, text = "Left", command=Left)
	buttonleft.grid(row = 1, column=0, padx=20)
	buttonright = tk.Button(root, text = "Right", command=Right)
	buttonright.grid(row=1, column=1, padx=20)
	root.mainloop()

def funcTwoB():
	# Just schoolwor- WAIT YOKO TARO?!
	root = tk.Tk()
	root.geometry("200x120")
	root.configure(background="Light green")
	def Left():
		label.config (text = "Left")
		label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="w")
	def Right():
		label.config (text = "Right")
		label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="e")
	label = tk.Label(root, text = "press one")
	label.grid(row = 0, column = 0, columnspan=2, padx=20, pady=20)
	buttonleft = tk.Button(root, text = "Left", command=Left)
	buttonleft.grid(row = 1, column=0, padx=20)
	buttonright = tk.Button(root, text = "Right", command=Right)
	buttonright.grid(row=1, column=1, padx=20)
	root.mainloop()


#Build dictionary
options = {
	1: funcOne,
	2: funcTwoA,
	3: funcTwoB,
}

whichOne = int(input("What one to run?"))

#run the one selected
options[whichOne]()

#Doing stuff like this instead of multiple files, I have written too much go man
