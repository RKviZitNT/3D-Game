import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 90
TILE = 100
FPS_POS = WIDTH - 70, 10
THREADS = 12

# map settings
MAP_HEIGHT = 20
MAP_WIDTH = 20
koef1 = 1.7
koef2 = 2.2
koef3 = 1.2
WALL_SYMBOL = "#"
NONE_SYMBOL = "."
EXIT_SYMBOL = "x"

# ray casting setting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 1200
MAX_DEPTH = max(MAP_WIDTH, MAP_HEIGHT)
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 0.8 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (1.5 * TILE, MAP_HEIGHT * TILE - 1.5 * TILE)
player_angle = -50
player_speed = 2.5 * (60 / FPS)
turn_speed = 0.04 * (60 / FPS)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 150)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
BLACKGRAY = (30, 30, 30)