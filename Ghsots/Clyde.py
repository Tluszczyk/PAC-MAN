import pygame
import random
from Directions import *
from settings import blocksize, RunSettings

class Clyde(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.size = blocksize
        self.pos = [pos[0] * self.size[0], pos[1] * self.size[1]]
        self.INIT_POS = self.pos

        self.image = pygame.Surface(self.size)
        self.color = (255, 161, 0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.direction = UP

        self.runSet = None

    def addRunSet(self, runSet):
        self.runSet = runSet

    def chase(self):
        self.image.fill(self.color)

    def run_away(self):
        self.image.fill(self.runSet.runColor)

    def move(self, labirynt):

        possible_moves = [RIGHT, DOWN, LEFT, UP]
        for wall in labirynt.walls:
            if [self.pos[0] - self.size[0], self.pos[1]] == wall.pos: possible_moves.remove(LEFT)
            if [self.pos[0] + self.size[0], self.pos[1]] == wall.pos: possible_moves.remove(RIGHT)
            if [self.pos[0], self.pos[1] - self.size[1]] == wall.pos: possible_moves.remove(UP)
            if [self.pos[0], self.pos[1] + self.size[1]] == wall.pos: possible_moves.remove(DOWN)

        if opposite(self.direction) in possible_moves:
            possible_moves.remove(opposite(self.direction))

        self.direction = random.choice(possible_moves)
        self.pos[0] += self.direction[0] * self.size[0]
        self.pos[1] += self.direction[1] * self.size[1]

        if self.pos[0] > labirynt.pos[0] + labirynt.size[0] - self.size[0]:
            self.pos[0] = labirynt.pos[0]
        elif self.pos[0] < labirynt.pos[0]:
            self.pos[0] = labirynt.pos[0] + labirynt.size[0] - self.size[0]
        elif self.pos[1] > labirynt.pos[1] + labirynt.size[1] - self.size[1]:
            self.pos[1] = labirynt.pos[1]
        elif self.pos[1] < labirynt.pos[1]:
            self.pos[1] = labirynt.pos[1] + labirynt.size[1] - self.size[1]