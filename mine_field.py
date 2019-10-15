
import pygame, sys
from random import random
from pygame.locals import *

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

FPS = 60
WIDTH = 700
HEIGHT = 500

class Cell:
	def __init__(self, i, j, size):
		self.color = BLACK
		self.visible = False
		self.mine = False
		self.value = 0
		self.rect = pygame.Rect(i*size, j*size, size, size)
		
		if(random() < 0.1):
			self.mine = True
		
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect, 1)
		if self.mine :
			
		
	def update(self):
		pass

def main():
	global SCREEN
	
	pygame.init()

	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

	pygame.display.set_caption("My Game")
	clock = pygame.time.Clock()

	cell_size = 100
	num_cells = 5
	x_margin = 0
	y_margin = 0
	
	cells = []
	for i in range(num_cells):
		for j in range(num_cells):
			cells.append(Cell(i, j, cell_size))
			
	for cell in cells:
		pass
	

	while True:
		for event in pygame.event.get():
			#~ print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		SCREEN.fill(WHITE)
		
		for cell in cells:
			cell.draw(SCREEN)

		pygame.display.flip()
		clock.tick(FPS)

	

if __name__ == '__main__':
	main()

