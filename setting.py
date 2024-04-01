import math

# game settings
WIDTH = 1280
HEIGHT = 720
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60 // 2
TILE = 100
FPS_POS = WIDTH - 70, 10
THREADS = 12

# texture settings
TEXTURE_WIDTH = 800
TEXTURE_HEIGHT = 800
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# map settings
MAP_WIDTH = 12
MAP_HEIGHT = 8
koef1 = 1.7
koef2 = 2.2
koef3 = 1.2
WALL_SYMBOL = "1"
NONE_SYMBOL = "."
EXIT_SYMBOL = "x"

# ray casting setting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
MAX_DEPTH = max(MAP_WIDTH, MAP_HEIGHT)
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = (1 * (WIDTH / NUM_RAYS)) * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (1.5 * TILE, MAP_HEIGHT * TILE - 1.5 * TILE)
player_angle = -50
player_speed = 2.5 * (60 / FPS)
turn_speed = 0.02 * (60 / FPS)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 150)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
BLACKGRAY = (30, 30, 30)