import pygame,time,random,math
from collections import Counter
pygame.init()
max_width=600
max_height=500
gameDisplay=pygame.display.set_mode((max_width,max_height))
pygame.display.set_caption("Tanks")

font_chosen_small=pygame.font.SysFont("comicsansms",25)
font_chosen_medium=pygame.font.SysFont("comicsansms",45)
font_chosen_large=pygame.font.SysFont("monospace",60)
	

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
orange=(100,100,0)
green=(0,255,0)
dark_green=(0,100,0)
yellow=(255,255,0)
blue=(0,0,255)
light_blue=(0,0,100)
tank_start_x=250
tank_start_y=450

clock=pygame.time.Clock()

# snakehead=pygame.image.load('final.png')
# appleimage=pygame.image.load('Apple1.png')
# pygame.display.set_icon(appleimage)

# def write_text(message,color,size,offset):
# 	if(size=="small"):

# 		rendering=font_chosen_small.render(message,True,color)
# 	elif(size=="medium"):
# 		rendering=font_chosen_medium.render(message,True,color)
# 	else:
# 		rendering=font_chosen_large.render(message,True,color)
# 	area=rendering.get_rect()
# 	area.center=max_width/2,max_height/2+offset
# 	gameDisplay.blit(rendering,area)

def write_text(message,color,size,offsetx,offsety):
	if(size=="small"):

		rendering=font_chosen_small.render(message,True,color)
	elif(size=="medium"):
		rendering=font_chosen_medium.render(message,True,color)
	else:
		rendering=font_chosen_large.render(message,True,color)
	area=rendering.get_rect()
	area.center=max_width/2+offsetx,max_height/2+offsety
	gameDisplay.blit(rendering,area)


def write_text_to_button(message,color,size,buttonx,buttony,button_width,button_height):
	if(size=="small"):
		textsurface=font_chosen_small.render(message,True,color)
	elif(size=="medium"):
		textsurface=font_chosen_medium.render(message,True,color)
	else:
		textsurface=font_chosen_large.render(message,True,color)

	textrect=textsurface.get_rect()
	textrect.center=buttonx+button_width/2,buttony+button_height/2
	gameDisplay.blit(textsurface,textrect)




def tank(x,y,theta):
	pygame.draw.rect(gameDisplay,black,(x,y,80,30))
	pygame.draw.rect(gameDisplay,green,(0,485,600,15))
	pygame.draw.circle(gameDisplay,black,(x+40,y),20)
	pygame.draw.circle(gameDisplay,black,(x+20,y+30),8)
	pygame.draw.circle(gameDisplay,black,(x+60,y+30),8)
	# pygame.draw.line(gameDisplay,black,(x+40,y-20),((x+40)-30*math.sin(0),y-50+30*(1-math.cos(0))),10)
	pygame.draw.line(gameDisplay,black,(x+40,y-10),((x+40)-40*math.sin(theta),y-50+40*(1-math.cos(theta))),10)



def controls():
	conti=True
	while(conti==True):
		gameDisplay.fill(yellow)
		write_text("Fire : Spacebar",blue,"medium",0,-100)
		write_text("Move turret : Up or Down",blue,"medium",0,0)
		write_text("Move tank : left or right",blue,"medium",0,100)


		

		button("Play",60,400,100,30,green,dark_green,"play")
		# button("Main",220,400,100,30,light_blue,blue,"main")
		button("Quit",380,400,100,30,orange,red,"quit")

		# button("Back",160,400,100,30,green,dark_green,"back")



		pygame.display.update()
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if(event.key==pygame.K_SPACE):
					conti=False
				elif(event.key==pygame.K_ESCAPE):
					pygame.quit()
					quit()
		





def button(message,x,y,width,height,color1,color2,function):
	mouse_position=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()

	if(mouse_position[0]>=x and mouse_position[0]<=x+width and mouse_position[1]>=y and mouse_position[1]<=y+height):

		pygame.draw.rect(gameDisplay,color1,(x,y,width,height))
		if(click[0]==1 and function!=None):
			if(function=="quit"):
				pygame.quit() 
				quit()
			elif function=="controls":
				controls()
			elif function=="back":
				pass
			# elif function=="main":
			# 	start_game()
				# start_game()
			else:
				loop()
	else:
		pygame.draw.rect(gameDisplay,color2,(x,y,width,height))
	write_text_to_button(message,black,"small",x,y,width,height)

def start_game():

	starting=True
	while(starting==True):
		gameDisplay.fill(yellow)
		write_text("Welcome to snake game",green,"medium",0,0)
		write_text("Press space to play",red,"small",0,40)


		

		button("Play",60,400,100,30,green,dark_green,"play")
		button("Controls",220,400,100,30,light_blue,blue,"controls")
		button("Quit",380,400,100,30,orange,red,"quit")



		pygame.display.update()
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if(event.key==pygame.K_SPACE):
					starting=False
				elif(event.key==pygame.K_ESCAPE):
					pygame.quit()
					quit()
		




def loop():
	

	pygame.display.update()

	exit=False
	end=False
	global tank_start_x
	global tank_start_y
	dir_x=0
	theta=0
	del_theta=0

	
	while not exit:
		
		while(end==True):
			write_text("Game over :)",red,"large",0,0)
			write_text("Press space key to play again",red,"medium",0,60)
			
			pygame.display.update()
			for event in pygame.event.get():
				if(event.type==pygame.KEYDOWN):
					if(event.key==pygame.K_ESCAPE):
						end=False
						exit=True
						break
					elif(event.key==pygame.K_SPACE):
						exit=False
						end=False
						loop()

		for event in pygame.event.get():
			
			if event.type==pygame.QUIT:
				end=True
				exit=True
			if event.type==pygame.KEYDOWN:
				if(event.key==pygame.K_ESCAPE):
					exit=True
					
				if(event.key==pygame.K_LEFT):
					dir_x-=2
				
				elif(event.key==pygame.K_RIGHT):
					dir_x=2
				elif(event.key==pygame.K_UP):
					del_theta=(math.pi*2/180)
				elif(event.key==pygame.K_DOWN):
					del_theta=-(math.pi*2/180)
			if(event.type==pygame.KEYUP):
				if(event.key==pygame.K_LEFT):
					dir_x=0
				elif(event.key==pygame.K_RIGHT):
					dir_x=0
				elif(event.key==pygame.K_UP or event.key==pygame.K_DOWN):
					del_theta=0

		
		
		tank_start_x+=dir_x
		theta+=del_theta
		
		gameDisplay.fill(white)
		tank(tank_start_x,tank_start_y,theta)
		

		
		
		
		
		pygame.display.update()

		
		

		clock.tick(20)
	pygame.quit()
	quit()
start_game()
loop()
write_text("You lose",red)
pygame.display.update()

