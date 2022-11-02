import pygame
from pygame.locals import *

from settings import *
from classes.piece import *



def main():

    clock = pygame.time.Clock()
    clock.tick(FPS)
    chrono = 0
    level = 10
    score = 0
    piece = Piece()
    play = True

    while play:

        WIND.fill(WHITE)
        build_console()
        BLOCKED_BRICKS.draw(WIND)
        WIND.blit(TEXT.render("Score: " + str(score), 5, (0, 0, 0)), (5, 0))
        WIND.blit(TEXT.render("Level: " + str(level), 5, (0, 0, 0)), (200, 0))

        chrono += 1
        if chrono > 10000:
            chrono = 0

        if piece.is_locked():
            if piece.is_drowned():
                play = False
            else:
                score += piece.add_points(level)
                print("New score : " + str(score))
                piece = Piece()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    piece.move_right()

                if event.key == pygame.K_LEFT:
                    piece.move_left()

                if event.key == pygame.K_DOWN:
                    try:
                        piece.move_down()

                    except IndexError:
                        piece.lock()
                        LOCKED_SOUNDEFFECT.play()

                if event.key == pygame.K_SPACE:
                    piece.rotate()
                    ROTATION_SOUNDEFFECT.play().set_volume(0.1)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_DOWN]:
            pygame.time.wait(15)
            try:
                piece.move_down()
            except IndexError:
                piece.lock()
                LOCKED_SOUNDEFFECT.play().set_volume(0.3)

        if chrono in range(0, 10000, LEVEL[level]):
            try:
                piece.move_down()
            except IndexError:
                piece.lock()
                LOCKED_SOUNDEFFECT.play().set_volume(0.3)

        piece.refresh()

        pygame.display.flip()

    pygame.quit()

    print("Game-Overrrrrrr")

if __name__ == "__main__":
    main()
