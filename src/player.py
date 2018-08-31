import sys 
import os

from vector2d import vector2d
from constants import *
# initialize attributes based on character class

class Player:
#player constant attributes
	playerGameSide = 0
	height = 30
	width = 10
	forwardVelocity = 2
	backwardVelocity = 1

	
#player state related variable attributes
#maybe wrap these in a datatype
	canInitAction = True
	isBlocking = False
	isAirborne = False
	isCrouching = False
	isHitStunned = False

	isAttacking = False
	alreadyHit = False
	attackType = "notAttacking"
	attackFrame = 0


#player variable attributes
	xPos = 0
	yPos = 0
	xVelocity = 0
	yVelocity = 0
	playerLocationSide = 0


	def __init__(self, characterClass, playerGameSide):
		self.characterClass = characterClass
		self.playerGameSide = playerGameSide
		self.playerLocationSide = playerGameSide
		if playerGameSide == 1:
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
			self.isCrouching = True
			self.height = 15
		if action == "verticalJump":
			self.verticalJump()
		if action == "forwardJump":
			self.forwardJump()
		if action == "backwardJump":
			self.backwardJump()
		if action == "punch":
			self.punch()
			pass


	def tick(self):
		# update jump frames
		if self.isAirborne == True:
			self.yPos += self.yVelocity
			self.xPos += self.xVelocity
			self.yVelocity += 1
			if self.yPos >= GAMEFLOOR:
				self.yVelocity = 0
				self.yPos = GAMEFLOOR
				self.isAirborne = False	

		if self.isAttacking == True:
			self.attackFrame -= 1
			if self.attackFrame == 0:			# basically self.resetAttackState()
				self.isAttacking = False
				self.canInitAction = True
				self.attackType = "notAttacking"

		if self.isHitStunned == True:
			pass



	def verticalJump(self):
		self.yVelocity = -15
		self.xVelocity = 0
		self.isAirborne = True
	def forwardJump(self):
		self.yVelocity = -15
		self.xVelocity = self.forwardVelocity
		self.isAirborne = True
	def backwardJump(self):
		self.yVelocity = -15
		self.xVelocity = -self.backwardVelocity
		self.isAirborne = True

# make this into struct?
	def punch(self):
		self.isAttacking = True
		self.canInitAction = False
		self.attackType = "punch"
		self.attackFrame = 10

	def resetCrouch(self):
		self.isCrouching = False
		self.height = 30


	# TODO: Account for crouch
	def getHurtBox(self):
		minHurtBoxCord = vector2d(self.xPos, self.yPos)
		maxHurtBoxCord = vector2d(self.xPos + self.width, self.yPos + self.height)
		return (minHurtBoxCord, maxHurtBoxCord)

	# hitbox does not always exist
	# need to take in move type as function and check frame count. return hitbox according to move state in the specific frame
	# this replaces the temporary math section
	# need to account player side
	# the same thing need to be accounted in rendering
	def getHitBox(self):
		if self.isAttacking == True and self.alreadyHit == False:
			if self.attackType == "punch":
				# temporary math, change later
				minHitBoxCord = vector2d(self.xPos + (self.width/2), self.yPos + (self.height/3))
				maxHitBoxCord = vector2d(self.xPos + (self.width/2)+20, self.yPos + (self.height/3)+5)
				return (minHitBoxCord, maxHitBoxCord)
		# players can never have coord of 0,0 since it's top left of screen
		noHitBoxRet = vector2d(0,0)		
		return (noHitBoxRet, noHitBoxRet)
