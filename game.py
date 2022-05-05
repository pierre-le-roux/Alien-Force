import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Force")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

PLAYER_IMAGE = pygame.image.load(
    os.path.join('assets', 'player.png'))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (55, 43))

ENEMY_IMAGE = pygame.image.load(
    os.path.join('assets', 'enemy.png'))
ENEMY_IMAGE = pygame.transform.scale(ENEMY_IMAGE, (52, 55))

def draw_window():

    WIN.fill(WHITE)

    WIN.blit(PLAYER_IMAGE, (300, 100))

    pygame.display.update()




def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # controls the speed at which the game will run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    
    pygame.quit()


# ensure that this file only executes if this py file is run directly
if __name__ == "__main__":
    main()