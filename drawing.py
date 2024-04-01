import pygame

from setting import *
from ray_casting import drawing_walls

class Drawing:
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.SysFont('Arial', 36, bold=True)
		self.textures = {0: pygame.image.load("texture/wall0.jpg").convert(),
						 1: pygame.image.load("texture/wall1.jpg").convert(),
						 }

	def background(self):
		# pygame.draw.rect(self.screen, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
		pygame.draw.rect(self.screen, BLACKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

	def world(self, player):
		drawing_walls(self.screen, player, self.textures)

	def fps(self, clock):
		display_fps = str(int(clock.get_fps()))
		render = self.font.render(display_fps, 0, RED)
		self.screen.blit(render, FPS_POS)