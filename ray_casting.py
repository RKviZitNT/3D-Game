import pygame
from numba import njit

from setting import *
from map import world_map

@njit(fastmath=True)
def mapping(x, y):
	return (x // TILE) * TILE, (y // TILE) * TILE

@njit(fastmath=True)
def ray_casting(player_pos, player_angle, world_map):
	walls = []
	texture_v, texture_h = 0, 0
	xo, yo = player_pos
	xm, ym = mapping(xo, yo)
	cur_angle = player_angle - HALF_FOV

	for ray in range(NUM_RAYS):
		sin_a = math.sin(cur_angle)
		cos_a = math.cos(cur_angle)
		sin_a = sin_a if sin_a else 0.000001

		# verticals
		if cos_a >= 0:
			x = xm + TILE
			dx = 1
		else:
			x = xm
			dx = -1
		for	i in range(0, MAX_DEPTH):
			depth_v = (x - xo) / cos_a
			yv = yo + depth_v * sin_a
			tile_v = mapping(x + dx, yv)
			if tile_v in world_map:
				texture_v = world_map[tile_v]
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
			xh = xo + depth_h * cos_a
			tile_h = mapping(xh, y + dy)
			if tile_h in world_map:
				texture_h = world_map[tile_h]
				break
			y += dy * TILE

		# projection
		if depth_v < depth_h:
			depth = depth_v
			offset = yv
			texture = texture_v
		else:
			depth = depth_h
			offset = xh
			texture = texture_h
		offset = int(offset) % TILE

		depth *= math.cos(player_angle - cur_angle)

		depth = max(depth, 0.00001)
		proj_height = min(int(PROJ_COEFF / depth), HEIGHT * 7)

		walls.append((depth, offset, texture, proj_height))

		cur_angle += DELTA_ANGLE
	return walls

def drawing_walls(screen, player, textures):
	walls = ray_casting(player.pos, player.angle, world_map)
	for ray, values in enumerate(walls):
		depth, offset, texture, proj_height = values
		wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
		wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
		wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
		screen.blit(wall_column, (ray * SCALE, HALF_HEIGHT - proj_height // 2))