# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Brooklyn D'Olympio>
# Creation Date: <7/24/2020>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	#print('''You are in a land full of dragons. In front of you,
	#you see two caves. In one cave, the dragon is friendly
	#and will share his treasure with you. The other dragon
	#is greedy and hungry, and will eat you on sight.''')
	print()

	print("You are in a land full of dragons. In front of you,"
              "you see two caves. In one cave, the dragon is friendly"
              "and will share his treasure with you. The other dragon"
              "is greedy and hungry, and will eat you on sight.")
	#Incorrect quotation marks at the beginning and the end of the message, as well as not wrapping the quotation for the entire message.
	#Also possible incorrect indentation

def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	#return caves

	return cave
#there was an 's' when it should have just been 'cave'

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	#time.sleep(3)
	time.sleep(2)
	#the instructions said '2 seconds' but the line has '3'
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#print 'Gobbles you down in one bite!'
                print("Gobbles you down in one bite!")
                #no parenthesis were used to enclose the message

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
        #Missing an equal sign on both statements to make it 'true'
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		#print("Thanks for planing")
                print("Thanks for playing!")
                #incorrect spelling

