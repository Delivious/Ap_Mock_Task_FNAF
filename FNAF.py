import pygame
import random
import time
pygame.init()
    
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")
freddy1=pygame.image.load("freddy1.png")
freddy2=pygame.image.load("freddy2.png")
freddy3=pygame.image.load("freddy3.png")
freddy4=pygame.image.load("freddy4.png")

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User clicked the close button
            running = False

    # Game logic (e.g., update object positions)

    # Drawing
    screen.blit(freddy1, (0,0))
    time.sleep(.2)
    pygame.display.update()
    screen.blit(freddy2, (0,0))
    time.sleep(.4)
    pygame.display.update()
    screen.blit(freddy3, (0,0))
    time.sleep(.2)
    pygame.display.update()
    screen.blit(freddy4, (0,0))
    time.sleep(.1)
    pygame.display.update()
    time.sleep(.2)
    # Update the display
    pygame.display.flip() # or pygame.display.update()
#^ Use of AI for pygame starter ^

pygame.quit()