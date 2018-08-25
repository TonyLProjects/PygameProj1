import sys 
import os

from constants import *
# initialize attributes based on character class

class Player:
#player constant attributes
	characterClass = ""
	playerGameSide = 0
	forwardVelocity = 1
	backwardVelocity = 0.5
	jumpHeight = 1
	forwardJumpDistance = 1
	
#player state related variable attributes
	healthPoint = 100
	canInitAction = True

	isBlocking = False
	isAirborne = False
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




###class methods
	# validity of action is handled in another function
	def initializeAction(self, action):
		if action == "forward":
			self.xPos += self.forwardVelocity
		if action == "backward":
			self.xPos -= self.backwardVelocity
		if action == "crouch":
			# self.crouch()
			pass
		if action == "verticalJump":
			print("imjumping")
			# self.verticalJump()
			pass
		if action == "forwardJump":
			# self.forwardJump()
			pass
		if action == "backwardJump":
			# self.backwardJump()
			pass
		if action == "punch":
			# self.punch()
			pass

	def tick(self):
		pass


