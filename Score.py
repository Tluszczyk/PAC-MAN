import pygame
from settings import blocksize
import os

class Score(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.size = blocksize
        self.pos = [pos[0]*self.size[0], pos[1]*self.size[1]]

        self.value = 0
        self.highest_score = 0

        self.font = pygame.font.SysFont('Comic Sans', 30)
        self.textSurface = self.font.render(str(self.value), True, (255, 255, 255))
        self.archive_score()

    def score_a_point(self):
        self.value += 1
        self.textSurface = self.font.render(str(self.value), True, (255, 255, 255))
        if self.value > self.highest_score:
            self.highest_score = self.value

    def score_ten_points(self):
        self.value += 10
        self.textSurface = self.font.render(str(self.value), True, (255, 255, 255))
        if self.value > self.highest_score:
            self.highest_score = self.value

    def archive_score(self):
        scoreF = open("/Users/tluszczyk/Desktop/Python/PycharmProjects/PAC-MAN/resources/highest_score", 'r+')
        hs = int(scoreF.readlines()[-1])
        if hs < self.highest_score:
            scoreF.write('\n'+str(self.highest_score))
            scoreF.close()
        else:
            self.highest_score = hs

    def get_text_surface(self):
        return self.textSurface
