
# helper data structure to make rectangle collision code more readable
class squareCoord2d:
	def __init__(self, minCoord, maxCoord):
		self.min = minCoord
		self.max = maxCoord


	# takes in 2 squareCord2d objects, each containing 2 vector2d objects
	# each squareCord2d object represent coordinates of a square
	# returns true if collision detected between the squares, false if no collision
	def checkIfTwoRectCollide(self, coord1, coord2):
		if coord1.x.max < coord2.x.min:
			return False
		if coord1.x.min > coord2.x.max:
			return False
		if coord1.y.max < coord1.y.min:
			return False
		if coord1.y.min > coord2.y.max:
			return False

		return True

