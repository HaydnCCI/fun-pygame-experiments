import pygame

HEIGHT, WIDTH = 800, 800
COLS, ROWS  = 8, 8
SQUARE_SIZE  = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# king piece
CROWN = pygame.transform.scale(pygame.image.load('checkers_set/assets/king_crown.png'), (44, 35))
