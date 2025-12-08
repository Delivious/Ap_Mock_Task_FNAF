import pygame
pygame.init()
    
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")
freddy1=pygame.image.load("freddy1.png")
freddy2=pygame.image.load("freddy2.png")
freddy3=pygame.image.load("freddy3.png")
freddy4=pygame.image.load("freddy4.png")
freddy5=pygame.image.load("freddy5.png")
freddy6=pygame.image.load("freddy6.png")
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User clicked the close button
            running = False

    # Game logic (e.g., update object positions)

    # Drawing
    screen.fill((0, 0, 0)) # Fill the screen with black (RGB)
    screen.blit(freddy6, (0,0))
    # Update the display
    pygame.display.flip() # or pygame.display.update()

# ^ Use of AI for pygame starter ^

pygame.quit()

