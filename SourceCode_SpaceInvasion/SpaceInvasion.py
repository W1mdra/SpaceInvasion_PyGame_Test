"""
Auteur : W1mdra_
Date : 03.10.2024
Version : test
Description :   Ce jeu consiste à naviguer un vaisseau spatial et
                détruire des objets volants ou d'autres vaisseaux spatiaux.
"""

# Importation des bibliothèques nécessaires.
import pygame   # Pygame pour la gesion graphique.
import random   # Random pour les éléments aléatoires.
from pygame import *

# Variable
#  Définition des dimensions de la fenêtre de jeu.
WEIGHT_SCREEN = 800  # Largeur de l'écran.
HEiGHT_SCREEN = 600  # Hauteur de l'écran.
# Version du jeu.
versions = '0.3'


# Class définissant le vaisseau spatial et ses mouvements.
class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
        super(Spaceship, self).__init__()
        # Représentation du vaisseau par un rectangle blanc pour la version de test.
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 255, 255))

        #  Définition des limites de déplacement du vaisseau.
        self.rect = self.surf.get_rect()

        # Variable d'état pour suivre les impressions.
        self.last_key = None
        # Variable d'état pour suivre les colisions dû bord du jeu.
        self.last_border = None

    def update(self, pressed_keys):
        # key = None  # Variable pour stocker la direction courante.
        # border = None
        # Mouvements du vaisseau en fonction des touches appuyées.
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
            # key = "Haut"
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
            # key = "Bas"
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
            # key = "Gauche"
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_SPACE]:
            if len(the_missile.sprites()) < 1:  # Limite à un missile à la fois.
                missile = Missile(self.rect.center)
                every_sprite.add(missile)
                the_missile.add(missile)
            # key = "Space"

        # Vérifie si une direction a changé et si c'est différent de la précédente.
        """if key and key != self.last_key:
            print(f"Touche : {key}")
            self.last_key = key"""

        # Limite les déplacements du vaisseau aux bords de l'écran.
        if self.rect.left < 0:
            self.rect.left = 0
            # border = "Bord Gauche"
        if self.rect.right > WEIGHT_SCREEN:
            self.rect.right = WEIGHT_SCREEN
            # border = "Bord Droite"
        if self.rect.top <= 0:
            self.rect.top = 0
            # border = "Bord Haut"
        if self.rect.bottom >= HEiGHT_SCREEN:
            self.rect.bottom = HEiGHT_SCREEN
            # border = "Bord Bas"

        # Vérifie qu'un bord a été toucher.
        """if border and border != self.last_border:
            print(f"Bord : {border}")
            self.last_border = border"""


# Class définissant les missiles.
class Missile(pygame.sprite.Sprite):

    def __init__(self, center_missile):
        super(Missile, self).__init__()

        # Représentation du missile par un rectangle blanc.
        self.surf = pygame.Surface((10, 10), RLEACCEL)
        self.surf.fill((255, 255, 255))

        # Définition des limites de déplacement des missiles.
        self.rect = self.surf.get_rect(center=center_missile)

    def update(self):
        # Déplacement du missile vers la droite.
        self.rect.move_ip(20, 0)
        #  Si le missile sort de l'écran, on le supprime.
        if self.rect.left > WEIGHT_SCREEN:
            self.kill()


# class définissant un vaisseau ennemei.
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()
        # Représentation de l'ennemi par un rectangle blanc.
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 255, 255))

        # Placement initial de l'ennemi à droite de l'écran.
        self.rect = self.surf.get_rect(
            center=(
                WEIGHT_SCREEN + 50,
                random.randint(0, HEiGHT_SCREEN)
            )
        )
        # Vitesse aléatoire de l'ennemi, entre 5 et 20.
        self.speed = random.randint(5, 20)

    def update(self):
        # Déplacement de l'ennemi vers la gauche.
        self.rect.move_ip(-self.speed, 0)
        # Si l'ennemi sort de l'écran, on le supprime.
        if self.rect.right < 0:
            self.kill()


