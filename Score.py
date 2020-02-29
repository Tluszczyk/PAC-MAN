import pygame
from settings import blocksize

class Score(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.size = blocksize
        self.pos = [pos[0]*self.size[0], pos[1]*self.size[1]]

        self.value = 0

        self.font = pygame.font.SysFont('Comic Sans', 30)
        self.textSurface = self.font.render(str(self.value), True, (255, 255, 255))

    def scoreAPoint(self):
        self.value += 1
        self.textSurface = self.font.render(str(self.value), True, (255, 255, 255))

    def getTextSurface(self):
        return self.textSurface