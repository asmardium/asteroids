# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
	print("Starting Asteroids!")
	pygame.init() #initialize all pygame modules
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #This is a Surface class object in pygame
	whileLoop = True
	while(whileLoop):
		#enable the "x" close window button in upper right corner
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		#define colors used
		color_black = pygame.Color(0,0,0)
		color_white = pygame.Color(255,255,255)

		#draw graphics on screen
		screen.fill(color=color_black)

		#refresh display
		pygame.display.flip()


if __name__ == "__main__":
	main()

	

