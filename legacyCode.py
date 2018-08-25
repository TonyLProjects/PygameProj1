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