#!/usr/bin/python 
import random 

def decide(player_pick,computer_pick):
	print 'You picked %s ' %player_pick
	print 'Computer picked %s' %computer_pick
        if player_pick == computer_pick:
                print "It's a tie"
		return 2
        elif player_pick == 'Rock': 
		if computer_pick == 'Scissors':
                	print 'You win!'
			return 1
		else:
			print 'You lose'
			return 0 
        elif player_pick == 'Paper':
		if computer_pick == 'Rock':
                	print 'You win'
			return 1
		else:
			print 'You lose'
			return 0 
        elif player_pick == 'Scissors':
                if computer_pick == 'Paper':
			print 'You win!'
			return 1
		else:
			print 'You lose'
			return 0  

player_score  = 0
computer_score = 0 
picks = ['Rock', 'Paper', 'Scissors']
while True:
	player = raw_input("Pick Rock, Paper, or scissors..., or Score for score, or  Enough to exit\n")
	computer = random.choice(picks)
	if player not in picks:
		if player == 'Score':
			print("The score is You - Computer %s - %s" %(player_score,computer_score))
		if player == 'Enough':
			exit()
		else:
			print 'Pick one of the above...'
	else:
		d = int(decide(player, computer))
		if d == 0:
			computer_score += 1
		elif d == 1:
			player_score += 1
		elif d == 2:
			player_score += 1
			computer_score += 1
exit()
