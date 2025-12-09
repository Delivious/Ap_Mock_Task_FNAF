import pygame
import random
from Custom_Night_Menu import CN

pygame.init()
# all images used are from FNAF and owned by Scott Cawthon, no copyright intended, this is for educational purposes only.
# Fonts
font = pygame.font.SysFont('Arial', 72)
five = font.render('Five', True, (255, 255, 255))
nights = font.render('Nights', True, (255, 255, 255))
at = font.render('at', True, (255, 255, 255))
freddys = font.render("Freddy's", True, (255, 255, 255))
new_game = font.render('New Game', True, (255, 255, 255))
cont = font.render('Continue', True, (255, 255, 255))
arrows = font.render('>>', True, (255, 255, 255))

# Window
screen_width = 2500
screen_height = 1500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FNAF Menu")

# Images
freddy1 = pygame.image.load("freddy1.png")
freddy2 = pygame.image.load("freddy2.png")
freddy3 = pygame.image.load("freddy3.png")
freddy4 = pygame.image.load("freddy4.png")
freddy_list = [freddy1, freddy2, freddy3, freddy4]

clock = pygame.time.Clock()

# Menu selector state
whereat = 1
running = True

freddy_timer = 0
freddy_image = freddy1


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        whereat = 1
    if keys[pygame.K_DOWN]:
        whereat = 2

    # ENTER to select
    if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER] and whereat==1:
        running = False  # exit menu
        selected = CN()  # call Custom Night function
    elif keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER] and whereat==2:
        running = False  # exit menu
        # Placeholder for Continue function

    # ------------- Drawing ---------------
    screen.fill(BLACK)
    # Freddy animation
    freddy_timer += clock.get_time()
    if freddy_timer > 200:
        freddy_image = random.choice(freddy_list)
        freddy_timer = 0

    screen.blit(freddy_image, (500, 0))

    # Title text
    screen.blit(five, (125, 200))
    screen.blit(nights, (125, 300))
    screen.blit(at, (125, 400))
    screen.blit(freddys, (125, 500))
    screen.blit(new_game, (125, 650))
    screen.blit(cont, (125, 750))

    # Arrow indicator
    if whereat == 1:
        screen.blit(arrows, (30, 650))
    else:
        screen.blit(arrows, (30, 750))

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()  # close menu screen

CN()

pygame.quit()
# ^ Use of AI for pygame starter ^
# ^ slight inhance with AI to fix some problems ^