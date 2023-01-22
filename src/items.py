import pygame
from random import randint


class Toy(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (randint(500, 700), randint(130, 190))

    def update(self, player):
        self.rect.centerx -= player.speed
        if self.rect.right <= 0:
            self.rect.center = (randint(700, 900), randint(130, 190))
            self.image = self.images[randint(0, 6)]


class Spikes(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (randint(500, 700), 265)

    def update(self, player):
        self.rect.centerx -= player.speed
        if self.rect.right <= 0:
            self.rect.left = randint(700, 820)


class Button(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.clicked = False

    def check_button(self, event):
        x, y = pygame.mouse.get_pos()
        if not self.clicked:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.rect.collidepoint(x, y):
                        self.clicked = True
