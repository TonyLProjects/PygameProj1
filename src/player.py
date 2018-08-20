import sys 
import os

from constants import *
# initialize attributes based on character class

class Player:
#player constant attributes
	characterClass = ""
	playerGameSide = 0
	forwardVelocity = 1
	jumpHeight = 1
	forwardJumpDistance = 1
	
#player state related variable attributes
	healthPoint = 100

	isBlocking = False
	isJumping = False
	isCrouching = False
	isAttacking = False
	isHitStunned = False

	inputLock = False

#player variable attributes
	xPos = 0
	yPos = 0
	playerLocationSide = 0


	def __init__(self, characterClass, playerSide):
		self.characterClass = characterClass
		self.playerGameSide = playerSide
		self.playerLocationSide = playerSide
		if playerSide == 1:
			self.xPos = DEFAULT_P1_XPOS
			self.yPos = DEFAULT_P1_YPOS
		else:
			self.xPos = DEFAULT_P2_XPOS
			self.yPos = DEFAULT_P2_YPOS

		#initialize the rest according to character class

###getter/setter
	def isInputLocked(self):
		return inputLock



###class methods

	#control character left-right movement behavior including when both L/R keys are pressed
	#state design see design.txt section [	TODO	]
	def handleDirectionalMovement(self, event):
		pass

	#TODO: 
#	improve readability
#	code written according to state design in design.txt
	
		# x = 400
		# y = 300
		# keyHeld = 0
		# currentDirection = 0
		# forwardVelocity = 5
		# backwardVelocity = -5



		# if keyHeld == 0 and currentDirection == 0:
		# 	if event.type == pygame.KEYDOWN:
		# 		if event.key == pygame.K_a:
		# 			currentDirection = -1
		# 		elif event.key == pygame.K_d:
		# 			currentDirection = 1
		# elif keyHeld == 0 and currentDirection == 1:
		# 	if event.type == pygame.KEYUP:
		# 		if event.key == pygame.K_d:
		# 			currentDirection = 0
		# 	elif event.type == pygame.KEYDOWN:
		# 		if event.key == pygame.K_a:
		# 			keyHeld = currentDirection
		# 			currentDirection = -1
		# elif keyHeld == 0 and currentDirection == -1:
		# 	if event.type == pygame.KEYUP:
		# 		if event.key == pygame.K_a:
		# 			currentDirection = 0
		# 	elif event.type == pygame.KEYDOWN:
		# 		if event.key == pygame.K_d:
		# 			keyHeld = currentDirection
		# 			currentDirection = 1
		# elif keyHeld == 1 and currentDirection == -1:
		# 	if event.type == pygame.KEYUP:
		# 		if event.key == pygame.K_a:
		# 			currentDirection = keyHeld
		# 			keyHeld = 0
		# 		if event.key == pygame.K_d:
		# 			keyHeld = 0
		
		# elif keyHeld == -1 and currentDirection == 1:
		# 	if event.type == pygame.KEYUP:
		# 		if event.key == pygame.K_d:
		# 			currentDirection = keyHeld
		# 			keyHeld = 0
		# 		if event.key == pygame.K_a:
		# 			keyHeld = 0
		

		# if currentDirection == 1:
		# 	x += forwardVelocity
		# elif currentDirection == -1:
		# 	x += backwardVelocity