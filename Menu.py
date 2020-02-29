import pygame

class StartButton(pygame.sprite.Sprite):
    def __init__(self, resolution):
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.SysFont('Comic Sans', 80)
        self.textSurface = self.font.render("Commence the game of PAC-MAN!", True, (255, 255, 255))

        self.pos = [dS//2 - dT//2 for dS, dT in zip(resolution, self.textSurface.get_size())]

        self.image = pygame.Surface([d+20 for d in self.textSurface.get_size()])
        self.image.fill((105, 105, 105))

        self.image.blit(self.textSurface, [dB//2-dT//2 for dB, dT in zip(self.image.get_size(),self.textSurface.get_size())])

        self.rect = pygame.Rect(self.pos, self.image.get_size())

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def set_mouse_pos(self, pos):
        if self.rect.collidepoint(pos):
            self.image.fill((80, 80, 80))
        else:
            self.image.fill((105, 105, 105))
        self.image.blit(self.textSurface, [dB // 2 - dT // 2 for dB, dT in zip(self.image.get_size(), self.textSurface.get_size())])

class QuitButton(pygame.sprite.Sprite):
    def __init__(self, resolution):
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.SysFont('Comic Sans', 80)
        self.textSurface = self.font.render("Quit the game", True, (255, 255, 255))

        self.pos = [dS // 2 - dT // 2 for dS, dT in zip(resolution, self.textSurface.get_size())]
        self.pos[1] += 100

        self.image = pygame.Surface([d + 20 for d in self.textSurface.get_size()])
        self.image.fill((105, 105, 105))

        self.image.blit(self.textSurface,
                        [dB // 2 - dT // 2 for dB, dT in zip(self.image.get_size(), self.textSurface.get_size())])

        self.rect = pygame.Rect(self.pos, self.image.get_size())

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def set_mouse_pos(self, pos):
        if self.rect.collidepoint(pos):
            self.image.fill((80, 80, 80))
        else:
            self.image.fill((105, 105, 105))
        self.image.blit(self.textSurface,
                        [dB // 2 - dT // 2 for dB, dT in zip(self.image.get_size(), self.textSurface.get_size())])

class Menu(pygame.sprite.Sprite):
    def __init__(self, resolution):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(resolution)
        self.image.fill((105, 105, 105))
        self.image.set_alpha(105)
        self.rect = self.image.get_rect()

        self.start_button = StartButton(resolution)
        self.quit_button = QuitButton(resolution)