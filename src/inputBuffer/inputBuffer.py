from collections import deque


class inputBuffer:
	inputBuffer = deque([])
	sizeLimit = 5000
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


