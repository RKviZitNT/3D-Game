import pygame

from setting import *
from player import Player
from drawing import Drawing

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D Game')
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()

	player.move()
	screen.fill(BLACK)

	drawing.background()
	drawing.world(player)
	drawing.fps(clock)

	pygame.display.flip()
	clock.tick(FPS)