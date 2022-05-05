import pygame
import random
import os
from icecream import ic

WIDTH, HEIGHT = 850, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Force")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 50

PLAYER_IMAGE = pygame.image.load(
    os.path.join('assets', 'player.png'))
PLAYER = pygame.transform.rotate(
    pygame.transform.scale(PLAYER_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)

ENEMY_IMAGE = pygame.image.load(
    os.path.join('assets', 'enemy.png'))
ENEMY = pygame.transform.rotate(
    pygame.transform.scale(ENEMY_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)

ASTEROID_IMAGE = pygame.image.load(
    os.path.join('assets', 'asteroid.png'))

def draw_grid():
    """
    generate grid that spaceships will be flying within
    """
    for x in range(SPACESHIP_WIDTH, WIDTH-SPACESHIP_WIDTH, SPACESHIP_WIDTH*2):
        for y in range(SPACESHIP_HEIGHT, HEIGHT-SPACESHIP_HEIGHT, SPACESHIP_HEIGHT*2):
            ASTERIOD = pygame.transform.rotate(ASTEROID_IMAGE, random.randint(1, 180))
            WIN.blit(ASTERIOD, (x, y))

def draw_background():

    WIN.fill(BLACK)

    draw_grid()

    pygame.display.update()


def draw_window(player, enemy):

    WIN.blit(PLAYER, (player.x, player.y))
    WIN.blit(ENEMY, (enemy.x, enemy.y))

    pygame.display.update()


def main():
    player = pygame.Rect(WIDTH - SPACESHIP_WIDTH, HEIGHT - SPACESHIP_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    enemy = pygame.Rect(0, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    draw_background()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # controls the speed at which the game will run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(player, enemy)

    
    pygame.quit()


# ensure that this file only executes if this py file is run directly
if __name__ == "__main__":
    main()