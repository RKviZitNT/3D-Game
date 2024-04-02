import random

from setting import *

sides = {'up': (0, -1), 'right': (1, 0), 'down': (0, 1), 'left': (-1, 0)}
reside = {'up': 'down', 'right': 'left', 'down': 'up', 'left': 'right'}

text_map = [[WALL_SYMBOL for i in range(MAP_WIDTH)] for j in range(MAP_HEIGHT)]

min_entry = MAP_WIDTH * MAP_HEIGHT * 2

start_x, start_y = 1, 1
path_history = [(start_x, start_y)]
text_map[start_y][start_x] = NONE_SYMBOL

def print_map():
	for j in range(MAP_HEIGHT):
		for i in range(MAP_WIDTH):
			print(text_map[j][i], end='')
		print('\n', end='')

def is_wall(x ,y):
	if x > 0 and x < MAP_WIDTH-1 and y > 0 and y < MAP_HEIGHT-1:
		return False
	return True

def is_space(x, y):
	if text_map[y][x] == NONE_SYMBOL:
		return True
	return False

def is_pass(x, y, key):
	key = reside[key]
	if is_space(x, y):
		return False
	for val in sides:
		if val != key:
			dx, dy = sides[val]
			if is_space(x+dx, y+dy):
				return False
	return True

def generate_path():
	path_end = False
	step = 0

	x, y = path_history[step]

	#while not path_end:
	while not path_end:
		sidesch = ['up', 'right', 'down', 'left']
		next_step = False

		for _ in range(4):
			side = random.choice(sidesch)
			sidesch.remove(side)

			if side == 'up':
				if not is_wall(x, y-1) and is_pass(x, y-1, side):
					x, y = x, y-1
					next_step = True
					break
			if side == 'right':
				if not is_wall(x+1, y) and is_pass(x+1, y, side):
					x, y = x+1, y
					next_step = True
					break
			if side == 'down':
				if not is_wall(x, y+1) and is_pass(x, y+1, side):
					x, y = x, y+1
					next_step = True
					break
			if side == 'left':
				if not is_wall(x-1, y) and is_pass(x-1, y, side):
					x, y = x-1, y
					next_step = True
					break

		if not next_step:
			step -= 1
			if step < 0:
				path_end = True
			x, y = path_history[step]
			path_history.pop()
		else:
			text_map[y][x] = NONE_SYMBOL
			path_history.append((x, y))
			step += 1
		#print_map()

def generate():
	generate_path()
	print_map()

generate()