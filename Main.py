import pygame
import PacMac
import Map
import Dijistra
from Directions import *
from settings import *
from Ghsots import Blinky, Pinky, Inky, Clyde
import Score
import Menu

pygame.init()


def game():
    labirynt = Map.Map()

    pacMan = PacMac.PacMan(labirynt.pacManSpawnPoint, resolution)

    blinky = Blinky.Blinky(labirynt.blinkySpawnPoint)
    pinky = Pinky.Pinky(labirynt.obtain_ghost_spawn_point())
    inky = Inky.Inky(labirynt.obtain_ghost_spawn_point())
    clyde = Clyde.Clyde(labirynt.obtain_ghost_spawn_point())

    Dijistra.create_graph(labirynt, [blinky, pinky, inky, clyde])

    blinky.addPacPos(pacMan.pos)

    menu = Menu.Menu(resolution)

    ghosts = [blinky, pinky, inky, clyde]

    clock.tick()

    score = Score.Score((0, 0))
    stop = True
    gameOn = True

    while gameOn:
        #EVENTS

        for event in pygame.event.get():
            if stop:
                if event.type == pygame.MOUSEMOTION:
                    menu.start_button.set_mouse_pos(event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN and menu.start_button.is_clicked(event.pos):
                    stop = False

                if event.type == pygame.MOUSEMOTION:
                    menu.quit_button.set_mouse_pos(event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN and menu.quit_button.is_clicked(event.pos):
                    stop = False
                    gameOn = False
                    pygame.quit()
                    quit()


            if event.type == pygame.QUIT:
                gameOn = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop = not stop
                elif event.key == pygame.K_d:
                    pacMan.set_direction(RIGHT)
                elif event.key == pygame.K_s:
                    pacMan.set_direction(DOWN)
                elif event.key == pygame.K_a:
                    pacMan.set_direction(LEFT)
                elif event.key == pygame.K_w:
                    pacMan.set_direction(UP)

        if stop:
            screen.blit(image, (0, 0))

            for wall in labirynt.walls + labirynt.points + labirynt.boosts:
                screen.blit(wall.image, wall.pos)

            for ghost in ghosts:
                screen.blit(ghost.image, ghost.pos)

            screen.blit(pacMan.image, pacMan.pos)

            screen.blit(score.textSurface, score.pos)

            screen.blit(menu.image, (0, 0))
            screen.blit(menu.start_button.image, menu.start_button.pos)
            screen.blit(menu.quit_button.image, menu.quit_button.pos)

            pygame.display.update()
            clock.tick()
            continue

            #MOVES
        try:

                #PACMAN
            pacMan.move(labirynt)
            pacMan.score(labirynt, score)
            pacMan.boost(labirynt, ghosts)

                #BLINKY
            blinky.addPacPos(pacMan.pos)
            blinky.move(labirynt)

                #CLYDE
            clyde.move(labirynt)

                #INKY
            inky.move(pacMan.pos, [blinky, pinky, clyde], labirynt)

                #PINKY
            pinky.move(pacMan.pos, [blinky, inky, clyde], labirynt)

        except:
            break

        for ghost in ghosts:
            if pacMan.pos == ghost.pos:
                if ghost.run:
                    ghost.pos = ghost.INIT_POS
                else:
                    gameOn = False
        #DISPLAY

        screen.blit(image, (0, 0))

        for wall in labirynt.walls + labirynt.points + labirynt.boosts:
            screen.blit(wall.image, wall.pos)

        for ghost in ghosts:
            screen.blit(ghost.image, ghost.pos)

        screen.blit(pacMan.image, pacMan.pos)

        screen.blit(score.textSurface, score.pos)
        pygame.display.update()

        pygame.time.wait(1000 // FPS)
        clock.tick()

while True:
    game()

pygame.quit()
quit()
