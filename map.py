from setting import *
from map_generate import text_map

# text_map = [
# 	'WWWWWWWWWWWW',
# 	'W.WW...WW..W',
# 	'W.W..W.WW..W',
# 	'W......W..WW',
# 	'WW..W......W',
# 	'W..WW.W..W.W',
# 	'W..WW...WW.W',
# 	'WWWWWWWWWWWW',
# ]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '#':
            world_map.add((i * TILE, j * TILE))