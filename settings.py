import pygame as pg

gameOn = True
resolution = (1000, 800)
screen = pg.display.set_mode(resolution)

blocksize = [30, 30]

image = pg.Surface(resolution)
image.fill((0, 0, 0))

FPS = 3

clock = pg.time.Clock()


class RunSettings:
    def __init__(self, t, m, r, c):
        self.runTime = t
        self.maxRunTime = m
        self.run = r
        self.runColor = c