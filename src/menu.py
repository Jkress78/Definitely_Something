import pygame

class Menu():

    def __init__(self) -> None:
        self.name = "Block Shooter"
        self.win_size = [800, 600]

    def run(self, screen):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return -1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False
                        return 1
                    

            screen.fill([0,0,0])

            pygame.draw.rect(screen, [0,255,0], pygame.Rect(30, 30, 60, 60))

            pygame.display.flip()
