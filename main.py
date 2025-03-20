# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():
	print("Starting Asteroids!")
	pygame.init() #initialize all pygame modules
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #This is a Surface class object in pygame
	clock = pygame.time.Clock()
	dt = 0
	whileLoop = True

	player_x = SCREEN_WIDTH / 2
	player_y = SCREEN_HEIGHT / 2
	thePlayer = Player(player_x, player_y)

	while(whileLoop):
		#enable the "x" close window button in upper right corner
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		#define colors used
		color_black = pygame.Color(0,0,0)
		color_white = pygame.Color(255,255,255)

		#draw background graphics on screen
		screen.fill(color=color_black)

		#draw player on screen
		thePlayer.draw(screen)

		#refresh display
		pygame.display.flip()

		#delay starting the next game loop until 60 milliseconds have passed; 
		#we also retrieve amount of time passed since last tick (delta time) 
		#also convert dt from milliseconds to seconds
		dt = clock.tick(60) / 1000 


if __name__ == "__main__":
	main()

	

