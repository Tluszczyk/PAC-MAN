import pygame
from Directions import *
import random
import Dijistra
from settings import blocksize


class Pinky(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.size = blocksize
        self.pos = [pos[0] * self.size[0], pos[1] * self.size[1]]
        self.INIT_POS = self.pos

        self.image = pygame.Surface(self.size)
        self.color = (244, 66, 226)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.destination = []
        self.shortest_path = []

        self.runSet = None

    def addRunSet(self, runSet):
        self.runSet = runSet

    def chase_PacMan(self, pacPos, ghosts, labirynt):
        self.graph = Dijistra.create_graph(labirynt, ghosts)
        self.shortest_path = Dijistra.shortest_path(self.pos, pacPos, self.graph)[1:]

    def move_at_random(self, labirynt):
        possible_moves = [RIGHT, DOWN, LEFT, UP]
        for wall in labirynt.walls:
            if [self.pos[0] - self.size[0], self.pos[1]] == wall.pos: possible_moves.remove(LEFT)
            if [self.pos[0] + self.size[0], self.pos[1]] == wall.pos: possible_moves.remove(RIGHT)
            if [self.pos[0], self.pos[1] - self.size[1]] == wall.pos: possible_moves.remove(UP)
            if [self.pos[0], self.pos[1] + self.size[1]] == wall.pos: possible_moves.remove(DOWN)

        self.direction = random.choice(possible_moves)
        self.pos[0] += self.direction[0] * self.size[0]
        self.pos[1] += self.direction[1] * self.size[1]

        if opposite(self.direction) in possible_moves:
            possible_moves.remove(opposite(self.direction))

        if self.pos[0] > labirynt.pos[0] + labirynt.size[0] - self.size[0]:
            self.pos[0] = labirynt.pos[0]
        elif self.pos[0] < labirynt.pos[0]:
            self.pos[0] = labirynt.pos[0] + labirynt.size[0] - self.size[0]
        elif self.pos[1] > labirynt.pos[1] + labirynt.size[1] - self.size[1]:
            self.pos[1] = labirynt.pos[1]
        elif self.pos[1] < labirynt.pos[1]:
            self.pos[1] = labirynt.pos[1] + labirynt.size[1] - self.size[1]

    def run_away(self):
        self.image.fill(self.runSet.runColor)

    def chase(self):
        self.image.fill(self.color)

    def move(self, pacPos, ghosts, labirynt):
        if self.runSet.run:
            self.move_at_random(labirynt)
            return

        self.chase_PacMan(pacPos, ghosts, labirynt)

        if len(self.shortest_path) == 0:
            self.move_at_random(labirynt)
        else:
            self.pos = self.shortest_path.pop(0)
