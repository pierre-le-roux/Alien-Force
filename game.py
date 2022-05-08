from shutil import move
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
VEL = 5
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
            ASTERIOD = pygame.transform.rotate(ASTEROID_IMAGE, 0)
            WIN.blit(ASTERIOD, (x, y))

def draw_window(player, enemy):

    WIN.fill(BLACK)
    draw_grid()

    WIN.blit(PLAYER, (player.x, player.y))
    WIN.blit(ENEMY, (enemy.x, enemy.y))

    pygame.display.update()

def movement(keys_pressed, player, enemy=False):
    if enemy:
        if keys_pressed[pygame.K_LEFT]: # LEFT
            player.x -= VEL
        if keys_pressed[pygame.K_RIGHT]: # RIGHT
            player.x += VEL
        if keys_pressed[pygame.K_UP]: # UP
            player.y -= VEL
        if keys_pressed[pygame.K_DOWN]: # DOWN
            player.y += VEL
    else:
        if keys_pressed[pygame.K_a]: # LEFT
            player.x -= VEL
        if keys_pressed[pygame.K_d]: # RIGHT
            player.x += VEL
        if keys_pressed[pygame.K_w]: # UP
            player.y -= VEL
        if keys_pressed[pygame.K_s]: # DOWN
            player.y += VEL

def main():
    player = pygame.Rect(WIDTH - SPACESHIP_WIDTH, HEIGHT - SPACESHIP_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    enemy = pygame.Rect(0, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # controls the speed at which the game will run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, player)
        movement(keys_pressed, enemy, True)

        draw_window(player, enemy)

    
    pygame.quit()


# ensure that this file only executes if this py file is run directly
if __name__ == "__main__":
    main()