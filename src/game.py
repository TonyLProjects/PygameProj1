import sys
import os
import pygame

# import inputBuffer
import inputHandler
import updater
import Keybindings as keybinds
import player

from constants import *

def render(p1, p2, display):
	gameDisplay.fill(WHITE)	
	pygame.draw.rect(display, BLACK, [p1.xPos, p1.yPos, 10, 10])
	pygame.draw.rect(display, RED, [p2.xPos, p2.yPos, 10, 10])

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
	# not sure how to design the updater module module

	collisionResult = updater.hurtboxCollisionDetection(p1, p2)
	updater.update(p1, p1Action, collisionResult)
	updater.update(p2, p2Action, collisionResult)




	# update(p1, p2, p1Actions, p2Actions)
	render(p1, p2, gameDisplay)

	pygame.display.update()
	pygame.event.pump()
	clock.tick(60)


pygame.quit()
quit()


