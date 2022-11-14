import os

import pygame

from settings import *


FREE_BRICK = pygame.sprite.Group()
BLOCKED_BRICKS = pygame.sprite.Group()


class Brick(pygame.sprite.Sprite):
    """
    Brick are a square of 20 pixels by 20 pixels.
    """

    def __init__(self, row, column, color):
        pygame.sprite.Sprite.__init__(self)
        self.row = row # from 0 to 19
        self.column = column # from 0 to 9 <- or ->
        self.position = PLAY_AREA[self.row][self.column]
        self.image = pygame.image.load(os.path.join("assets", "blocks", f"{color}.png"))
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

        # We decide to put at the initialisation the Bricks in the FREE_BRICK group
        # in order to make difference between piece in moving and locked pieces.
        FREE_BRICK.add(self)
        FREE_BRICK.update()


    def refresh_position(self):
        """ This method is call to refresh in the game new positions
        of the Bricks which composed the piece. """

        self.position = PLAY_AREA[self.row][self.column]
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
