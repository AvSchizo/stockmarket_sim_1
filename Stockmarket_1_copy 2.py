import pygame
pygame.init()

import random

from math import log

space = [400, 300]

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

poop = [1000, 0]
direction = 1
operating = 200
upped = (space[1]-operating)/2


def pissyDissy():

	poopShit = []

	for i in range(int(space[0]/xScale)):
		if i >= len(poop)-1:
			break
		poopShit.append(poop[i])
	
	return poopShit



currentFrame = 0
while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			quit()

	currentFrame += 1


	mo = [
		[-2, -1],
		[1, 2]
	]
	

	changeChance = [
		1,
		# in
		20
	]

	if currentFrame%round(60/(2)) == 0:

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

	mPos = pygame.mouse.get_pos()
	xScale = int((1/2000)*(mPos[0]**2)+1)
	if xScale <= 0:
		xScale = 1
	# test
	if pygame.key.get_pressed()[pygame.K_SPACE]:
		xScale = 0.5
	else:
		xScale = 1


	omega = pissyDissy()

	limits = [min(omega), max(omega)]
	diff = limits[1]-limits[0]
	if diff == 0:
		sC = 1
	else:
		sC = operating/diff

	startRight = (len(omega)-1)*xScale
	pointst = []
	for i, e in enumerate(omega):
		addin = [
			startRight-i*xScale,
			space[1]-((e-limits[0])*(sC)+upped)
		]
		pointst.append(addin)

	for i, e in enumerate(omega):
		if i == len(omega)-1:
			continue
		
		if pointst[i][1] > pointst[i+1][1]:
			color = "red"
		elif pointst[i][1] < pointst[i+1][1]:
			color = "green"
		else:
			color = "grey"

		pygame.draw.line(screen, color, pointst[i], pointst[i+1])
		



	pygame.display.update()
	clock.tick(60)
