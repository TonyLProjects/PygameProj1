import sys
import os
import pygame
# might not be necessary to put these functions into a separate file
# maybe change the name of file to something else than updater


# checks a player's hitbox collided with hurtbox 
def hurtBoxCollisionDetection(player1, player2):
	if player1.isAttacking == False and player2.isAttacking == False:
		return "noHit"
	else:
		p1Hit = False
		p2Hit = False
		p1HitBox = player1.getHitBox()			# these should be vector2d objects
		# print(p1HitBox.max.x, p1HitBox.max.y)
		p1HurtBox = player1.getHurtBox()
		p2HitBox = player2.getHitBox()
		p2HurtBox = player2.getHurtBox()
		p2Hit = checkRectCollision(p1HitBox, p2HurtBox)
		p1Hit = checkRectCollision(p2HitBox, p1HurtBox)

		if p2Hit == True:
			print(p2Hit)
		if p1Hit == True:
			print(p1Hit)

# maybe this should be helper method in squareCord2d class
def checkRectCollision(coord1, coord2):
	if coord1.max.x < coord2.min.x:
		return False
	if coord1.min.x > coord2.max.x:
		return False
	if coord1.max.y < coord2.min.y:
		return False
	if coord1.min.y > coord2.max.y:
		return False
	return True

	

# TODO: restructure logic here
# function updates 1 player
# if player is hit, init hitstun and reset all other actions
# if player hit the other, refresh/update attack frame timer attack frame timer
# 		need cooldown timer for attacks

# if player takes no action, or if action is invalid, action is not initialized
def update(player, action, hurtBoxCollisionResult):
		
	# if hurtBoxCollisionResult.playerHit == "p1Hit":
	# 	# init hitstun 
	# 	pass
	# if hurtBoxCollisionResult.playerHit == "p2Hit":
	# 	pass

	if isActionValid(player, action) != "noAction":
		player.initializeAction(action)
	else:
		player.resetCrouch()
	player.tick() # always tick after all actions




# takes in player object and action string
# responsibility is to process validity of action. if valid, issue to updater
# TODO:
# 		include and generalize all attack inputs
# 		maybe add cannotInitAction to return value
def isActionValid(player, action):
	# print(action)
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