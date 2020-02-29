import pygame
from settings import blocksize

class Point(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.size = [5, 5]
        self.pos = [blocksize[0]*(pos[0]+0.5)-self.size[0]//2, blocksize[1]*(pos[1]+0.5)-self.size[1]//2]

        self.image = pygame.Surface(self.size)
        self.image.fill((223, 224, 161))
        self.rect = self.image.get_rect()