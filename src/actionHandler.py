# THIS FILE IS NOT NEEDED

import sys
import os
import pygame


# TODO: restructure logic here
# function updates 1 player
# if player is hit, init hitstun and reset all other actions
# if player hit the other, refresh/update attack frame timer attack frame timer
# 		need cooldown timer for attacks

# if player takes no action, or if action is invalid, action is not initialized
def handlePlayerAction(player, action, hurtBoxCollisionResult):
		
	# if hurtBoxCollisionResult.playerHit == "p1Hit":
	# 	# init hitstun 
	# 	pass
	# if hurtBoxCollisionResult.playerHit == "p2Hit":
	# 	pass

	if isActionValid(player, action) != "noAction":
		player.initializeAction(action)
	elif player.isCrouching:
		player.resetCrouch()
	player.tick() # always tick after all actions


# takes in player object and action string
# responsibility is to process validity of action. if valid, issue to updater
# TODO:
# 		include and generalize all attack inputs
# 		maybe add cannotInitAction to return value
def isActionValid(player, action):
	if player.canInitAction == False:
		return "noAction"
	if action == "noAction":
		return "noAction"
	if player.isAirborne == True:
		if action == "punch": # add/generalize more attack commands later
			return action
		else:
			return "noAction"
	return action