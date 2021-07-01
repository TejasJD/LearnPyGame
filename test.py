# importing pygame
import pygame

# initialize pygame
pygame.init()

# constants for screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# creating a Player class extending Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # inherit and initialize super class
        super().__init__()
        # player surface object
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(WHITE)
        # player rect
        self.rect = self.surf.get_rect()


# setting the display size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# setting the main window icon and caption
icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("LearnPyGame")

# instantiate player object
player = Player()

# game loop control variable
run = True

while run:
    # going through event queue
    for event in pygame.event.get():
        # if close window button is clicked we stop the game
        if event.type == pygame.QUIT:
            run = False
    # fill screen with black
    screen.fill(BLACK)

    # blit the player onto the screen
    screen.blit(player.surf, player.rect)

    # update all the changes made in that iteration
    # or after the previous flip
    pygame.display.flip()

# uninitialize pygame
pygame.quit()