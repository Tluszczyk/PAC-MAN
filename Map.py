import Wall
import Point
import Boost
import random
from settings import blocksize

class Map:
    def __init__(self):
        self.walls = []
        self.planche = [[]]
        self.points = []
        self.boosts = []
        self.ghostsSpawnPoints = []
        self.pacManSpawnPoint = []
        self.blinkySpawnPoint = []

        # bodyF = open("/Users/tluszczyk/Desktop/Python/PycharmProjects/PAC-MAN/resources/map", "r")
        bodyF = open("/Users/tluszczyk/Desktop/Python/PycharmProjects/PAC-MAN/resources/test_map", "r")

        self.pos = [0, 0]

        w, x, y = 0, 0, 0
        for line in bodyF.readlines():
            for elem in line:
                if elem != '\n':
                    self.planche[y].append([x, y] if elem != '1' else [-1, -1])

                if elem == '*':
                    self.boosts.append(Boost.Boost((x, y)))
                elif elem == '1':
                    self.walls.append(Wall.Wall((x, y)))
                elif elem == '.':
                    self.points.append(Point.Point((x, y)))
                elif elem == 'G':
                    self.ghostsSpawnPoints.append([x, y])
                elif elem == 'B':
                    self.blinkySpawnPoint = [x, y]
                elif elem == 'P':
                    self.pacManSpawnPoint = [x, y];
                x += 1
            y += 1
            self.planche.append([])
            w=x
            x=0

        self.size = [w*blocksize[0], y*blocksize[1]]

    def obtain_ghost_spawn_point(self):
        return self.ghostsSpawnPoints.pop(random.randint(0, len(self.ghostsSpawnPoints)-1))