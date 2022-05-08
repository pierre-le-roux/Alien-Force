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
    asteroids = []
    for x in range(SPACESHIP_WIDTH, WIDTH-SPACESHIP_WIDTH, SPACESHIP_WIDTH*2):
        for y in range(SPACESHIP_HEIGHT, HEIGHT-SPACESHIP_HEIGHT, SPACESHIP_HEIGHT*2):
            asteroids.append(pygame.Rect(x, y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
    return asteroids


ASTEROIDS = draw_grid()

def draw_window(player, player_rotation, enemy, enemy_rotation):

    WIN.fill(BLACK)
    for asteroid in ASTEROIDS:
        WIN.blit(ASTEROID_IMAGE, (asteroid.x, asteroid.y))
        
    WIN.blit(pygame.transform.rotate(PLAYER, player_rotation), (player.x, player.y))
    WIN.blit(pygame.transform.rotate(ENEMY, enemy_rotation), (enemy.x, enemy.y))

    pygame.display.update()

def movement(keys_pressed, rotation, player, enemy=False):
    if enemy:
        if keys_pressed[pygame.K_a] and player.x - VEL >= 0: # LEFT
            player.x -= VEL
            rotation = 270
        if keys_pressed[pygame.K_d] and player.x + SPACESHIP_WIDTH + VEL <= WIDTH: # RIGHT
            player.x += VEL
            rotation = 90
        if keys_pressed[pygame.K_w] and player.y - VEL >= 0: # UP
            player.y -= VEL
            rotation = 180
        if keys_pressed[pygame.K_s] and player.y + SPACESHIP_HEIGHT + VEL <= HEIGHT: # DOWN
            player.y += VEL
            rotation = 0
    else:
        if keys_pressed[pygame.K_LEFT] and player.x - VEL >= 0: # LEFT
            player.x -= VEL
            rotation = 0
        if keys_pressed[pygame.K_RIGHT] and player.x + SPACESHIP_WIDTH + VEL <= WIDTH: # RIGHT
            player.x += VEL
            rotation = 180
        if keys_pressed[pygame.K_UP] and player.y - VEL >= 0: # UP
            player.y -= VEL
            rotation = 270
        if keys_pressed[pygame.K_DOWN] and player.y  + SPACESHIP_HEIGHT + VEL <= HEIGHT: # DOWN
            player.y += VEL
            rotation = 90

    if collide(player):
        if enemy:
            if keys_pressed[pygame.K_a] and player.x - VEL >= 0: # LEFT
                player.x += VEL
                rotation = 0
            if keys_pressed[pygame.K_d] and player.x + SPACESHIP_WIDTH + VEL <= WIDTH: # RIGHT
                player.x -= VEL
                rotation = 180
            if keys_pressed[pygame.K_w] and player.y - VEL >= 0: # UP
                player.y += VEL
                rotation = 270
            if keys_pressed[pygame.K_s] and player.y + SPACESHIP_HEIGHT + VEL <= HEIGHT: # DOWN
                player.y -= VEL
                rotation = 90
        else:
            if keys_pressed[pygame.K_LEFT] and player.x - VEL >= 0: # LEFT
                player.x += VEL
                rotation = 0
            if keys_pressed[pygame.K_RIGHT] and player.x + SPACESHIP_WIDTH + VEL <= WIDTH: # RIGHT
                player.x -= VEL
                rotation = 180
            if keys_pressed[pygame.K_UP] and player.y - VEL >= 0: # UP
                player.y += VEL
                rotation = 270
            if keys_pressed[pygame.K_DOWN] and player.y  + SPACESHIP_HEIGHT + VEL <= HEIGHT: # DOWN
                player.y -= VEL
                rotation = 90

    return rotation
        

def collide(player):
    collision = False

    for asteroid in ASTEROIDS:
        if asteroid.colliderect(player):
            collision = True
            break

    return collision

def main():
    player = pygame.Rect(WIDTH - SPACESHIP_WIDTH, HEIGHT - SPACESHIP_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    enemy = pygame.Rect(0, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    player_rotation = 0
    enemy_rotation = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # controls the speed at which the game will run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        player_rotation = movement(keys_pressed, player_rotation, player)
        enemy_rotation = movement(keys_pressed, enemy_rotation, enemy, True)

        draw_window(player, player_rotation, enemy, enemy_rotation)

    pygame.quit()


# ensure that this file only executes if this py file is run directly
if __name__ == "__main__":
    main()