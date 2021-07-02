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
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.type = "PLAYER"
    
    # function that updates state of player
    # based on keys pressed
    def update(self, pressed_keys):
        # depending on arrow keys pressed, player will move
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)   
        
        # this keeps player on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# enemy class that extends sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)
        self.type = "ENEMY"
    
    # enemy object has job to start from right edge of screen to left
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.kill()
    
# pygame clock
clock = pygame.time.Clock()     

# setting the display size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# setting the main window icon and caption
icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("LearnPyGame")

# creating custom event for enemies to act
# we want enemies to be added at regular intervals
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# instantiating player object
player = Player()

# creating sprite groups
enemies = pygame.sprite.Group() # groups of all enemies
all_sprites = pygame.sprite.Group() # groups of all entities on field
all_sprites.add(player) # adding players to the main group

# game loop control variable
run = True

while run:
    # going through event queue
    for event in pygame.event.get():
        # if close window button is clicked we stop the game
        if event.type == pygame.QUIT:
            run = False

        # Add a new enemy ?
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # fill screen with black
    screen.fill(BLACK)

    # get all keys pressed in current frame, for player
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # blit every entity in sprite group onto screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # check if player collides any enemy
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        run = False

    # update the position of all enemies
    enemies.update()

    # update all the changes made in that iteration
    # or after the previous flip
    pygame.display.flip()

    # setting tick rate for processing of each frame
    clock.tick(60)

# uninitialize pygame
pygame.quit()
