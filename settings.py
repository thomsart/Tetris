import os

import pygame


FPS = 60
LEVEL = [1000, 800, 600, 500, 400, 350, 300, 150, 100, 75, 50]
POINT = [10, 20, 40, 80, 150, 300, 600, 1300, 3000, 10000, 20000]
WHITE = (255, 255, 255)
EDGE = os.path.join("assets", "blocks", "edge.png")
PAUSE = pygame.image.load(os.path.join("assets", "blocks", "pause.png"))
pygame.display.set_caption("Tetris")

BRICK = 30 # pixels for each side of the brick
COLUMN = 10
ROW = COLUMN * 2
CONSOLE = 7
GAME_WIDTH = BRICK * COLUMN + BRICK * CONSOLE
GAME_HEIGHT = BRICK * (ROW + 2)
WIND = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

def display_screen():

    for row in range(0, GAME_HEIGHT, BRICK):
        for column in range(0, GAME_WIDTH, BRICK):
            WIND.blit(pygame.image.load(EDGE), (column, row))

display_screen()

"""
w To avoid to refresh useless zone in the game, we create two distincts
Surfaces, one for the pieces areaand an other one for the console board. 
"""
PLAY_SURFACE = pygame.Surface((BRICK * COLUMN, BRICK * ROW))
PLAY_RECT = pygame.Rect((BRICK, BRICK), (BRICK * COLUMN, BRICK * ROW))
CONSOLE_SURFACE = pygame.Surface((BRICK * 4, BRICK * 16))
CONSOLE_RECT = CONSOLE_SURFACE.get_rect(topleft=(BRICK * 12, BRICK))

PLAY_AREA = [] # [ brick_rows[ brick_columns(x, y) ] ]
for Y_Blocks in range(1, ROW + 1):
    row = []
    for X_Blocks in range(1, COLUMN + 1):
        row.append((BRICK * X_Blocks, BRICK * Y_Blocks))
    PLAY_AREA.append(row)
# print(PLAY_AREA)

##### All sound effects #####
pygame.mixer.init()
ROTATION_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "rotate.wav"))
LOCKED_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "locked.wav"))
JACKPOT_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "jackpot.wav"))
LINE_FREE_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "line_free.wav"))
GAMEOVER_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "gameover_laugth.wav"))
BINGO_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "bingo.wav"))
pygame.mixer.music.load(os.path.join("assets", "midi", "music_overworld.wav"))

##### Text ##################
pygame.font.init()
TEXT = pygame.font.SysFont('monospace', 19, bold=True)

