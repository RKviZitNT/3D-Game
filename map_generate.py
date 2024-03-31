from random import randint
import sys

from setting import *

sys.setrecursionlimit(100000)

text_map = []

def create_text_map(width, height):
    for y in range(height):
        text_map.append([])
        for x in range(width):
            text_map[-1].append(WALL_SYMBOL)

def generate_path(map, x, y, start_x, start_y, end_x, end_y):
    hodi = []
    now_x, now_y = start_x, start_y
    path = False
    back = 0
    st = 0
    while not path:
        hodi.append([now_x, now_y])

        rand = randint(1, 4)
        if rand == 1 and st != "left":
            st = "right"
            now_x += 2
        if rand == 2 and st != "right":
            st = "left"
            now_x -= 2
        if rand == 3 and st != "down":
            st = "up"
            now_y += 2
        if rand == 4 and st != "up":
            st = "down"
            now_y -= 2

        if now_x > x - 1: now_x = x - 1
        if now_x < 2: now_x = 2
        if now_y < 2: now_y = 2
        if now_y > y - 1: now_y = y - 1

        if map[now_y - 1][now_x - 1] == NONE_SYMBOL:
            now_x = hodi[-1][0]
            now_y = hodi[-1][1]

        if map[now_y - 1][now_x - 1] == WALL_SYMBOL:
            map[now_y - 1][now_x - 1] = NONE_SYMBOL
            if st == "right": map[now_y - 1][now_x - 2] = NONE_SYMBOL
            if st == "left": map[now_y - 1][now_x] = NONE_SYMBOL
            if st == "up": map[now_y - 2][now_x - 1] = NONE_SYMBOL
            if st == "down": map[now_y][now_x - 1] = NONE_SYMBOL

        if len(hodi) > x * y and k == "up" and map[end_y][end_x - 1] == NONE_SYMBOL: now_x, now_y = randint(3, x - 2), randint(3, y - 2)
        if len(hodi) > x * y and k == "down" and map[end_y - 2][end_x - 1] == NONE_SYMBOL: now_x, now_y = randint(3, x - 2), randint(3, y - 2)
        if len(hodi) > x * y and k == "left" and map[end_y - 1][end_x] == NONE_SYMBOL: now_x, now_y = randint(3, x - 2), randint(3, y - 2)
        if len(hodi) > x * y and k == "right" and map[end_y - 1][end_x - 2] == NONE_SYMBOL: now_x, now_y = randint(3, x - 2), randint(3, y - 2)

        if len(hodi) > x * y * koef3:
            path = True

def generate(map):
    global k
    y = len(text_map)
    x = len(text_map[0])
    start_x, start_y = 2, y - 1

    wall = randint(1, 4)

    if wall == 1:
        end_x, end_y = randint(2, x), 1
        k = "up"

    if wall == 2:
        end_x, end_y = randint(4, x - 1), y
        k = "down"

    if wall == 3:
        end_x, end_y = 1, randint(2, y - 4)
        k = "left"

    if wall == 4:
        end_x, end_y = x, randint(2, y - 1)
        k = "right"

    map[start_y - 1][start_x - 1] = NONE_SYMBOL
    map[end_y - 1][end_x - 1] = EXIT_SYMBOL

    generate_path(map, x, y, start_x, start_y, end_x, end_y)

    sym = 0
    max_s = x * y / koef1
    min_s = x * y / koef2
    for i in map:
        for i2 in i:
            if i2 == WALL_SYMBOL:
                sym += 1

    if k == "up" and map[end_y][end_x - 1] == NONE_SYMBOL and sym < max_s and sym > min_s:
        for i in range(len(map)):
            map[i] = "".join(map[i])
            print(map[i])
        return map
    elif k == "down" and map[end_y - 2][end_x - 1] == NONE_SYMBOL and sym < max_s and sym > min_s:
        for i in range(len(map)):
            map[i] = "".join(map[i])
            print(map[i])
        return map
    elif k == "left" and map[end_y - 1][end_x] == NONE_SYMBOL and sym < max_s and sym > min_s:
        for i in range(len(map)):
            map[i] = "".join(map[i])
            print(map[i])
        return map
    elif k == "right" and map[end_y - 1][end_x - 2] == NONE_SYMBOL and sym < max_s and sym > min_s:
        for i in range(len(map)):
            map[i] = "".join(map[i])
            print(map[i])
        return map
    else:
        start()

def start():
    text_map.clear()
    try:
        create_text_map(MAP_WIDTH, MAP_HEIGHT)
        generate(text_map)
    except:
        print("рекурсия")
        start()

start()