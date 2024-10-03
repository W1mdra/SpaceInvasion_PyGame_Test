# https://www.youtube.com/watch?v=KFVUzwPBpX4&list=PLp3pYrjF9bCn-PqQnKfKlGK-jIffdbgKo&index=2
# 06:42

import pygame

pygame.init()

screen = pygame.display.set_mode([800, 600])

continu = True
while continu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continu = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (200, 200), 100)

    pygame.draw.rect(screen, (0, 0, 255), (400, 300, 100, 100))

    pygame.display.flip()

pygame.quit()
