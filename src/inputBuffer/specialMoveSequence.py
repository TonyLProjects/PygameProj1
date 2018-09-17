
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for word in thisdict:
# 	print(word)
# 	print(thisdict[word])


# special move sequence format: 
# index 0: number of moves
# index 1: name of move
# anything after: sequence itself
SPECIAL_SEQUENCE = [
	[3, "QCF", "down", "forwardDown", "forward"],
	[3, "QCB", "down", "backwardDown", "backward"],
	[3, "DP", "forward", "down", "forward"],
	[2, "forwardDash", "forward", "forward"],
	[2, "backwardDash", "backward", "backward"]
]
