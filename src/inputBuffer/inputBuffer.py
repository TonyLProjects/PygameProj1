from collections import deque
import sys
import os
from specialMoveSequence import *

# TODO: 
# 	link this file with constants somehow


# README
# enqueue to front of array probably wouldve been better

class inputBuffer:
	inputBuffer = deque([])
	sizeLimit = 10
	# previousInput used to filter out repeated input from the same key press
	previousInput = ""

	# not sure if this is needed
	def __init__(self, sizeLimit):
		self.inputBuffer = deque([])
		self.sizeLimit = sizeLimit

	# buffer will automatically dequeue if exceed limit
	def enqueue(self, objToEnque):
		if self.getBufferSize() == self.sizeLimit:
			self.dequeue()
		# following if statement used to filter out multiple enqueue request in the same key press
		if self.previousInput != objToEnque:
			self.inputBuffer.append(objToEnque)
		self.previousInput = objToEnque

	def dequeue(self):
		if self.getBufferSize() > 0:
			self.inputBuffer.popleft()
			return
		print("Attempting to dequeue an empty inputBuffer")	# change this to python exception later, should be never called in main

	def printBuffer(self):
		print("printing buffer: ")
		print(self.inputBuffer)
		# for item in self.inputBuffer:
		# 	print(item)										# will be item.printSelf() for inputStruct

	def getBufferSize(self):
		return len(self.inputBuffer)

	def clearBuffer(self):
		self.inputBuffer = deque([])						# not sure how memory management work here in python

# action movement need to be generalized, eg 'punch'
# Acronyms:
# 	DP: Dragon Punch
# 	QCF: Quarter circle forward 
# 	QCB: Quarter circle backard
#	HCF/HCB/FCF/FCB: similar to above. 		H: half 		F: full
	def detectSpecialMove(self):
		bufferSize = self.getBufferSize()
		for sequence in SPECIAL_SEQUENCE:

			if bufferSize >= sequence[0]:
				moveMatches = True
				sequenceLength = sequence[0]
				for i in range(1, sequenceLength):
					if self.inputBuffer[bufferSize-i] != sequence[-i]:
						moveMatches = False
						# break 
				if moveMatches == True:
					print(sequence[1], " matched!")
					if sequence[1] == "QCF":
						print("HADOKEN!")
					self.clearBuffer()
					return sequence[1]

		
'''
psudocode for buffer detection
- since detection occur on every loop, always detect from end of buffer

detect dash
	if buffer[size-1] and buffer[size-2] are both "forward" or backward
		return dash with direction
	does not clear buffer

detect specials
	if buffer[size-1] is attack command:
		qcf = True
		dp = True
		halfCircle = True 	leave these two out for now
		fullCircle = True
		for i in range (3):
			if buffer[size-i-1] != qcf[i]:
				qcf = false
			if buffer[size-i-1] != dp[i]:
				dp = false

		#priority handling
		if dp:
			return dp
		if qcf:
			return qcf


		

'''
