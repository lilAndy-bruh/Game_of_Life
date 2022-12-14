import pygame
import sys
import time

from game import step
from game import print_grid
from game import insert_life
from game import BASE
from game import create_grid
from game import ALIVE, DEAD


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Grid Setup
grid = create_grid()
l1 = [15, 26, 34, 35, 36]
insert_life(grid, l1)
# grid = play(grid)
print_grid(grid, BASE)

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()


def pygame_step(grid, moving_sprites):
    moving_sprites.empty()
    for i in range(100):
        if grid[i] == ALIVE:
            j = i % BASE
            rectangle_tmp = Rectangle(j * BASE * BASE, (i-j) * BASE)
            moving_sprites.add(rectangle_tmp)
            print(i)
            print(j, " ", i-j)
            print()


# mainloop
"""i = 0
j = 0"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    """rectangle1.rect.topleft = [i, j*10]
    i += 1
    if i % 1000 == 0:
        i = 0
        j += 1
    print(i)"""

    pygame_step(grid, moving_sprites)
    grid = step(grid)

    screen.fill((0, 255, 255))
    moving_sprites.draw(screen)
    pygame.display.flip()

    # clock.tick(1000000)
    time.sleep(0.5)