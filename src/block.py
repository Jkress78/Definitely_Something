import pygame

class Block(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill([0,0,0])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 3

        pygame.draw.rect(self.image, [0,0,0], self.rect)

    def update(self):
        self.rect.y += self.change_y