import pygame
from setting import *
from map import world_map

def mapping(x, y):
	return (x // TILE) * TILE, (y // TILE) * TILE

def ray_casting(screen, player_pos, player_angle, num_thread):
	xo, yo = player_pos
	xm, ym = mapping(xo, yo)
	cur_angle = player_angle - (HALF_FOV - ((NUM_RAYS // THREADS) * num_thread * DELTA_ANGLE))

	for ray in range(NUM_RAYS // THREADS):
		sin_a = math.sin(cur_angle)
		cos_a = math.cos(cur_angle)

		# verticals
		if cos_a >= 0:
			x = xm + TILE
			dx = 1
		else:
			x = xm
			dx = -1
		for	i in range(0, MAX_DEPTH):
			depth_v = (x - xo) / cos_a
			y = yo + depth_v * sin_a
			if mapping(x + dx, y) in world_map:
				break
			x += dx * TILE

		# horizontals
		if sin_a >= 0:
			y = ym + TILE
			dy = 1
		else:
			y = ym
			dy = -1
		for	i in range(0, MAX_DEPTH):
			depth_h = (y - yo) / sin_a
			x = xo + depth_h * cos_a
			if mapping(x, y + dy) in world_map:
				break
			y += dy * TILE

		# projection
		if depth_v < depth_h:
			depth = depth_v
		else:
			depth = depth_h
		depth *= math.cos(player_angle - cur_angle)

		proj_height = min(int(PROJ_COEFF / depth), HEIGHT)

		c = 255 / (1 + depth * depth * 0.00002)
		color = (c, c, c)
		pygame.draw.rect(screen, color, ((((NUM_RAYS // THREADS) * num_thread) + ray) * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
		cur_angle += DELTA_ANGLE