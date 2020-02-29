import pygame
from settings import blocksize

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.size = blocksize
        self.pos = [pos[0]*self.size[0], pos[1]*self.size[1]]

        self.image = pygame.Surface(self.size)
        self.image.fill((0, 51, 135))
        self.rect = self.image.get_rect()