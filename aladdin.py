import sys
import os
import Tkinter as tk

def display_environment():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("| ------------------------------------- |")
	print("|        ALADDIN: adventure game        |")
	print("|                                       |")
	print("|                                       |")
	print("|                                       |")
	print("|         PRESS ENTER TO START          |")
	print("|                                       |")
	print("|                                       |")
	print("|                                       |")
	print("| ------------------------------------- |")

def keypress(event):
	if event.keysym == "Escape":
		root.destory()
	x = event.char
	if x == "w":
		print "UP"

def main():
	root = tk.Tk()
	root.bind_all("<Key>", keypress)
	root.withdraw()
	root.mailloop()

	# Display welcome screen
	# display_environment()
	# raw_input()




if __name__ == "__main__":
    main()