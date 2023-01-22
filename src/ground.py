import pygame
from random import randint


class Houses(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 170

    def update(self, player):
        self.rect.x -= player.speed // 2

        if self.rect.x <= -550:
            self.rect.x = randint(900, 1500)


class SnowGround(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x = 0
        self.x2 = self.image.get_width()
        self.y = 200

    def update(self, player):
        self.x -= 5
        self.x2 -= 5
        if self.x <= self.image.get_width() * -1:
            self.x = self.image.get_width()
        if self.x2 <= self.image.get_width() * -1:
            self.x2 = self.image.get_width()
