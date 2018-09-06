# helper data structure to make hit detection result code more readable
class hitResult:
	def __init__(self, p1Res, p2Res, moveThatHitP1, moveThatHitP2):
		self.p1HitResult = p1Res
		self.p2HitResult = p2Res
		self.moveThatHitP1 = moveThatHitP1
		self.moveThatHitP2 = moveThatHitP2

		