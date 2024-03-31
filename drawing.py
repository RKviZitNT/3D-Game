import pygame
from setting import *
from ray_casting import ray_casting
import threading

class Drawing:
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.SysFont('Arial', 36, bold=True)

	def background(self):
		# pygame.draw.rect(self.screen, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
		pygame.draw.rect(self.screen, BLACKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

	def world(self, player_pos, player_angle):
		lock = threading.Lock()

		def increment_counter():
			with lock:
				ray_casting(self.screen, player_pos, player_angle, num_thread)

		threads = []

		for num_thread in range(THREADS):
			thread = threading.Thread(target=increment_counter)
			thread.start()
			threads.append(thread)

		for thread in threads:
			thread.join()

	def fps(self, clock):
		display_fps = str(int(clock.get_fps()))
		render = self.font.render(display_fps, 0, GREEN)
		self.screen.blit(render, FPS_POS)