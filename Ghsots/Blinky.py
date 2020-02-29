import pygame
import random
from Directions import *
from settings import blocksize

class Blinky(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.size = blocksize
        self.pos = [pos[0] * self.size[0], pos[1] * self.size[1]]
        self.INIT_POS = self.pos

        self.image = pygame.Surface(self.size)
        self.color = (204, 33, 0)
        self.runColor = (53, 128, 46)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.run = False
        self.runTime = 0
        self.maxRunTime = 5

        self.direction = UP

        self.positions2B = []
        self.onTrack = False

    def addPacPos(self, pos):
        if len(self.positions2B) == 0 or self.positions2B[-1] != pos:
            self.positions2B.append([pos[0], pos[1]])

    def checkIfOnTrack(self):
        if self.pos in self.positions2B:
            self.onTrack = True
            lastIndex = [index for index, value in enumerate(self.positions2B) if value==self.pos][-1]
            self.positions2B = self.positions2B[lastIndex+1:]

    def run_away(self):
        self.run = True
        self.runTime = pygame.time.get_ticks()
        self.image.fill(self.runColor)

    def move(self, labirynt):
        if self.run:
            if pygame.time.get_ticks()-self.runTime >= 1000 * self.maxRunTime:
                self.run = False
                self.runTime = 0
                self.image.fill(self.color)
        else:
            self.checkIfOnTrack()

        if not self.onTrack or self.run:
            possible_moves = [RIGHT, DOWN, LEFT, UP]
            for wall in labirynt.walls:
                if [self.pos[0]-self.size[0], self.pos[1]] == wall.pos: possible_moves.remove(LEFT)
                if [self.pos[0] + self.size[0], self.pos[1]] == wall.pos: possible_moves.remove(RIGHT)
                if [self.pos[0], self.pos[1] - self.size[1]] == wall.pos: possible_moves.remove(UP)
                if [self.pos[0], self.pos[1] + self.size[1]] == wall.pos: possible_moves.remove(DOWN)

            self.direction = random.choice(possible_moves)
            self.pos[0] += self.direction[0]*self.size[0]
            self.pos[1] += self.direction[1]*self.size[1]

            if opposite(self.direction) in possible_moves:
                possible_moves.remove(opposite(self.direction))

            if self.pos[0] > labirynt.pos[0]+labirynt.size[0]-self.size[0]: self.pos[0] = labirynt.pos[0]
            elif self.pos[0] < labirynt.pos[0]: self.pos[0] = labirynt.pos[0]+labirynt.size[0]-self.size[0]
            elif self.pos[1] > labirynt.pos[1]+labirynt.size[1]-self.size[1]: self.pos[1] = labirynt.pos[1]
            elif self.pos[1] < labirynt.pos[1]: self.pos[1] = labirynt.pos[1]+labirynt.size[1] - self.size[1]
        else:
            self.pos = self.positions2B.pop(0)