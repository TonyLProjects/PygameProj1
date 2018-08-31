import sys 
import os
import pygame

# import inputBuffer
import Keybindings as keybinds

from constants import *

# design:
# 		actions will come from: buffer, attack, directional imput


# TODO: implement input buffer -> make a key state manager object
# 		include filter function for p2
def handlePlayerInputs(events, pressInputs, playerGameSide, playerLocationSide):

	pressedKeys = filterPressInputs(pressInputs, playerGameSide)
	keyDownInputs = filterKeyDownInputs(events, playerGameSide)
	playerAction = processAttack(keyDownInputs, pressedKeys, playerLocationSide)

	if playerAction == "noAction":
		playerAction = processMovement(pressedKeys, playerLocationSide)


	return playerAction


def filterPressInputs(inputList, playerGameSide,):
	currentPressedKeys = []
	if playerGameSide == 1:	
		for p1Key in keybinds.validP1Keys:
			if inputList[p1Key]:			#if a valid p1 input is in the current list of inputs
				currentPressedKeys.append(keybinds.validP1Keys[p1Key])	#saves string instead of key value
	return currentPressedKeys

# keydown events usually return 1 single action, but could return multiple if multiple keys are pressed at the same time
def filterKeyDownInputs(events, playerGameSide):
	relevantKeyDowns = []
	for event in events:
		if event.type == pygame.KEYDOWN:
			for p1Key in keybinds.validP1Keys:
				if event.key == p1Key:
					relevantKeyDowns.append(keybinds.validP1Keys[p1Key])
	return relevantKeyDowns




# 	
def processAttack(keyDownInputs, pressedKeys, playerLocationSide):
	# if len(keyDownInputs) != 0:
	# 	print(keyDownInputs)

# add attack variety here
	if 	"punch" in keyDownInputs:
		if "left" in pressedKeys:
			return "punch"
		if "right" in pressedKeys:
			return "punch"
		return "punch"
	return "noAction"
	

# TODO: implement frame timer for charge attacks
# 		determine forward/backward and replace left/right
# takes in list of string commands, push them to buffer, and return final player action
def processMovement(pressedKeys, playerLocationSide):

	if "jump" in pressedKeys:
		if "right" in pressedKeys:
			return "forwardJump"
		if  "left" in pressedKeys:
			return "backwardJump"
		return "verticalJump"
	if "crouch" in pressedKeys:
		if "left" in pressedKeys:
			return "crouchBlock"
		return "crouch"
	if "right" in pressedKeys:
		return "forward"
	if "left" in pressedKeys:
		return "backward"
	return "noAction"






# tap input
# press input 
# 	left right, up donw
# 	priority order: up,  down, forward, back 
# if key is pressed for number of frames, enqueue hold event to event queue 
