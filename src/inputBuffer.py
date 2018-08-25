import sys 
import os
import pygame
from collections import deque

from constants import *


class InputBuffer:
	inputBuffer = deque([])

	# not sure if this is needed
	def __init__(self):


	def enqueue(self, objToEnque):
		self.inputBuffer.append(objToEnque)

	def dequeue(self):
		self.inputBuffer.popleft()

	def findSpecialAction(self):
		pass
