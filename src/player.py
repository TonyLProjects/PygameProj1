import sys 
import os

from vector2d import vector2d
from squareCoord2d import squareCoord2d
from constants import *
# initialize attributes based on character class

class Player:
#player constant attributes
	playerGameSide = 0
	height = 30
	width = 10
	forwardVelocity = 5
	backwardVelocity = 1

	
#player state related variable attributes
#maybe wrap these in a datatype
	canInitAction = True
	recoveryFrames = 0

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

	# 0: facing right, 1: facing left
	# only changed when jumping over the other player
	playerFacingSide = 0
	sideSwitchRequest = False


	def __init__(self, characterClass, playerGameSide):
		self.characterClass = characterClass
		self.playerGameSide = playerGameSide
		if playerGameSide == 1:
			self.playerFacingSide = 0
		else:
			self.playerFacingSide = 1
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
			if self.playerFacingSide == 0:
				self.xPos += self.forwardVelocity
			else:
				self.xPos -= self.forwardVelocity
		if action == "backward":
			if self.playerFacingSide == 0:	
				self.xPos -= self.backwardVelocity
			else:
				self.xPos += self.backwardVelocity

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
				# init jump recovery frames
				self.canInitAction = False
				self.recoveryFrames = 3

		if self.isAttacking == True:
			self.attackFrame -= 1
			if self.attackFrame == 0:			# basically self.resetAttackState()
				self.isAttacking = False
				self.canInitAction = True
				self.attackType = "notAttacking"

		if self.isHitStunned == True:
			pass

		# ticking recovery frames
		if self.recoveryFrames != 0:
			self.recoveryFrames -= 1
			if self.recoveryFrames == 0:
				self.canInitAction = True
		if self.sideSwitchRequest == True:
			if self.isAirborne == False and self.isAttacking == False:

				self.sideSwitch()



	def verticalJump(self):
		self.yVelocity = -15
		self.xVelocity = 0
		self.isAirborne = True
	def forwardJump(self):
		self.yVelocity = -15
		if self.playerFacingSide == 0:
			self.xVelocity = self.forwardVelocity
		else:
			self.xVelocity = -self.forwardVelocity
		self.isAirborne = True
	def backwardJump(self):
		self.yVelocity = -15
		if self.playerFacingSide == 0:
			self.xVelocity = -self.backwardVelocity
		else:
			self.xVelocity = self.backwardVelocity
		self.isAirborne = True

# make this into struct?
	def punch(self):
		print("punch is called")
		self.isAttacking = True
		self.canInitAction = False
		self.attackType = "punch"
		self.attackFrame = 10

	def resetCrouch(self):
		self.isCrouching = False
		self.height = 30


	# TODO: Account for crouch
	def getHurtBox(self):
		minHurtBoxCoord = vector2d(self.xPos, self.yPos)
		maxHurtBoxCoord = vector2d(self.xPos + self.width, self.yPos + self.height)
		hurtboxCoord = squareCoord2d(minHurtBoxCoord, maxHurtBoxCoord)
		return hurtboxCoord

	# hitbox does not always exist
	# need to take in move type as function and check frame count. return hitbox according to move state in the specific frame
	# this replaces the temporary math section
	# need to account player side
	# the same thing need to be accounted in rendering
	def getHitBox(self):
		if self.isAttacking == True and self.alreadyHit == False:
			if self.attackType == "punch":
				if self.playerFacingSide == 0:
				# temporary math, change later
					minHitBoxCoord = vector2d(self.xPos + (self.width/2), self.yPos + (self.height/3))
					maxHitBoxCoord = vector2d(self.xPos + (self.width/2)+20, self.yPos + (self.height/3)+5)
				else:
					minHitBoxCoord = vector2d(self.xPos - (self.width/2)-20, self.yPos + (self.height/3))
					maxHitBoxCoord = vector2d(self.xPos - (self.width/2), self.yPos + (self.height/3+5))
				hitBoxCoord = squareCoord2d(minHitBoxCoord, maxHitBoxCoord)
				print(hitBoxCoord.max.x)
				print(hitBoxCoord.min.x)
				print(self.xPos)
				return hitBoxCoord


		# players can never have coord of 0,0 since it's top left of screen
		noHitBoxRet = vector2d(0,0)	
		noHitbox = squareCoord2d(noHitBoxRet, noHitBoxRet)
		return noHitbox

	def initSideSwitch(self):
		self.sideSwitchRequest = True

	def sideSwitch(self):
		self.playerFacingSide = (self.playerFacingSide + 1) % 2
		self.sideSwitchRequest = False
		print(self.playerGameSide)
		print("executing side switch")

