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

    runSet = RunSettings(0, 10, False, (53, 128, 46))

    Dijistra.create_graph(labirynt, [blinky, pinky, inky, clyde])

    blinky.addPacPos(pacMan.pos)

    ghosts = [blinky, pinky, inky, clyde]

    pacMan.addRunSet(runSet)
    for ghost in ghosts:
        ghost.addRunSet(runSet)

    clock.tick()

    score = Score.Score((0, 0))
    menu = Menu.Menu(resolution, score)

    stop = True
    gameOn = True
    died = False

    while gameOn:
        #EVENTS

        for event in pygame.event.get():
            if stop or died:
                menu.score_out.update_score(score.value, score.highest_score)

                if event.type == pygame.MOUSEMOTION:
                    menu.start_button.set_mouse_pos(event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN and menu.start_button.is_clicked(event.pos):
                    stop = False
                    if died:
                        score.archive_score()
                        return

                if event.type == pygame.MOUSEMOTION:
                    menu.quit_button.set_mouse_pos(event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN and menu.quit_button.is_clicked(event.pos):
                    stop = False
                    gameOn = False
                    score.archive_score()
                    pygame.quit()
                    quit()


            if event.type == pygame.QUIT:
                score.archive_score()
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

        if stop or died:
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
            screen.blit(menu.score_out.image, menu.score_out.pos)

            pygame.display.update()
            clock.tick()
            continue

            #MOVES
        try:

                #PACMAN
            pacMan.move(labirynt)
            pacMan.score(labirynt, score)
            pacMan.boost(labirynt, ghosts)

        except:
            break

        for ghost in ghosts:
            if pacMan.pos == ghost.pos:
                if runSet.run:
                    ghost.pos = ghost.INIT_POS
                    score.score_ten_points()
                else:
                    menu.score_out.update_score(score.value, score.highest_score)
                    score.archive_score()
                    died = True

        try:
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
                if runSet.run:
                    ghost.pos = ghost.INIT_POS
                    score.score_ten_points()
                else:
                    menu.score_out.update_score(score.value, score.highest_score)
                    score.archive_score()
                    died = True
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
