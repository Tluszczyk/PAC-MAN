RIGHT = [1, 0]
DOWN = [0, 1]
LEFT = [-1, 0]
UP = [0, -1]
STOP = [0, 0]


def opposite(direction):
        if direction == RIGHT: return LEFT
        elif direction == DOWN: return UP
        elif direction == LEFT: return RIGHT
        elif direction == UP: return DOWN


def will_collide(pos1, dir1, pos2, dir2):
        if dir1 == opposite(dir2) and pos1[0]+dir1[0] == pos2[0] and pos1[1]+dir1[1] == pos2[1]:
                return True


def get_direction(pos1, pos2):
        return [pos1[0]-pos2[0], pos1[1]-pos2[1]]
