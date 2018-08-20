import sys
import os
import pygame

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


# inputHandler = InputHandler()


while not gameExit:
	pressed = 0

	keys = pygame.key.get_pressed()
	p1Inputs = []
		#if p1 or p2's input keys are in 'keys', push it to the input list

	inputHandler.handlePlayerInput(p1Inputs, p1)
	inputHandler.handlePlayerInput(p2Inputs, p2)


	if keys[pygame.K_a]:
		print('a is pressed')

	if keys[pygame.K_d]:
		print("d is pressed")

	if keys[pygame.K_a] and keys[pygame.K_d]:
		print('a and d are pressed')


	events = pygame.event.get()
	for event in events:
		# print(event)

		#TODO: define p1/p2Action type
		# p1Actions = inputHandler.handlePlayerInput(event, p1, 1)
		# p2Actions = inputHandler.handlePlayerInput(event, p2, 2)


		if event.type == pygame.QUIT:
			gameExit = True


	# update(p1, p2, p1Actions, p2Actions)
	render(p1, p2, gameDisplay)


	if pressed > 0:
		print('end of frame: ' + str(pressed))

	pygame.display.update()
	pygame.event.pump()
	clock.tick(60)


pygame.quit()
quit()


