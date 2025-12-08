import pygame
pygame.init()
    
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User clicked the close button
            running = False

    # Game logic (e.g., update object positions)

    # Drawing
    screen.fill((0, 0, 0)) # Fill the screen with black (RGB)

    # Update the display
    pygame.display.flip() # or pygame.display.update()
#^ Use of AI for pygame starter ^

pygame.quit()