import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (280, 210)
        self.life = 3
        self.speed = 10
        self.score = 0
        self.isJump = False
        self.jumpCount = 9

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -9:
                self.rect.centery -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.jumpCount = 9
                self.isJump = False
                self.rect.centery = 210

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        self.jump()
