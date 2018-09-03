import pygame

# change this to json or something

p1Keybind = {	
			"jump": pygame.K_w, 
			"crouch":pygame.K_s, 
			"left":pygame.K_a,
			"right":pygame.K_d,
			"punch":pygame.K_j
			}
validP1Keys = {
			pygame.K_w:"jump" , 
			pygame.K_s:"crouch", 
			pygame.K_a:"left",
			pygame.K_d:"right",
			pygame.K_j:"punch"
}


p2Keybind = {
			"jump":pygame.K_UP,
			"crouch":pygame.K_DOWN,
			"left":pygame.K_LEFT,
			"right":pygame.K_RIGHT,
			"punch":pygame.K_p
}

validP2Keys = {
			pygame.K_UP:"jump" , 
			pygame.K_DOWN:"crouch", 
			pygame.K_LEFT:"left",
			pygame.K_RIGHT:"right",
			pygame.K_p:"punch"
}
