import pygame
pygame.init()

import random

from math import log

space = [400, 300]

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

poop = [1000, 0]
direction = -1
operating = 200
upped = (space[1]-operating)/2

xScale = 3

tamps = {
	pygame.K_1: False,
	pygame.K_2: False,
	pygame.K_3: False,
	pygame.K_4: False,
}


def pissyDissy():

	poopShit = []

	for i in range(int(space[0]/xScale)):
		if i >= len(poop)-1:
			break
		poopShit.append(poop[i])
	
	return poopShit



def intoBin():
	tot = 0

	loppy = list(tamps.values())
	for i in range(len(loppy)):
		tot += loppy[i]*2**i

	return tot



def truncIt(num, lev):

	bots = str(num).split(".")
	if len(bots) == 1:
		return str(num)
	return str(num) + bots[1][:lev]



currentFrame = 0
while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key in tamps.keys():
				if tamps[event.key] == False:
					tamps[event.key] = True
				else:
					tamps[event.key] = False

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

	if currentFrame%round(60/(10)) == 0:

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

	# xScale
	mPos = pygame.mouse.get_pos()
	if pygame.key.get_pressed()[pygame.K_SPACE]:
		xScale = max(1, int((1/2000)*(mPos[0]**2)+1))
		if pygame.key.get_pressed()[pygame.K_r]:
			if intoBin() == 0:
				oaga = 1
			else:
				oaga = intoBin()
			xScale /= oaga

		scaleShow = font.render(truncIt(xScale, 2), True, "black")
	else:
		scaleShow = None
	#


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


	if scaleShow != None:
		screen.blit(scaleShow, scaleShow.get_rect(bottomleft=[0, screen.get_height()]))
		



	pygame.display.update()
	clock.tick(60)