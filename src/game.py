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
def renderPlayer(player, display):
	if player.playerGameSide == 1:
		pygame.draw.rect(display, BLACK, [player.xPos, player.yPos, player.width, player.height])
		if player.isAttacking == True:
			coord = player.getHitBox()
			hitboxHeight = coord[1].y - coord[0].y
			hitboxWidth = coord[1].x - coord[0].x
			pygame.draw.rect(display, BLUE, [coord[0].x, coord[0].y, hitboxWidth, hitboxHeight])
	if player.playerGameSide == 2:
		pygame.draw.rect(display, RED, [player.xPos, player.yPos, player.width, player.height])


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

	p1Action = inputHandler.handlePlayerInputs(events, keys, p1.playerGameSide, p1.playerLocationSide)
	p2Action = inputHandler.handlePlayerInputs(events, keys, p2.playerGameSide, p2.playerLocationSide)
	# print(p1Action)
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


