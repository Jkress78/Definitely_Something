import pygame
import game
import menu

pygame.init()

game_in = game.Game()
menu_in = menu.Menu()

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Game")

run = True

STATE = 0

while run:
    match STATE: 
        case -1:
            run = False
        case 0:
            STATE = menu_in.run(screen)
        case 1:
            STATE = game_in.run(screen)



pygame.quit()