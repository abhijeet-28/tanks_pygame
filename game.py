import pygame
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
gameDisplay=pygame.display.set_mode((800,600))
gameDisplay.fill(blue)
pixels=pygame.PixelArray(gameDisplay)
for i in range(0,10):
	for j in range(0,10):
		pixels[i][j]=black
pygame.draw.circle(gameDisplay,white,(100,100),10)
while True:
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			pygame.quit()
			quit()
		elif(event.type==pygame.KEYDOWN):
			if(event.key==pygame.K_ESCAPE):
				pygame.quit()
				quit()
	pygame.display.update()