import pygame
import math

from setting import *
from map import wall_hitboxes

class Player:
	def __init__(self):
		self.x, self.y = player_pos
		self.angle = player_angle

		self.speed = player_speed
		self.acc = 1
		self.sens = player_sens
		self.lock_mouse = False

		self.side = player_side
		self.player_hitbox = pygame.Rect(*player_pos, self.side, self.side)

	@property
	def pos(self):
		return (self.x, self.y)

	def collide(self, dx, dy):
		next_step = self.player_hitbox.copy()
		next_step.move_ip(dx, dy)
		hits_ids = next_step.collidelistall(wall_hitboxes)
		if len(hits_ids):
			del_x, del_y = 0, 0
			for hit_id in hits_ids:
				wall_hitbox = wall_hitboxes[hit_id]
				if dx > 0:
					del_x += next_step.right - wall_hitbox.left
				else:
					del_x += wall_hitbox.right - next_step.left
				if dy > 0:
					del_y += next_step.bottom - wall_hitbox.top
				else:
					del_y += wall_hitbox.bottom - next_step.top

			if abs(del_x - del_y) < 10:
				dx, dy = 0, 0
			elif del_x > del_y:
				dy = 0
			elif del_y > del_x:
				dx = 0

		self.x += dx
		self.y += dy

	def move(self):
		self.keys()
		self.mouse()
		self.player_hitbox.center = self.x, self.y

	def mouse(self):
		pygame.mouse.set_visible(self.lock_mouse)
		if pygame.mouse.get_focused() and not self.lock_mouse:
			diff = pygame.mouse.get_pos()[0] - HALF_WIDTH
			pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
			self.angle += diff * self.sens

	def keys(self):
		sin_a = math.sin(self.angle)
		cos_a = math.cos(self.angle)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LSHIFT]: self.acc = player_acceleration
		else: self.acc = 1
		if keys[pygame.K_w]:
			dx = self.speed * self.acc * cos_a
			dy = self.speed * self.acc * sin_a
			self.collide(dx, dy)
		if keys[pygame.K_s]:
			dx = -self.speed * self.acc * cos_a
			dy = -self.speed * self.acc * sin_a
			self.collide(dx, dy)
		if keys[pygame.K_a]:
			dx = self.speed * self.acc * sin_a
			dy = -self.speed * self.acc * cos_a
			self.collide(dx, dy)
		if keys[pygame.K_d]:
			dx = -self.speed * self.acc * sin_a
			dy = self.speed * self.acc * cos_a
			self.collide(dx, dy)
		if keys[pygame.K_f]: self.lock_mouse = True
		else: self.lock_mouse = False