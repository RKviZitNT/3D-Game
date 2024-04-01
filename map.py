import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32, float64

from setting import *
from map_generate import text_map

text_map = [
	'000000000000',
	'0.11...11..0',
	'0.1..1.11..0',
	'0......1..10',
	'01..1......0',
	'0..11.1..1.0',
	'0..11...11.0',
	'000000000000',
]

wall_hitboxes = []
world_map = Dict.empty(key_type=types.UniTuple(float64, 2), value_type=int32)
for j, row in enumerate(text_map):
	for i, char in enumerate(row):
		if char != '.':
			wall_hitboxes.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
			if char == '0':
				world_map[(i * TILE, j * TILE)] = 0
			if char == '1':
				world_map[(i * TILE, j * TILE)] = 1