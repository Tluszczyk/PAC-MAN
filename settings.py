import pygame as pg

gameOn = True
resolution = (1000, 800)
screen = pg.display.set_mode(resolution)

blocksize = [30, 30]

image = pg.Surface(resolution)
image.fill((0, 0, 0))

FPS = 3

clock = pg.time.Clock()