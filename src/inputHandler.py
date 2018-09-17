import sys 
import os
import pygame

# import inputBuffer
import Keybindings as keybinds

from constants import *

# design:
# 		actions will come from: buffer, attack, directional imput


def insertToBuffer(pressedKeys, inputBuffer):
	if len(pressedKeys) == 0:
		inputBuffer.previousInput = ""
		return

	if len(pressedKeys) == 1:
		if pressedKeys[0] == "crouch":
			inputBuffer.enqueue("down")
			return
		if pressedKeys[0] == "jump":
			inputBuffer.enqueue("jump")
			return
		inputBuffer.enqueue(pressedKeys[0])
		return
	if "forward" in pressedKeys:
		if "crouch" in pressedKeys:
			inputBuffer.enqueue("forwardDown")
			return
		if "jump" in pressedKeys:
			inputBuffer.enqueue("forwardUp")
			return
	if "backward" in pressedKeys:
		if "crouch" in pressedKeys:
			inputBuffer.enqueue("backwardDown")
			return
		if "jump" in pressedKeys:
			inputBuffer.enqueue("backwardUp")
			return

# TODO: 
#	implement input buffer
#	buffer clear clock
#	REFACTOR 

def handlePlayerInputs(events, pressInputs, player, inputBuffer):

	pressedKeys = filterPressInputs(pressInputs, player.playerGameSide, player.playerFacingSide)
	insertToBuffer(pressedKeys, inputBuffer)
	# inputBuffer.printBuffer()
	playerAction = inputBuffer.detectSpecialMove()
	if playerAction != "noAction" and playerAction != None:
		return playerAction

	keyDownInputs = filterKeyDownInputs(events, player.playerGameSide, player.playerFacingSide)

	playerAction = processAttack(keyDownInputs, pressedKeys, player.playerFacingSide)

	if playerAction == "noAction":
		playerAction = processMovement(pressedKeys, player.playerFacingSide)


	return playerAction


def filterPressInputs(inputList, playerGameSide, playerFacingSide):
	currentPressedInput = []
	if playerGameSide == 1:	
		for p1Key in keybinds.validP1Keys:
			if inputList[p1Key]:			#if a valid p1 input is in the current list of inputs
				if keybinds.validP1Keys[p1Key] == "left" or keybinds.validP1Keys[p1Key] == "right":
					inputToInsert = convertInputDirectionToPlayerDirection(playerFacingSide, keybinds.validP1Keys[p1Key])
					currentPressedInput.append(inputToInsert)
				else:
					currentPressedInput.append(keybinds.validP1Keys[p1Key])	#saves string instead of key value
	else:
		for p2Key in keybinds.validP2Keys:
			if inputList[p2Key]:
				if keybinds.validP2Keys[p2Key] == "left" or keybinds.validP2Keys[p2Key] == "right":
					inputToInsert = convertInputDirectionToPlayerDirection(playerFacingSide, keybinds.validP2Keys[p2Key])
					currentPressedInput.append(inputToInsert)
				else:
					currentPressedInput.append(keybinds.validP2Keys[p2Key])

	return currentPressedInput

# keydown events usually return 1 single action, but could return multiple if multiple keys are pressed at the same time

# logic: if the event is a keydown event and the key is in the valid keybindings, append.
# not sure if possible to remove nested loop/statements
def filterKeyDownInputs(events, playerGameSide, playerFacingSide):
	relevantKeyDownInputs = []
	for event in events:
		if event.type == pygame.KEYDOWN:

			# key filter for p1
			if playerGameSide == 1:
				for p1Key in keybinds.validP1Keys:
					if event.key == p1Key:
						if keybinds.validP1Keys[p1Key] == "left" or keybinds.validP1Keys[p1Key] == "right":
							inputToInsert = convertInputDirectionToPlayerDirection(playerFacingSide, keybinds.validP1Keys[p1Key])
							relevantKeyDownInputs.append(inputToInsert)
						else:
							relevantKeyDownInputs.append(keybinds.validP1Keys[p1Key])
			# key filter for p2
			else:
				for p2Key in keybinds.validP2Keys:
					if event.key == p2Key:
						if keybinds.validP2Keys[p2Key] == "left" or keybinds.validP2Keys[p2Key] == "right":
							inputToInsert = convertInputDirectionToPlayerDirection(playerFacingSide, keybinds.validP2Keys[p2Key])
							relevantKeyDownInputs.append(inputToInsert)
						else:
							relevantKeyDownInputs.append(keybinds.validP2Keys[p2Key])
	return relevantKeyDownInputs




def processAttack(keyDownInputs, pressedKeys, playerFacingSide):


# add attack variety here
	if 	"punch" in keyDownInputs:
		if "left" in pressedKeys:
			return "punch"		# supposed to be forward and backward punch(direction modified punch)
		if "right" in pressedKeys:
			return "punch"
		return "punch"
	return "noAction"
	

# TODO: implement frame timer for charge attacks
# 		determine forward/backward and replace left/right
# takes in list of string commands, push them to buffer, and return final player action
def processMovement(pressedKeys, playerFacingSide):

	if "jump" in pressedKeys:
		if "forward" in pressedKeys:
			return "forwardJump"
		if  "backward" in pressedKeys:
			return "backwardJump"
		return "verticalJump"
	if "crouch" in pressedKeys:
		if "backward" in pressedKeys:
			return "crouchBlock"
		return "crouch"
	if "forward" in pressedKeys:
		return "forward"
	if "backward" in pressedKeys:
		return "backward"
	return "noAction"


# helper functions

# return string of either "forward" or "backward" depending on inputDirection and playerFacingSide
def convertInputDirectionToPlayerDirection(playerFacingSide, inputDirection):
	# Player facing right
	if playerFacingSide == 0:
		if inputDirection == "right":
			return "forward"
		else:
			return "backward"
	if playerFacingSide == 1:
		if inputDirection == "right":
			return "backward"
		else:
			return "forward"
