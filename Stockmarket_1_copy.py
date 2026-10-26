import pygame
pygame.init()

import random

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

poop = 1000
direction = 2


currentFrame = 0
while True:

	currentFrame += 1


	mo = [.9, 1.25]
	
	eeg = []
	for i in range(2):
		eeg.append(round( (poop*mo[i]-poop) ))


	changeChance = [
		1,
		# in
		10
	]

	if currentFrame%round(60/1) == 0:
		if random.randint(1, changeChance[1]) <= changeChance[0]:
			if direction < 0:
				direction += 3
			elif direction > 0:
				direction -= 3
		poop += random.randint(eeg[0], eeg[1])*direction



	screen.fill("lavender")

	ree = font.render(str(int(poop)), True, "black")
	screen.blit(ree, (0, 0))

	ra = font.render(str(direction), True, "black")
	screen.blit(ra, (0, 40))



	pygame.display.update()
	clock.tick(60)
