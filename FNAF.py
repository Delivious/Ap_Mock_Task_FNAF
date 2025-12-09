import pygame
import time
import random
pygame.init()
# All images found on google images, the FNAF characters are property of Scott Cawthon and used for educational purposes only.    

screen_width = 2500
screen_height = 1500
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
    while True:
        fred=random.randint(1,4)
        if fred==1:
            screen.blit(freddy1,(500,0))
        elif fred==2:
            screen.blit(freddy2,(500,0))
        elif fred==3:
            screen.blit(freddy3,(500,0))
        elif fred==4:
            screen.blit(freddy4,(500,0))
        pygame.display.update()       
        time.sleep(0.2)

    pygame.display.flip() # or pygame.display.update()

# ^ Use of AI for pygame starter ^

pygame.quit()

