import sys
import os
import random

PLAYING = 0
FAIL = 1
SUCCESS = 2
state = PLAYING
repeat = False
guessed_letters = []
myCount = 8

#TODO: get words dynamically from online repo
dictionary = [
	"lemon",
	"pirate",
	"planet",
	"company",
	"woman",
	"purple",
	"wild",
	"territory",
	"winner",
	"animal",
	"human",
	"house",
	"telephone",
	"table"]

def display_man(remaining_count):
	print("   ______")
	print("    |  \|")
	if remaining_count is 0:
		print("    ()  |")
		print("   /||\ |")
		print("    /\  |")
	if remaining_count is 1:
		print("    ()  |")
		print("   /||\ |")
		print("     \  |")
	if remaining_count is 2:
		print("    ()  |")
		print("   /||\ |")
		print("        |")
	if remaining_count is 3:
		print("    ()  |")
		print("    ||\ |")
		print("        |")
	if remaining_count is 4:
		print("    ()  |")
		print("    ||  |")
		print("        |")
	if remaining_count is 5:
		print("    ()  |")
		print("     |  |")
		print("        |")
	if remaining_count is 6:
		print("    ()  |")
		print("        |")
		print("        |")
	if remaining_count is 7:
		print("    (   |")
		print("        |")
		print("        |")
	if remaining_count is 8:
		print("        |")
		print("        |")
		print("        |")
	print("        |")
	print("[--------]")

def isInList(letter):
	count = 0
	while count < len(guessed_letters):
		if letter is guessed_letters[count]:
			return True
		count = count + 1
	return False

def isNotInWord(letter):
	count = 0
	while count < len(dictionary[0]):
		if letter is dictionary[0][count]:
			return False
		count = count + 1
	return True

def display_word(word):
	global state
	count = 0
	finish = True
	while count < len(word):
		if isInList(word[count]):
			sys.stdout.write(word[count] + " ")
		else:
			finish = False
			sys.stdout.write("- ")
		count = count + 1
	if finish is True:
		state = SUCCESS
	print("\n")

def display_message(state):
	global myCount
	global repeat
	if state is PLAYING:
		var = raw_input("Please guess a letter: ")
		if isInList(var):
			repeat = True
		else:
			if isNotInWord(var):
				myCount = myCount - 1
			guessed_letters.append(var)
	if state is FAIL:
		print("DEAD MEAT!")
	if state is SUCCESS:
		print("Whew! Another life saved!")

def handle_repeat():
	global repeat
	if repeat is True:
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		print("You already guessed that letter.")
		repeat = False
	else:
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def main():

	#TODO make welcome screen to set difficulty level
	global myCount
	repeat = False
	random.shuffle(dictionary)
	print(dictionary[0])

	while state is PLAYING:

		handle_repeat()

		# welcome screen
		display_man(myCount)
		display_word(dictionary[0])

		# user interaction screen
		display_message(state)

	print(str(myCount) + " guesses remaining.")

if __name__ == "__main__":
    main()