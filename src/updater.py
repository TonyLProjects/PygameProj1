import sys
import os
import pygame
# might not be necessary to put these functions into a separate file


# checks a player's hitbox collided with hurtbox 
def hurtBoxCollisionDetection(player1, player2):
	pass


def update(player, action, hurtBoxCollisionResult):
		
	# if hurtBoxCollisionResult.playerHit == "p1Hit":
	# 	# init hitstun 
	# 	pass

	if isActionValid(player, action) != "noAction":
		player.initializeAction(action)
		player.tick()


# takes in player object and action string
# responsibility is to process validity of action. if valid, issue to updater
# TODO:
# 		include and generalize all attack inputs
def isActionValid(player, action):
	if action == "noAction":
		return "noAction"
	if player.canInitAction == False:
		return "noAction"
	if player.isAirborne == True:
		if action == "punch": # add/generalize more attack commands later
			return action
		else:
			return "noAction"
	return action
