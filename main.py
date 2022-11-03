import pygame
from pygame.locals import *

from settings import *
from classes.piece import *



def main():

    clock = pygame.time.Clock()
    clock.tick(FPS)
    chrono = 0
    pause = False
    play = True
    level = 0
    score = 0
    piece = Piece()

    while play:

        WIND.fill(WHITE)
        BLOCKED_BRICKS.draw(WIND)
        display_board()
        WIND.blit(TEXT.render(" Level:" + str(level), 5, (0, 0, 0)), (B * 12, B * 2))
        WIND.blit(TEXT.render("  Score:", 5, (0, 0, 0)), (B * 12, B * 4))
        WIND.blit(TEXT.render("  " + str(score), 5, (0, 0, 0)), (B * 12, B * 5))

        chrono += 1
        if chrono > 10000:
            chrono = 0

        if piece.is_locked():
            if piece.is_drowned():
                play = False
            else:
                score += piece.add_points(level)
                piece = Piece()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT and not pause:
                    piece.move_right()

                if event.key == pygame.K_LEFT and not pause:
                    piece.move_left()

                if event.key == pygame.K_DOWN and not pause:
                    try:
                        piece.move_down()
                    except IndexError:
                        piece.lock()
                        LOCKED_SOUNDEFFECT.play()

                if event.key == pygame.K_KP_PLUS:
                    if level == len(LEVEL) - 1:
                        pass
                    else:
                        level += 1


                if event.key == pygame.K_UP:
                    if pause:
                        pause = False
                    else:
                        pause = True

                if event.key == pygame.K_SPACE and not pause:
                    piece.rotate()
                    ROTATION_SOUNDEFFECT.play().set_volume(0.1)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_DOWN] and not pause:
            pygame.time.wait(15)
            try:
                piece.move_down()
            except IndexError:
                piece.lock()
                LOCKED_SOUNDEFFECT.play().set_volume(0.3)

        if chrono in range(0, 10000, LEVEL[level]) and not pause:
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
