# importing pygame
import pygame

# initialize pygame
pygame.init()

# constants for screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# setting the display size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# setting the main window icon and caption
icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("LearnPyGame")

# game loop control variable
run = True

while run:
    # going through event queue
    for event in pygame.event.get():
        # if close window button is clicked we stop the game
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill((255, 255, 255))
    pygame.display.flip()

# uninitialize pygame
pygame.quit()