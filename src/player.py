import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        #--Player Pos--
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #--Player Speed--
        self.change_x = 0
        self.change_y = 0

        pygame.draw.rect(self.image, color, self.rect)
    

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    