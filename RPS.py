#Hank Warner, P1
#Rock, Paper Scissors game

# break int0 pieces
# Welcome screenm with name enterable thing
# Score Screen, computer wins, player wins, and ties
# gives options for r p s & q
# Game will loop until q is pressed
# Eack loop a random choice will be generated
# a choice from thge player, compare, and update score
# When game iis over, final score display
# WELCOME PAGE
# Name prompt
# Welcome msg


# Imports
import random
# Variables
playerSC = 0
computerSC = 0
ties = 0

# make a list
cChoice =["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name: ")

# main loop

while True:
	print("   Score: ")
	print("Computer: " + str(computerSC))
	print(name + ": " + str(playerSC))
	print("Ties:" + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to Quit")
	compChoice = random.choice(cChoice)
	print( "Computer picked: " + compChoice)
	if choice == "q":
		break

	if choice == "r":
		print( name +" Picked Rock")
		if compChoice == "r":
			print("Computer picked Rock, it is a tie")
			ties = ties + 1
		elif compChoice == "p":
			print("Computer picked Paper, Computer wins")
			computerSC = computerSC + 1
		else:
			print("Computer picked Scissors, " + name + " wins")
			playerSC = playerSC + 1

	elif choice == "p":
		if compChoice == "p":
			print("Computer picked Paper, it is a tie")
			ties = ties + 1
		elif compChoice == "s":
			print("Computer picked Scissors, Computer wins")
			computerSC = computerSC + 1
		else:
			print("Computer picked Rock, " + name + " wins")
			playerSC = playerSC + 1

	elif choice == "s":
		if compChoice == "s":
			print("Computer picked Scissors, it is a tie")
			ties = ties + 1
		elif compChoice == "r":
			print("Computer picked Rock, Computer wins")
			computerSC = computerSC + 1
		else:
			print("Computer picked Paper, " + name + " wins")
			playerSC = playerSC + 1
		
		

		




