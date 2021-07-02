# importing pygame
import pygame, random
from pygame.locals import *

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

    # function that updates state of player
    # based on keys pressed
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
            # if it goes out of bou
            if self.rect.top < 0:
                self.rect.top = 0
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
            if self.rect.left < 0:
                self.rect.left = 0
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)   
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

# enemy class that extends sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 50, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(1, 5)
    
    # enemy object has job to start from right edge of screen to left
    def update(self):
        self.rect.move_ip(-self.speed, 0)
    
        

# setting the display size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# setting the main window icon and caption
icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("LearnPyGame")

# instantiate player and enemy object (enemy object will be changed later)
player = Player()
enemy = Enemy()

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

    # get all keys pressed in current frame, for player
    pressed_keys = pygame.key.get_pressed()

    # update their states
    player.update(pressed_keys)
    enemy.update()

    # blit the game components onto the screen
    screen.blit(player.surf, player.rect)
    screen.blit(enemy.surf, enemy.rect)

    # update all the changes made in that iteration
    # or after the previous flip
    pygame.display.flip()

# uninitialize pygame
pygame.quit()
