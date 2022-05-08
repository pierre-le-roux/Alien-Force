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
    PLAYER = pygame.transform.rotate(PLAYER, player_rotation)
    WIN.blit(PLAYER, (player.x, player.y))
    WIN.blit(pygame.transform.rotate(ENEMY, enemy_rotation), (enemy.x, enemy.y))

    pygame.display.update()

def movement(keys_pressed, direction_current, player, enemy=False):
    direction_new = direction_current
    if enemy:
        if keys_pressed[pygame.K_a] and player.x - VEL >= 0: # LEFT
            player.x -= VEL
            direction_new = [1, 0, 0]
        if keys_pressed[pygame.K_d] and player.x + SPACESHIP_WIDTH + VEL <= WIDTH: # RIGHT
            player.x += VEL
            direction_new = [0, 0, 1]
        if keys_pressed[pygame.K_w] and player.y - VEL >= 0: # UP
            player.y -= VEL
            direction_new = [0, 1, 0]
        if keys_pressed[pygame.K_s] and player.y + SPACESHIP_HEIGHT + VEL <= HEIGHT: # DOWN
            player.y += VEL
            direction_new = [0, 0, 0]
    else:
        if keys_pressed[pygame.K_LEFT] and player.x - VEL >= 0: # LEFT
            player.x -= VEL
            direction_new = [1, 0, 0]
        if keys_pressed[pygame.K_RIGHT] and player.x + SPACESHIP_WIDTH + VEL <= WIDTH: # RIGHT
            player.x += VEL
            direction_new = [0, 0, 1]
        if keys_pressed[pygame.K_UP] and player.y - VEL >= 0: # UP
            player.y -= VEL
            direction_new = [0, 1, 0]
        if keys_pressed[pygame.K_DOWN] and player.y  + SPACESHIP_HEIGHT + VEL <= HEIGHT: # DOWN
            player.y += VEL
            direction_new = [0, 0, 0]

    if collide(player):
        if enemy:
            if keys_pressed[pygame.K_a] and player.x - VEL >= 0: # LEFT
                player.x += VEL
                direction_new = [1, 0, 0]
            if keys_pressed[pygame.K_d] and player.x + SPACESHIP_WIDTH + VEL <= WIDTH: # RIGHT
                player.x -= VEL
                direction_new = [0, 0, 1]
            if keys_pressed[pygame.K_w] and player.y - VEL >= 0: # UP
                player.y += VEL
                direction_new = [0, 1, 0]
            if keys_pressed[pygame.K_s] and player.y + SPACESHIP_HEIGHT + VEL <= HEIGHT: # DOWN
                player.y -= VEL
                direction_new = [0, 0, 0]
        else:
            if keys_pressed[pygame.K_LEFT] and player.x - VEL >= 0: # LEFT
                player.x += VEL
                direction_new = [1, 0, 0]
            if keys_pressed[pygame.K_RIGHT] and player.x + SPACESHIP_WIDTH + VEL <= WIDTH: # RIGHT
                player.x -= VEL
                direction_new = [0, 0, 1]
            if keys_pressed[pygame.K_UP] and player.y - VEL >= 0: # UP
                player.y += VEL
                direction_new = [0, 1, 0]
            if keys_pressed[pygame.K_DOWN] and player.y  + SPACESHIP_HEIGHT + VEL <= HEIGHT: # DOWN
                player.y -= VEL
                direction_new = [0, 0, 0]

    return player_orientation(direction_current, direction_new)
        

def collide(player):
    collision = False

    for asteroid in ASTEROIDS:
        if asteroid.colliderect(player):
            collision = True
            break

    return collision

def player_orientation(direction_current, direction_new):
    '''
    [0, 0, 1] # right
    [1, 0, 0] # left
    [0, 1, 0] # up
    [0, 0, 0] # down
    '''
    if direction_current != direction_new:
        delta = [
            direction_current[0] - direction_new[0], 
            direction_current[1] - direction_new[1], 
            direction_current[2] - direction_new[2]
        ]

        if delta in [[0, 1, 0], [0, -1, 0], [1, 0, -1], [-1, 0, 1]]:
            rotation = 180

        elif delta in [[-1, 1, 0], [1, 0, 0], [0, 0, -1], [0, -1, 1]]:
            rotation = -90

        elif delta in [[0, 1, -1], [0, 0, 1], [-1, 0, 0], [1, -1, 0]]:
            rotation = 90

        direction = direction_new
    else:
        rotation = 0
        direction = direction_current

    return rotation, direction

def main():
    player = pygame.Rect(WIDTH - SPACESHIP_WIDTH, HEIGHT - SPACESHIP_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    enemy = pygame.Rect(0, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    player_dir = [1, 0, 0]
    enemy_dir = [0, 0, 0]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # controls the speed at which the game will run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        player_rotation, player_dir = movement(keys_pressed, player_dir, player)
        enemy_rotation, enemy_dir = movement(keys_pressed, enemy_dir, enemy, True)

        ic(player_rotation, player_dir)

        draw_window(player, player_rotation, enemy, enemy_rotation)


    
    pygame.quit()


# ensure that this file only executes if this py file is run directly
if __name__ == "__main__":
    main()