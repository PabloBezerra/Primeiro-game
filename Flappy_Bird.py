import pygame
from pygame.locals import *
from time import sleep

TELA_LAR = 400
TELA_ALT = 720
SPEED = 10
GRAVITY = 1
GAME_SPEED = 10
PISO_LAR = 2 * TELA_LAR
PISO_ALT = 100

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens = [pygame.image.load('bluebird-upflap.png').convert_alpha(),
                        pygame.image.load('bluebird-midflap.png').convert_alpha(),
                        pygame.image.load('bluebird-downflap.png').convert_alpha()]
        self.current_image = 0
        self.speed = SPEED
        self.image = pygame.image.load('bluebird-midflap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = TELA_LAR / 2
        self.rect[1] = TELA_ALT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        sleep(0.03)
        self.image = self.imagens[self.current_image]
        self.speed += GRAVITY
        self.rect[1] += self.speed


    def bump(self):
        self.speed = -SPEED


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('base.png')
        self.image = pygame.transform.scale(self.image, (PISO_LAR, PISO_ALT))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = TELA_ALT - PISO_ALT

    def update(self):
        self.rect[0] -= GAME_SPEED


def is_off_screen(sprite):
    return sprite.rect[0] < (sprite.rect[2])

pygame.init()
tela = pygame.display.set_mode((TELA_LAR, TELA_ALT))

BACKGROUND = pygame.image.load('backboard_day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (TELA_LAR, TELA_ALT))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(PISO_LAR * i)
    ground_group.add(ground)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()

    tela.blit(BACKGROUND, (0, 0))

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = Ground(PISO_LAR)
        ground_group.add(new_ground)

    bird_group.update()
    ground_group.update()

    bird_group.draw(tela)
    ground_group.draw(tela)

    pygame.display.update()
