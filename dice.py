import sys
import os
import random

def show_die(number):
	if number is 1:
		print(" ------- ")
		print("|       |")
		print("|   .   |")
		print("|       |")
		print(" ------- ")	
	if number is 2:
		print(" ------- ")
		print("|     . |")
		print("|       |")
		print("| .     |")
		print(" ------- ")	
	if number is 3:
		print(" ------- ")
		print("|     . |")
		print("|   .   |")
		print("| .     |")
		print(" ------- ")	
	if number is 4:
		print(" ------- ")
		print("| .   . |")
		print("|       |")
		print("| .   . |")
		print(" ------- ")	
	if number is 5:
		print(" ------- ")
		print("| .   . |")
		print("|   .   |")
		print("| .   . |")
		print(" ------- ")	
	if number is 6:
		print(" ------- ")
		print("| .   . |")
		print("| .   . |")
		print("| .   . |")
		print(" ------- ")

def roll():
	items = [1,2,3,4,5,6]
	random.shuffle(items)
	result = items[0]

	show_die(result)

	return result

def main():
	items = [1,2,3,4,5,6]
	random.shuffle(items)

	show_die(items[0])
	

if __name__ == "__main__":
	main()