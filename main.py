import pygame
from pygame.locals import *

from settings import *
from classes.piece import *


def main():

    clock = pygame.time.Clock()
    clock.tick(FPS)
    chrono = 0
    level = 0
    score = 0
    pause = False
    play = True

    piece = Piece()
    next_piece = Piece()
    next_piece.put_aside()

    while play:

        try:

            WIND.blit(PLAY_SURFACE, PLAY_RECT)
            WIND.blit(CONSOLE_SURFACE, CONSOLE_RECT)
            PLAY_SURFACE.fill(WHITE)
            CONSOLE_SURFACE.fill(WHITE)
            BLOCKED_BRICKS.draw(WIND)
            WIND.blit(TEXT.render("  Level:" + str(level), 5, (0, 0, 0)), (BRICK * 12, BRICK * 3))
            WIND.blit(TEXT.render("  Score:", 5, (0, 0, 0)), (BRICK * 12, BRICK * 5))
            WIND.blit(TEXT.render("  " + str(score), 5, (0, 0, 0)), (BRICK * 12, BRICK * 6))
            WIND.blit(TEXT.render("  Next", 5, (0, 0, 0)), (BRICK * 12, BRICK * 8))
            WIND.blit(TEXT.render("  piece:", 5, (0, 0, 0)), (BRICK * 12, BRICK * 9))

            chrono += 1
            if chrono > 10000:
                chrono = 0

            # If a piece is just locked we check if it's not drowned
            # if not we set the new score and increase the level in
            # function of the score.
            if piece.is_locked():
                if piece.is_drowned():
                    play = False
                else:
                    score += piece.add_points(POINT[level])
                    if score > LEVEL[level] * POINT[level] and level <= 9:
                        level += 1
                        BINGO_SOUNDEFFECT.play().set_volume(0.1)
                    piece = next_piece
                    piece.remove_back_to_init()
                    next_piece = Piece()
                    next_piece.put_aside()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    play = False

                if event.type == pygame.KEYDOWN:

                    # Move the piece to right.
                    if event.key == pygame.K_RIGHT and not pause:
                        piece.move_right()

                    # Move the piece to left.
                    if event.key == pygame.K_LEFT and not pause:
                        piece.move_left()

                    # Go down the piece.
                    if event.key == pygame.K_DOWN and not pause:
                        try:
                            piece.move_down()
                        except IndexError:
                            piece.lock()
                            LOCKED_SOUNDEFFECT.play()

                    # Increase the level.
                    if event.key == pygame.K_KP_PLUS:
                        if level == len(LEVEL) - 1:
                            pass
                        else:
                            level += 1

                    # Set the game in pause.
                    if event.key == pygame.K_UP:
                        if pause:
                            pause = False
                        else:
                            pause = True

                    # Rotate the piece.
                    if event.key == pygame.K_SPACE and not pause:
                        piece.rotate()
                        ROTATION_SOUNDEFFECT.play().set_volume(0.1)

            # Go down faster the piece.
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_DOWN] and not pause:
                pygame.time.wait(40)
                try:
                    piece.move_down()
                except IndexError:
                    piece.lock()
                    LOCKED_SOUNDEFFECT.play().set_volume(0.3)

            # We use the chrono to mark portion of times to make the piece
            # going down itself insted of doing pygame.time.wait() which
            # would considerably slowdown the game.
            if chrono in range(0, 10000, LEVEL[level]) and not pause:
                try:
                    piece.move_down()
                except IndexError:
                    piece.lock()
                    LOCKED_SOUNDEFFECT.play().set_volume(0.3)                

            piece.refresh()
            next_piece.refresh()

            if pause:
                WIND.blit(PAUSE, (BRICK * 5, BRICK * 8))

            pygame.display.update()

        except RecursionError:
            play = False

    # Game-over
    GAMEOVER_SOUNDEFFECT.play().set_volume(0.3)
    WIND.blit(TEXT.render("GAME OVER", 5, (0, 0, 0)), (BRICK * 4, BRICK * 8))
    pygame.display.flip()
    pygame.time.wait(5000)

    pygame.quit()


if __name__ == "__main__":
    main()
