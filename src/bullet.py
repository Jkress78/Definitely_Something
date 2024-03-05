import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.Surface([6,10])
        self.image.fill([255,0,0])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_y = 10

        pygame.draw.rect(self.image, [255,0,0], self.rect)

    def update(self):
        self.rect.y -= self.change_y