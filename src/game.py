import sys
import os
import pygame

dirPath = os.path.dirname(os.path.realpath(__file__))	# not sure if this is the proper way to import
sys.path.append(dirPath + '/inputBuffer')

import inputHandler
import player
# importing keybinding dictionary
import Keybindings as keybinds

# importing helper structures
from vector2d import vector2d
from hitResult import hitResult
from playerAction import playerAction

from inputBuffer import inputBuffer


from constants import *

def playerSideSwitchDetection(player1, player2):
	if player1.xPos > player2.xPos and player1.playerFacingSide == 0:
			return True
			# request side switch
	if player1.xPos < player2.xPos and player1.playerFacingSide == 1:
			return True
			# request side switch
	return False

# TODO: move this to squareCoord2d.py and call from that file
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

# TODO: check if using object as struct is efficient
def hurtBoxCollisionDetection(player1, player2):
	if player1.isAttacking == False and player2.isAttacking == False:
		return hitResult(False, False, player1.attackType, player2.attackType)
	else:
		p1Hit = False
		p2Hit = False
		p1HitBox = player1.getHitBox()			
		p1HurtBox = player1.getHurtBox()
		p2HitBox = player2.getHitBox()
		p2HurtBox = player2.getHurtBox()
		p2Hit = checkRectCollision(p1HitBox, p2HurtBox)
		p1Hit = checkRectCollision(p2HitBox, p1HurtBox)
		moveThatHitP1 = player2.attackType
		moveThatHitP2 = player1.attackType
	return hitResult(p1Hit, p2Hit, moveThatHitP1, moveThatHitP2)

# does not need to account for multiple hit by the same move since hitbox will disapear when hit lands
def handlePlayerAction(player, action, hitResult):
	if player.playerGameSide == 1 and hitResult.p1HitResult == True:
		return playerAction("hitstun", hitResult.moveThatHitP1)
	if player.playerGameSide == 1 and hitResult.p2HitResult == True:
		return playerAction("landedHit", hitResult.moveThatHitP2)
	if player.playerGameSide == 2 and hitResult.p2HitResult == True:
		return playerAction("hitstun", hitResult.moveThatHitP2)
	if player.playerGameSide == 2 and hitResult.p1HitResult == True:
		return playerAction("landedHit", hitResult.moveThatHitP1)
	if isActionValid(player, action) != "noAction":
		return playerAction(action, "NULL")
	return playerAction("noAction", "NULL")

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

# parameter "action" is an array witFh [0] containing string of move type and [1] containing move hit/landed. 
# [1] contains "null" if no hit landed
def initFinalAction(player, action):
	if action.moveType != "noAction":
		player.initializeAction(action)
	elif player.isCrouching: 
		player.resetCrouch()


# temporary rendering functions
# TODO: 
# 	Load background and sprite
def renderDisplay(display):
	gameDisplay.fill(WHITE)	

def renderPlayer(player, display):
		drawPlayerBody(player, display)
		drawPlayerAttack(player, display)

def drawPlayerBody(player, display):
	if player.playerGameSide == 1:
		playerColor = BLACK
		if player.isHitStunned:
			playerColor = GREEN
		pygame.draw.rect(display, playerColor, [player.xPos, player.yPos, player.width, player.height])
	else:
		playerColor = RED
		if player.isHitStunned:
			playerColor = GREEN
		pygame.draw.rect(display, playerColor, [player.xPos, player.yPos, player.width, player.height])


def drawPlayerAttack(player, display):
	if player.isAttacking == True:
		coord = player.getHitBox()
		hitboxHeight = coord.max.y - coord.min.y

		hitboxWidth = coord.max.x - coord.min.x

		pygame.draw.rect(display, BLUE, [coord.min.x, coord.min.y, hitboxWidth, hitboxHeight])




clock = pygame.time.Clock()
pygame.init()

#set display surface, only 1 is allowed by SDL
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Street fighter II clone")
gameExit = False

#initialize players and other modules
p1 = player.Player("default class", 1)
p2 = player.Player("default class", 2)
p1InputBuffer = inputBuffer(INPUT_BUFFER_SIZE)
p2InputBuffer = inputBuffer(INPUT_BUFFER_SIZE)




while not gameExit:

	currentPressedKeys = []
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			gameExit = True
	# action events handled with KEYDOWN events


	# movement handled with pressed keys 
	keys = pygame.key.get_pressed()

	if p1.sideSwitchRequest == False and p2.sideSwitchRequest == False:
		playerSideSwitchResult = playerSideSwitchDetection(p1, p2)
	if playerSideSwitchResult == True:
		p1.initSideSwitch()
		p2.initSideSwitch()
		playerSideSwitchResult = False
	p1ActionFromInput = inputHandler.handlePlayerInputs(events, keys, p1, p1InputBuffer)
	p2ActionFromInput = inputHandler.handlePlayerInputs(events, keys, p2, p2InputBuffer)
	collisionResult = hurtBoxCollisionDetection(p1, p2)
	p1ActionToInit = handlePlayerAction(p1, p1ActionFromInput, collisionResult)
	p2ActionToInit = handlePlayerAction(p2, p2ActionFromInput, collisionResult)
	initFinalAction(p1, p1ActionToInit)
	initFinalAction(p2, p2ActionToInit)
	p1.tick()
	p2.tick()

	# TODO: include game UI into renderDisplay and change name of function
	renderDisplay(gameDisplay)
	renderPlayer(p1, gameDisplay)
	renderPlayer(p2, gameDisplay)

	pygame.display.update()
	pygame.event.pump()
	clock.tick(60)


pygame.quit()
quit()


