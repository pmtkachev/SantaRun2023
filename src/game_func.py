import pygame
from time import sleep
from random import randint
import src.resources as res
from src.items import Button, Spikes, Toy
from src.player import Player
from src.ground import Houses, SnowGround
import sys

pygame.init()

items = pygame.sprite.Group()
snd_channel = pygame.mixer.Channel(2)
jump_channel = pygame.mixer.Channel(3)


def check_events(button_play=None, button_credits=None, button_quit=None,
                 button_home=None, param='menu', player=None):
    for event in pygame.event.get():
        if param == 'menu':
            button_play.check_button(event)
            button_credits.check_button(event)
            button_quit.check_button(event)

            if button_play.clicked:
                res.sounds['click'].play()
                button_play.clicked = False
                return 'start_game'

            if button_credits.clicked:
                res.sounds['click'].play()
                button_credits.clicked = False
                return 'credits'

            if button_quit.clicked:
                res.sounds['click'].play()
                sleep(0.2)
                pygame.quit()
                sys.exit()

        elif param == 'game':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'game_over'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not player.isJump:
                    jump_channel.play(res.sounds['jump'])
                    return 'jump'

        elif param == 'game_over':
            button_play.check_button(event)
            button_home.check_button(event)
            if button_play.clicked:
                res.sounds['click'].play()
                button_play.clicked = False
                return 'start_game'
            if button_home.clicked:
                res.sounds['click'].play()
                button_home.clicked = False
                return 'home'


def draw_menu(window, fps):
    button_play = Button(res.button_image['play'], 350, 150)
    button_credits = Button(res.button_image['credits'], 350, 200)
    button_quit = Button(res.button_image['quit'], 350, 250)
    while True:
        window.blits(blit_sequence=((res.images['splash'], (0, 0)),
                                    (button_play.image, button_play.rect),
                                    (button_credits.image, button_credits.rect),
                                    (button_quit.image, button_quit.rect)))
        event = check_events(button_play, button_credits, button_quit)
        if event == 'start_game':
            start_game(window, fps)
        elif event == 'credits':
            show_credits(window)
        pygame.display.flip()


def start_game(window, fps):
    fnt = pygame.font.Font('fnt/fnt.ttf', 30)
    player = Player(res.images['player'])
    background = res.images['background']
    hud = res.images['hud']
    spikes = Spikes(res.images['spikes'])
    toys = Toy(res.images['toys'])
    houses = Houses(res.images['houses'])
    snow_ground = SnowGround(res.images['snow_ground'])
    items.add([houses, spikes, toys])
    while True:
        score_count = fnt.render(f'{player.score}', True, (255, 255, 255))
        window.blits(blit_sequence=((background, (0, 0)),
                                    (snow_ground.image, (snow_ground.x, snow_ground.y)),
                                    (snow_ground.image, (snow_ground.x2, snow_ground.y)),
                                    (hud, (0, 10))))
        items.draw(window)
        window.blits(blit_sequence=((score_count, (100, 20)),
                                    (player.image, player.rect)))
        draw_lives(window, player)
        update_game(window, fps, player, snow_ground, spikes, toys, score_count)


def draw_lives(window, player):
    life = res.images['life']
    x = 560
    for i in range(player.life):
        window.blit(life, (x, 15))
        x += 45


# Обновления спрайтов
def update_game(window, fps, player, snow_ground, spikes, toys, score_count):
    for i in range(50):
        pygame.draw.circle(window, (255, 255, 255),
                           (randint(0, 700),
                            randint(0, 300)), randint(1, 3))
    event = check_events(param='game', player=player)
    if event == 'jump':
        player.isJump = True
    elif event == 'game_over':
        game_over(window, score_count, fps)
    player.update()
    snow_ground.update(player)
    items.update(player)

    if pygame.sprite.collide_mask(player, spikes):
        spikes.rect.left = randint(700, 820)
        snd_channel.play(res.sounds['spike'])
        player.life -= 1

    if pygame.sprite.collide_mask(player, toys):
        snd_channel.play(res.sounds['get_toy'])
        toys.image = toys.images[randint(0, 6)]
        toys.rect.center = (randint(700, 900), randint(130, 190))
        player.score += 10
        if player.score % 50 == 0:
            player.speed += 2

    if player.life <= 0:
        game_over(window, score_count, fps)

    fps.tick(25)
    pygame.display.flip()


def game_over(window, score_count, fps):
    items.empty()
    button_play_ic = Button(res.button_image['play_ic'], 650, 250)
    button_home_ic = Button(res.button_image['home'], 50, 250)
    while True:
        window.blits(blit_sequence=((res.images['game_over'], (0, 0)),
                                    (score_count, (357, 192)),
                                    (button_play_ic.image, button_play_ic.rect),
                                    (button_home_ic.image, button_home_ic.rect)))
        event = check_events(param='game_over', button_play=button_play_ic,
                             button_home=button_home_ic)
        if event == 'start_game':
            start_game(window, fps)
        elif event == 'home':
            draw_menu(window, fps)
        pygame.display.flip()


def show_credits(window):
    flag = True
    while flag:
        window.blit(res.images['credits'], (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    flag = False
        pygame.display.flip()
