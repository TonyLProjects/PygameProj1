import sys
import os
import pygame

# import inputBuffer
import inputHandler
import updater
import Keybindings as keybinds
import player
import vector2d

from constants import *

def renderDisplay(display):
	gameDisplay.fill(WHITE)	

# temporary rendering method, will be changed
# TODO: move these to the player class since need side detection
def renderPlayer(player, display):
		drawPlayerBody(player, display)
		drawPlayerAttack(player, display)

def drawPlayerBody(player, display):
	if player.playerGameSide == 1:
		pygame.draw.rect(display, BLACK, [player.xPos, player.yPos, player.width, player.height])
	else:
		pygame.draw.rect(display, RED, [player.xPos, player.yPos, player.width, player.height])


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
# p1InputBuffer = inputBuffer()
# p2InputBuffer = inputBuffer()


while not gameExit:

	currentPressedKeys = []
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			gameExit = True
	# action events handled with KEYDOWN events


	# movement handled with pressed keys 
	keys = pygame.key.get_pressed()

	p1Action = inputHandler.handlePlayerInputs(events, keys, p1.playerGameSide, p1.playerFacingSide)
	p2Action = inputHandler.handlePlayerInputs(events, keys, p2.playerGameSide, p2.playerFacingSide)
	# print(p1Action)
	# print(p2Action)

	collisionResult = updater.hurtBoxCollisionDetection(p1, p2)

	updater.update(p1, p1Action, collisionResult)
	updater.update(p2, p2Action, collisionResult)

	# TODO: include game UI into renderDisplay and change name of function
	renderDisplay(gameDisplay)
	renderPlayer(p1, gameDisplay)
	renderPlayer(p2, gameDisplay)

	pygame.display.update()
	pygame.event.pump()
	clock.tick(60)


pygame.quit()
quit()


