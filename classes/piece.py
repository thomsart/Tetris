import random

from settings import *
from .brick import *



class Piece:
    """
    Each piece is composed of several bricks.
    """

    def __init__(self):
        self.bricks = random.choice(
            [
                [Brick(2, 4, "blue"), Brick(2, 5, "blue") , Brick(2, 6, "blue"), Brick(1, 4, "blue")], # L
                [Brick(2, 4, "green"), Brick(2, 5, "green") , Brick(2, 6, "green"), Brick(1, 6, "green")], # L
                [Brick(2, 4, "red"), Brick(2, 5, "red") , Brick(1, 5, "red"), Brick(1, 6, "red")], # S
                [Brick(1, 4, "yellow"), Brick(1, 5, "yellow") , Brick(2, 5, "yellow"), Brick(2, 6, "yellow")], # S
                [Brick(2, 4, "purple"), Brick(2, 5, "purple") , Brick(2, 6, "purple"), Brick(1, 5, "purple")], # podium
                [Brick(2, 4, "brown"), Brick(2, 5, "brown") , Brick(2, 6, "brown"), Brick(2, 7, "brown")], # stick
                [Brick(2, 4, "pink"), Brick(2, 5, "pink") , Brick(1, 4, "pink"), Brick(1, 5, "pink")] # square
            ]
        )
        self.pivot = self.bricks[1]

    def put_aside(self):

        self.rotate()
        for brick in self.bricks:
            brick.position = (brick.position[0] + 210, brick.position[1] + 300)

    def remove_back_to_init(self):

        self.rotate_back()
        for brick in self.bricks:
            brick.refresh_position()
        
    def is_move_possible(self, dir):

        for brick in self.bricks:
            if dir == "down":
                if brick.row + 1 not in range(ROW):
                    return False
            if dir == "right":
                if brick.column + 1 not in range(COLUMN):
                    return False
            if dir == "left":
                if brick.column - 1 not in range(COLUMN):
                    return False

    def move_up(self):
        for brick in self.bricks:
            brick.row -= 1
            brick.refresh_position()

    def move_down(self):
        if self.is_move_possible("down") != False:
            for brick in self.bricks:
                brick.row += 1
                brick.refresh_position()
            for brick in self.bricks:
                if pygame.sprite.spritecollideany(brick, BLOCKED_BRICKS):
                    self.move_up()
                    raise IndexError
        else:
            raise IndexError

    def move_right(self):
        if self.is_move_possible("right") != False:
            for brick in self.bricks:
                brick.column += 1
                brick.refresh_position()
            for brick in self.bricks:
                if pygame.sprite.spritecollideany(brick, BLOCKED_BRICKS):
                    self.move_left()

    def move_left(self):
        if self.is_move_possible("left") != False:
            for brick in self.bricks:
                brick.column -= 1
                brick.refresh_position()
            for brick in self.bricks:
                if pygame.sprite.spritecollideany(brick, BLOCKED_BRICKS):
                    self.move_right()

    def is_rotation_possible(self):

        # verification de la collision non faite
        new_position = []
        for brick in self.bricks:
            if brick == self.pivot:
                continue
            else:
                new_row = self.pivot.row - self.pivot.column + brick.column
                new_column = self.pivot.column + self.pivot.row - brick.row
                if new_row not in range(ROW) or new_column not in range(COLUMN):
                    return False
                else:
                    new_position.append((new_row, new_column))

        return new_position

    def rotate_back(self):

        for brick in self.bricks:
            if brick == self.pivot:
                continue
            else:
                new_row = - brick.column + self.pivot.column + self.pivot.row
                new_column = brick.row - self.pivot.row + self.pivot.column 
                brick.row = new_row
                brick.column = new_column
                brick.refresh_position()

    def rotate(self):

        new_position = self.is_rotation_possible()
        come_back = False

        if new_position:
            index = 0
            for brick in self.bricks:
                if brick == self.pivot:
                    continue
                else:
                    brick.row = new_position[index][0]
                    brick.column = new_position[index][1]
                    brick.refresh_position()
                    if pygame.sprite.spritecollideany(brick, BLOCKED_BRICKS):
                        come_back = True
                index += 1

        if come_back:
            self.rotate_back()

    def refresh(self):

        for brick in self.bricks:
            WIND.blit(brick.image, brick.position)

    def lock(self):

        for brick in self.bricks:
            BLOCKED_BRICKS.add(brick)
            FREE_BRICK.remove(brick)
        BLOCKED_BRICKS.update()
        FREE_BRICK.update()

    def is_locked(self):

        if BLOCKED_BRICKS.has(self.bricks):
            return True
        else:
            return False

    def add_points(self, level):

        rows_to_free = []
        checked_rows = []
        points = 0

        for brick in self.bricks:
            count = 0
            if not brick.row in checked_rows:
                checked_rows.append(brick.row)
                for bricks in BLOCKED_BRICKS:
                    if bricks.row == brick.row:
                        count += 1
                        if count == 10:
                            rows_to_free.append(brick.row)

        if rows_to_free != []:

            rows_to_free.sort()

            if len(rows_to_free) == 4:
                JACKPOT_SOUNDEFFECT.play().set_volume(0.1)
            else:
                LINE_FREE_SOUNDEFFECT.play().set_volume(0.1)

            multiples = {1: 1, 2: 2, 3: 5, 4: 10}
            multiple = multiples[len(rows_to_free)]
            # First we remove all bricks of the lines to free
            for brick in BLOCKED_BRICKS:
                if brick.row in rows_to_free:
                    BLOCKED_BRICKS.remove(brick)
                    BLOCKED_BRICKS.update()
                    points += level

            for each_row in rows_to_free:
                for brick in BLOCKED_BRICKS:
                    if brick.row < each_row:
                        brick.row += 1
                        brick.refresh_position()

            points = points * multiple

        return points
    
    def is_drowned(self):

        for brick in self.bricks:
            if brick.row < 1:
                return True
