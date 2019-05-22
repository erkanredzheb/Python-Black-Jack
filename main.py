#!/usr/bin/env python3

import random, os, sys

cardName = { 1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King' }
cardSuit = { 'c': 'Clubs', 'h': 'Hearts', 's': 'Spades', 'd': 'Diamonds' }

class Card:

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return(cardName[self.rank]+" Of "+cardSuit[self.suit])

	def getRank(self):
		return(self.rank)

	def getSuit(self):
		return(self.suit)

	def BJValue(self):
		if self.rank > 9:
			return(10)
		else:
			return(self.rank)

def showHand(hand):
	for card in hand:
		print("|", card, "|")

def showCount(hand):
	print("Count: "+str(handCount(hand)))

def handCount(hand):
	handCount=0
	for card in hand:
		handCount += card.BJValue()
	return(handCount)

def gameEnd(score):
	print("Blackjack! *Final Score* Computer: "+str(score['computer'])+" You: "+str(score['human']))
	sys.exit(0)
	

deck	= []
suits = [ 'c','h','d','s' ]
score = { 'computer': 0, 'human': 0 }
hand	= { 'computer': [],'human': [] }
name = input("Hello! Please, enter your name: ")
balance = int(input("Enter the amount of credits you wish to deposit: "))
betEntered = False
balanceUpdated = False

for suit in suits:
	for rank in range(1,14):
		deck.append(Card(rank,suit))

keepPlaying = True

while keepPlaying:
	
	random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)
	
	#Deal Cards
	
	hand['human'].append(deck.pop(0))
	hand['computer'].append(deck.pop(0))
	
	hand['human'].append(deck.pop(0))
	hand['computer'].append(deck.pop(0))
	
	playHuman = True
	bustedHuman = False 
	

	while playHuman:
		os.system('clear')
		print("Dealer: "+str(score['computer'])+" "+ name + ":"+str(score['human']))
		
		if(balance < 1):
		    if(balanceUpdated == False):
		        print("Your balance is low! Please get some more chips and compe back!")
		        exit()
		else:
		    print("Your balance is", balance)
		
		if(betEntered == False):
		    bet = int(input("Please, enter your bet: "))
		    betEntered = True
		    balance = balance - bet
		    balanceUpdated = True
		
		
		print()
        

		print("Dealer's Hand: | "+ str(hand['computer'][-1]), "|")
		print()

		print('Your Hand:')

		showHand(hand['human'])

		showCount(hand['human'])

		print()
	
		inputCycle = True
		userInput = ''

		while inputCycle:
			userInput = input("(H)it, (S)tay, or (Q)uit: ").upper()
			if userInput == 'H' or 'S' or 'Q':
				inputCycle = False
		
		if userInput == 'H':
			hand['human'].append(deck.pop(0))
			if handCount(hand['human']) > 21:
				playHuman = False
				bustedHuman = True
		elif userInput == 'S':
			playHuman = False
		else:
			gameEnd(score)

	playComputer = True
	bustedComputer = False

	while not bustedHuman and playComputer:
		print(handCount(hand['computer']))
		if handCount(hand['computer'])<17:
			hand['computer'].append(deck.pop(0))
		else:
			playComputer = False

		if handCount(hand['computer'])>21:
			playComputer = False
			bustedComputer = True

	if bustedHuman:
		print(name, 'Too Many!')
		score['computer'] += 1
	elif bustedComputer:
		print('Dealer Too Many!')
		score['human'] += 1
		balance = balance + 2 * bet
	elif handCount(hand['human']) > handCount(hand['computer']):
		print(name, 'Wins')
		score['human'] += 1
		balance = balance + 2 * bet
	else:
		print('Dealer Wins')
		score['computer'] += 1
	
	print()
	print("Dealer's Hand:")
	showHand(hand['computer'])
	showCount(hand['computer'])

	print()
	print('Your Hand:')
	showHand(hand['human'])
	showCount(hand['human'])
	print()
	betEntered = False
	balanceUpdated = False
	if input("(Q)uit or enter for next round").upper() == 'Q':
		gameEnd(score)

	deck.extend(hand['computer'])
	deck.extend(hand['human'])

	del hand['computer'][:]
	del hand['human'][:]
