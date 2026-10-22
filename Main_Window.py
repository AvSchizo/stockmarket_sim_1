import pygame
pygame.init()

import random

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

poop = [1000, 0]
direction = 1
xScale = 10
operating = 200
upped = (300-operating)/2



currentFrame = 0
while True:

	currentFrame += 1


	mo = [
		[-300, -100],
		[500, 800]
	]
	

	changeChance = [
		1,
		# in
		20
	]

	if currentFrame%round(60/2) == 0:

		# direction change
		if random.randint(1, changeChance[1]) <= changeChance[0]:
			direction *= -1
		
		if random.randint(1, 3) <= 1.5-direction/2:
			addRad = random.randint(mo[0][0], mo[0][1])
		else:
			addRad = random.randint(mo[1][0], mo[1][1])

		poop.insert(0, round(poop[0] + addRad*(poop[0]/1000)) )



	screen.fill("grey")

	ree = font.render(str(int(poop[0])), True, "black")
	screen.blit(ree, (0, 0))

	ra = font.render(str(direction), True, "black")
	screen.blit(ra, (0, 40))


	limits = [min(poop), max(poop)]
	diff = limits[1]-limits[0]
	if diff == 0:
		sC = 1
	else:
		sC = operating/diff

	pointst = []
	for i, e in enumerate(poop):
		addin = [
			400-i*xScale,
			(e-limits[1])*(sC)+upped
		]
		pointst.append(addin)

	for i, e in enumerate(poop):
		if i == len(poop)-1:
			continue
		
		if e > poop[i+1]:
			color = "green"
		elif e < poop[i+1]:
			color = "red"
		else:
			color = "grey"

		pygame.draw.line(screen, color, pointst[i], pointst[i+1])
		



	pygame.display.update()
	clock.tick(60)
