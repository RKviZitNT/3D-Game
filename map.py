import pygame
from numba.core import types
from numba.typed import Dict
from numba import int64, float64

from setting import *
from maze_gen import text_map

# text_map = [
# 	'000000000000',
# 	'0.11...11..0',
# 	'0.1..1.11..0',
# 	'0......1..10',
# 	'01..1......0',
# 	'0..11.1..1.0',
# 	'0..11...11.0',
# 	'000000000000',
# ]

wall_hitboxes = []
world_map = Dict.empty(key_type=types.UniTuple(float64, 2), value_type=int64)
for j, row in enumerate(text_map):
	for i, char in enumerate(row):
		if char != NONE_SYMBOL:
			wall_hitboxes.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
			if char == '0':
				world_map[(i * TILE, j * TILE)] = 0
			if char == '1':
				world_map[(i * TILE, j * TILE)] = 1
			if char == 'X':
				world_map[(i * TILE, j * TILE)] = 10