import random

from setting import *

sides = {'up': (0, -1), 'right': (1, 0), 'down': (0, 1), 'left': (-1, 0)}
reside = {'up': 'down', 'right': 'left', 'down': 'up', 'left': 'right'}

text_map = [[WALL_SYMBOL for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

def print_map():
    for j in range(MAP_HEIGHT):
        for i in range(MAP_WIDTH):
            print(text_map[j][i], end=' ')
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

def generate_path(start_x, start_y):
    path_history = [(start_x, start_y)]

    while path_history:
        x, y = path_history[-1]
        text_map[y][x] = NONE_SYMBOL
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
            path_history.pop()
        else:
            text_map[y][x] = NONE_SYMBOL
            path_history.append((x, y))

    for i in range(-1, 2):
        for j in range(-1, 2):
            text_map[start_y+i][start_x+j] = NONE_SYMBOL

    exit_spawn = random.choice(['up', 'down'])
    if exit_spawn == 'up':
        walls = [i for i in range(1, MAP_WIDTH-2)]
        wall = random.choice(walls)
        walls.remove(wall)
        for _ in range(len(walls)):
            if text_map[1][wall] == NONE_SYMBOL:
                text_map[0][wall] = EXIT_SYMBOL
                break
    if exit_spawn == 'down':
        walls = [i for i in range(1, MAP_WIDTH-2)]
        wall = random.choice(walls)
        walls.remove(wall)
        for _ in range(len(walls)):
            if text_map[MAP_HEIGHT-2][wall] == NONE_SYMBOL:
                text_map[MAP_HEIGHT-1][wall] = EXIT_SYMBOL
                break

def generate():
    generate_path(MAP_WIDTH//2, MAP_HEIGHT//2)
    print_map()

generate()