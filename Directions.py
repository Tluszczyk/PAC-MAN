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