# Classe définissant une explosion.
class Explosion(pygame.sprite.Sprite):
    #  Score du jeu défini à 0.
    Score = 0

    def __init__(self, center_spaceship):
        super(Explosion, self).__init__()
        # L'explosion dure 10 cycles.
        self._compteur = 10
        self.surf = pygame.Surface((70, 70))
        self.surf.fill((255, 255, 255))

        # Placement de l'explosion au centre de l'impact.
        self.rect = self.surf.get_rect(center=center_spaceship)

        # Variable pour savoir si "Boom!" a déjà été affiché.
        self._boom = False

    def update(self):
        # Si le message n'a pas encore été affiché.
        if not self._boom:
            print("Boom!")
            self._boom = True

        # On décrémente le compteur de l'explosion.
        self._compteur -= 1

        # Quand le compteur atteint 0, on supprime l'explosion.
        if self._compteur == 0:
            self.kill()


pygame.font.init()


# Class permettant d'afficher le score actuel.
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self._scoreCourant = 0
        self._setText()

    def _setText(self):
        self.surf = police_score.render(
            'Score: ' + str(self._scoreCourant), False,(255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(WEIGHT_SCREEN / 4, 15)
        )

    def update(self):
        self._setText()

    def increment(self, value):
        self._scoreCourant = self._scoreCourant + value


# Initialisation de font.
pygame.font.init()
# Police d'écriture pour le score.
police_score = pygame.font.SysFont('Arial', 30)

# Gestion de la vitesse de rafraichissement du jeu.dss
clock = pygame.time.Clock()

# Initialisation de pygame.
pygame.init()

# Nom de la fenêtre de jeu.
pygame.display.set_caption(f"Space Invasion {versions}")

# Ajoute un ennemi toutes les 500 ms.
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 500)

# Taille de la fenêtre de jeu.
screen = pygame.display.set_mode([WEIGHT_SCREEN, HEiGHT_SCREEN])

# Groupe de sprites.
every_sprite = pygame.sprite.Group()
the_missile = pygame.sprite.Group()
the_enemy = pygame.sprite.Group()
the_explosion = pygame.sprite.Group()

# Création du vaisseau.
spaceship = Spaceship()
every_sprite.add(spaceship)
score = Score()
every_sprite.add(score)

continu = True
while continu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continu = False
        elif event.type == ADD_ENEMY:
            # Creation d'un nouvel ennemie.
            new_enemy = Enemy()
            the_enemy.add(new_enemy)
            every_sprite.add(new_enemy)

    # Couleur de fond noire (RVB).
    screen.fill((0, 0, 0))

    # Détection des collisions entre le vaisseau et les ennemis.
    if pygame.sprite.spritecollideany(spaceship, the_enemy):
        spaceship.kill()
        explosion = Explosion(spaceship.rect.center)
        the_explosion.add(explosion)
        every_sprite.add(explosion)
        continu = False

    # Détection des collisions entre les missiles et les ennemis.
    for missile in the_missile:
        touch_enemy_list = pygame.sprite.spritecollide(
            missile, the_enemy, True
        )
        if len(touch_enemy_list) > 0:
            missile.kill()
            score.increment(len(touch_enemy_list))
        for enemy in touch_enemy_list:
            explosion = Explosion(enemy.rect.center)
            the_explosion.add(explosion)
            every_sprite.add(explosion)

    # Mise à jour des touches pressées.
    keyboard_touch = pygame.key.get_pressed()

    # Mise a jour des éléments du jeu.
    spaceship.update(keyboard_touch)
    the_missile.update()
    the_enemy.update()
    the_explosion.update()
    score.update()

    # Affichage des sprites à l'écran.
    for my_sprite in every_sprite:
        screen.blit(my_sprite.surf, my_sprite.rect)

    # Rafraichissement de l'écran
    pygame.display.flip()

    # Limite de 30 images par seconde.
    clock.tick(30)

# Ajout du délai avant la fermeture de la fenêtre après avoir exploser.
pygame.time.delay(100)

# Fermeture de Pygame.
pygame.quit()
