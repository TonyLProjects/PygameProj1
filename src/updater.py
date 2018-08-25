import sys
import os
import pygame

def update(playerObject, playerAction, hurtBoxCollisionResult):
		
		if isActionValid(playerObject, playerAction):
			initializeAction(playerObject, playerAction)
		updateFrameCounters(playerObject) # this might just be playerObj.tick()


# checks a player's hitbox collided with hurtbox 

def hurtBoxCollisionDetection(player1, player2):
