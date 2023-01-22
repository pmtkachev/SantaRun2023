import pygame
from src import game_func as gf

window = pygame.display.set_mode((700, 300), flags=pygame.NOFRAME)

fps = pygame.time.Clock()


def run():
    pygame.mixer.music.play(-1)
    gf.draw_menu(window, fps)


if __name__ == '__main__':
    while True:
        run()
