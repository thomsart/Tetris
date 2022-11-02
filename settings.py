import os

import pygame

FPS = 60
LEVEL = [3000, 2750, 2500, 2250, 2000, 1750, 1500, 1250, 1000, 750, 500, 250, 100]
WHITE = (255, 255, 255)
pygame.display.set_caption("T'es-triste")

B = 30 # pixels for each side of the brick
COLUMN = 10
ROW = COLUMN * 2
GAME_WIDTH = B * COLUMN + B * 7
GAME_HEIGHT = B * ROW + B * 2
WIND = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

CONSOLE = [
    # all column edges
    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(0,16),(0,17),(0,18),(0,19),(0,20),
    (11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12),(11,13),(11,14),(11,15),(11,16),(11,17),(11,18),(11,19),(11,20),
    (12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10),(12,11),(12,12),(12,13),(12,14),(12,15),(12,16),(12,17),(12,18),(12,19),(12,20),
    (13,1),(13,2),(13,3),(13,4),(13,5),(13,6),(13,7),(13,8),(13,9),(13,10),(13,11),(13,12),(13,13),(13,14),(13,15),(13,16),(13,17),(13,18),(13,19),(13,20),
    (14,1),(14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,8),(14,9),(14,10),(14,11),(14,12),(14,13),(14,14),(14,15),(14,16),(14,17),(14,18),(14,19),(14,20),
    (15,1),(15,2),(15,3),(15,4),(15,5),(15,6),(15,7),(15,8),(15,9),(15,10),(15,11),(15,12),(15,13),(15,14),(15,15),(15,16),(15,17),(15,18),(15,19),(15,20),
    (16,1),(16,2),(16,3),(16,4),(16,5),(16,6),(16,7),(16,8),(16,9),(16,10),(16,11),(16,12),(16,13),(16,14),(16,15),(16,16),(16,17),(16,18),(16,19),(16,20),
    # bottom edge
    (0,21),(1,21),(2,21),(3,21),(4,21),(5,21),(6,21),(7,21),(8,21),(9,21),(10,21),(11,21),(12,21),(13,21),(14,21),(15,21),(16,21),
] # coord(x,y)

def build_console():

    for coord in CONSOLE:
        WIND.blit(pygame.image.load(os.path.join("assets", "blocks", "edge.png")), (coord[0] * B, coord[1] * B))

GAME_AREA = [] # [ brick_rows[ brick_columns(x, y) ] ]
for Y_Blocks in range(1, ROW + 1):
    row = []
    for X_Blocks in range(1, COLUMN + 1):
        row.append((B * X_Blocks, B * Y_Blocks))
    GAME_AREA.append(row)

##### All sound effects #####
pygame.mixer.init()
ROTATION_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "rotate.wav"))
LOCKED_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "locked.wav"))
JACKPOT_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "jackpot.wav"))
LINE_FREE_SOUNDEFFECT = pygame.mixer.Sound(os.path.join("assets", "midi", "line_free.wav"))


# print(GAME_AREA)
# GAME_AREA = [
# [(30, 30), (60, 30), (90, 30), (120, 30), (150, 30), (180, 30), (210, 30), (240, 30), (270, 30), (300, 30)],
# [(30, 60), (60, 60), (90, 60), (120, 60), (150, 60), (180, 60), (210, 60), (240, 60), (270, 60), (300, 60)],
# [(30, 90), (60, 90), (90, 90), (120, 90), (150, 90), (180, 90), (210, 90), (240, 90), (270, 90), (300, 90)],
# [(30, 120), (60, 120), (90, 120), (120, 120), (150, 120), (180, 120), (210, 120), (240, 120), (270, 120), (300, 120)],
# [(30, 150), (60, 150), (90, 150), (120, 150), (150, 150), (180, 150), (210, 150), (240, 150), (270, 150), (300, 150)],
# [(30, 180), (60, 180), (90, 180), (120, 180), (150, 180), (180, 180), (210, 180), (240, 180), (270, 180), (300, 180)],
# [(30, 210), (60, 210), (90, 210), (120, 210), (150, 210), (180, 210), (210, 210), (240, 210), (270, 210), (300, 210)],
# [(30, 240), (60, 240), (90, 240), (120, 240), (150, 240), (180, 240), (210, 240), (240, 240), (270, 240), (300, 240)],
# [(30, 270), (60, 270), (90, 270), (120, 270), (150, 270), (180, 270), (210, 270), (240, 270), (270, 270), (300, 270)],
# [(30, 300), (60, 300), (90, 300), (120, 300), (150, 300), (180, 300), (210, 300), (240, 300), (270, 300), (300, 300)],
# [(30, 330), (60, 330), (90, 330), (120, 330), (150, 330), (180, 330), (210, 330), (240, 330), (270, 330), (300, 330)],
# [(30, 360), (60, 360), (90, 360), (120, 360), (150, 360), (180, 360), (210, 360), (240, 360), (270, 360), (300, 360)],
# [(30, 390), (60, 390), (90, 390), (120, 390), (150, 390), (180, 390), (210, 390), (240, 390), (270, 390), (300, 390)],
# [(30, 420), (60, 420), (90, 420), (120, 420), (150, 420), (180, 420), (210, 420), (240, 420), (270, 420), (300, 420)],
# [(30, 450), (60, 450), (90, 450), (120, 450), (150, 450), (180, 450), (210, 450), (240, 450), (270, 450), (300, 450)],
# [(30, 480), (60, 480), (90, 480), (120, 480), (150, 480), (180, 480), (210, 480), (240, 480), (270, 480), (300, 480)],
# [(30, 510), (60, 510), (90, 510), (120, 510), (150, 510), (180, 510), (210, 510), (240, 510), (270, 510), (300, 510)],
# [(30, 540), (60, 540), (90, 540), (120, 540), (150, 540), (180, 540), (210, 540), (240, 540), (270, 540), (300, 540)],
# [(30, 570), (60, 570), (90, 570), (120, 570), (150, 570), (180, 570), (210, 570), (240, 570), (270, 570), (300, 570)],
# [(30, 600), (60, 600), (90, 600), (120, 600), (150, 600), (180, 600), (210, 600), (240, 600), (270, 600), (300, 600)]
# ]