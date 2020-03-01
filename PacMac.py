import pygame
from Directions import *
from settings import blocksize, RunSettings

class PacMan(pygame.sprite.Sprite):
    def __init__(self, pos, resolution):
        pygame.sprite.Sprite.__init__(self)

        self.resolution = resolution

        self.size = blocksize
        self.pos = [pos[0]*self.size[0], pos[1]*self.size[1]]
        self.direction = STOP

        self.image = pygame.Surface(self.size)
        self.image.fill((238, 255, 0))
        self.rect = self.image.get_rect()

        self.nextDircextion = STOP

        self.runSet = None

    def addRunSet(self, runSet):
        self.runSet = runSet

    def set_pos(self, pos):
        self.pos = pos

    def set_direction(self, direction):
        self.nextDircextion = direction

    def move(self, labirynt):
        bad = False
        for wall in labirynt.walls:
            if [self.pos[0]+self.nextDircextion[0]*self.size[0], self.pos[1]] == wall.pos or\
                [self.pos[0], self.pos[1]+self.nextDircextion[1]*self.size[1]] == wall.pos:
                bad = True
        for wall in labirynt.walls:
            if [self.pos[0]+self.direction[0]*self.size[0], self.pos[1]] == wall.pos or\
                [self.pos[0], self.pos[1]+self.direction[1]*self.size[1]] == wall.pos:
                self.direction = STOP

        if not bad: self.direction = self.nextDircextion

        self.pos[0] += self.direction[0] * self.size[0]
        self.pos[1] += self.direction[1]*self.size[1]

        if self.pos[0] > labirynt.pos[0]+labirynt.size[0]-self.size[0]: self.pos[0] = labirynt.pos[0]
        elif self.pos[0] < labirynt.pos[0]: self.pos[0] = labirynt.pos[0]+labirynt.size[0]-self.size[0]
        elif self.pos[1] > labirynt.pos[1]+labirynt.size[1]-self.size[1]: self.pos[1] = labirynt.pos[1]
        elif self.pos[1] < labirynt.pos[1]: self.pos[1] = labirynt.pos[1]+labirynt.size[1] - self.size[1]

    def score(self, labirynt, score):
        i=0
        for point in labirynt.points:
            if pygame.Rect(self.pos, self.size).collidepoint(point.pos):
                score.score_a_point()
                labirynt.points.pop(i)
            i+=1

    def boost(self, labirynt, ghosts):
        i=0
        for boost in labirynt.boosts:
            if pygame.Rect(self.pos, self.size).collidepoint(boost.pos):
                self.runSet.runTime = pygame.time.get_ticks()
                self.runSet.run = True

                for ghost in ghosts:
                    ghost.run_away()

                labirynt.boosts.pop(i)
            i+=1

        if self.runSet.run:
            if pygame.time.get_ticks() - self.runSet.runTime >= 1000 * self.runSet.maxRunTime:
                self.runSet.run = False
                self.runSet.runTime = 0
                for ghost in ghosts:
                    ghost.chase()
