import pygame

pygame.mixer.init()

images = {
    'background': pygame.image.load('img/background.png'),
    'splash': pygame.image.load('img/splash.png'),
    'snow_ground': pygame.image.load('img/snow_gr.png'),
    'houses': pygame.image.load('img/houses.png'),
    'player': [pygame.image.load(f'img/player/player_{i}.png') for i in range(11)],
    'spikes': pygame.image.load('img/spikes.png'),
    'toys': [pygame.image.load(f'img/toys/toy_{i}.png') for i in range(7)],
    'hud': pygame.image.load('img/hud.png'),
    'life': pygame.image.load('img/life.png'),
    'game_over': pygame.image.load('img/game_over.png'),
    'credits': pygame.image.load('img/credits.png')
}

button_image = {
    'play': pygame.image.load('img/buttons/play_btn.png'),
    'play_ic': pygame.image.load('img/buttons/play_btn_ico.png'),
    'credits': pygame.image.load('img/buttons/credits_btn.png'),
    'quit': pygame.image.load('img/buttons/quit_btn.png'),
    'home': pygame.image.load('img/buttons/home_btn_ico.png')
}

sounds = {
    'music': pygame.mixer.music.load('snd/music.mid'),
    'click': pygame.mixer.Sound('snd/click.mp3'),
    'get_toy': pygame.mixer.Sound('snd/toy.wav'),
    'jump': pygame.mixer.Sound('snd/jump.wav'),
    'spike': pygame.mixer.Sound('snd/spike.wav')
}
