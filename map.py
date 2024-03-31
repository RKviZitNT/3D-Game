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

world_map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            if char == '0':
                world_map[(i * TILE, j * TILE)] = '0'
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'