"""
Auteur : W1mdra_
Date : 03.10.2024
Version : Beta
Description : This game aims to navigate a spaceship and destroy flying objects or other spaceships.
"""

#  Importation
import pygame   # Pygame
from pygame import *

#  Variable
WEIGHT_SCREEN = 800  # Largeur de l'écran.
HEiGHT_SCREEN = 600  # Hauteur de l'écran.
versions = '0.1'  # Version du jeu.


#  Défini les commandes et la taille du vaisseau spatial.
class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
        super(Spaceship, self).__init__()
        # Vaisseau spatial en format test (Carré)
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 255, 255))

        # Vaisseau spatial en format jeu. (2D)
        #  self.surf = pygame.image.load("ressources/image/spaceship_base/spaceship.png").convert()
        #  self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            # print("TOP")
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            # print("DOWN")
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            # print("LEFT")
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            # print("RIGHT")
        if pressed_keys[K_SPACE]:
            if len(the_missile.sprites()) < 1:
                missile = Missile(self.rect.center)
                every_sprite.add(missile)
                the_missile.add(missile)

        #  Défini jusqu'a ou le vaisseau spatial peut bouger. (Limite de l'écran.)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WEIGHT_SCREEN:
            self.rect.right = WEIGHT_SCREEN
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEiGHT_SCREEN:
            self.rect.bottom = HEiGHT_SCREEN


#  Défini la taille et les commandes des missile.
class Missile(pygame.sprite.Sprite):

    def __init__(self, center_missile):
        super(Missile, self).__init__()

        # Missile en format test (Carré)
        self.surf = pygame.Surface((10, 10), RLEACCEL)
        self.surf.fill((255, 255, 255))

        # Missile en format jeu. (2D)
        #  self.surf = pygame.image.load("ressources/image/missile.png").convert()
        #  self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.surf.get_rect(center=center_missile)

    def update(self):
        self.rect.move_ip(20, 0)
        if self.rect.left > WEIGHT_SCREEN:
            self.kill()


#  class définissant un vaisseau ennemei.
class Ennemi(pygame.sprite.Sprite):
    def __init__(self):
        super(Ennemi, self).__init__()
        # Vaisseau spatial en format test (Carré)
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect()

#  Initialise l'extension pygame.
pygame.init()

#  Défini le nom de la page.
pygame.display.set_caption(f"Space Invasion {versions}")

#  Défini la taille de la page.
screen = pygame.display.set_mode([WEIGHT_SCREEN, HEiGHT_SCREEN])

#  Permet de définir le temp de mouvement du vaisseau spatial.
clock = pygame.time.Clock()

every_sprite = pygame.sprite.Group()
the_missile = pygame.sprite.Group()

#  Défini la classe en variable.
spaceship = Spaceship()
every_sprite.add(spaceship)

continu = True
while continu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continu = False

    screen.fill((0, 0, 0))

    #  Permet au vaisseau spatial de bouger.
    keyboard_touch = pygame.key.get_pressed()
    spaceship.update(keyboard_touch)
    the_missile.update()

    for my_sprite in every_sprite:
        screen.blit(my_sprite.surf, my_sprite.rect)  # Défini la taille du vaisseau spatial.

    pygame.display.flip()

    #  Défini le temp de mouvement du vaisseau spatial.
    clock.tick(30)

#  Ferme la page.
pygame.quit()
